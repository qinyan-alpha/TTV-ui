# flake8: noqa: E402
import logging
import re_matching
logging.getLogger("numba").setLevel(logging.WARNING)
logging.getLogger("markdown_it").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("matplotlib").setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.INFO, format="| %(name)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

import torch
import commons
from text.symbols import symbols
from text import cleaned_text_to_sequence, get_bert
from text.cleaner import clean_text
import numpy as np


net_g = None


def get_text(text, language_str, hps,device):
    norm_text, phone, tone, word2ph = clean_text(text, language_str)
    phone, tone, language = cleaned_text_to_sequence(phone, tone, language_str)

    if hps.data.add_blank:
        phone = commons.intersperse(phone, 0)
        tone = commons.intersperse(tone, 0)
        language = commons.intersperse(language, 0)
        for i in range(len(word2ph)):
            word2ph[i] = word2ph[i] * 2
        word2ph[0] += 1
    bert = get_bert(norm_text, word2ph, language_str, device)
    del word2ph
    assert bert.shape[-1] == len(phone), phone

    if language_str == "ZH":
        bert = bert
        ja_bert = torch.zeros(768, len(phone))
    elif language_str == "JP":
        ja_bert = bert
        bert = torch.zeros(1024, len(phone))
    else:
        bert = torch.zeros(1024, len(phone))
        ja_bert = torch.zeros(768, len(phone))

    assert bert.shape[-1] == len(
        phone
    ), f"Bert seq len {bert.shape[-1]} != {len(phone)}"

    phone = torch.LongTensor(phone)
    tone = torch.LongTensor(tone)
    language = torch.LongTensor(language)
    return bert, ja_bert, phone, tone, language


def infer(text, sdp_ratio, noise_scale, noise_scale_w, length_scale, sid, language,hps,device,net_g):
    bert, ja_bert, phones, tones, lang_ids = get_text(text, language, hps,device)
    with torch.no_grad():
        x_tst = phones.to(device).unsqueeze(0)
        tones = tones.to(device).unsqueeze(0)
        lang_ids = lang_ids.to(device).unsqueeze(0)
        bert = bert.to(device).unsqueeze(0)
        ja_bert = ja_bert.to(device).unsqueeze(0)
        x_tst_lengths = torch.LongTensor([phones.size(0)]).to(device)
        del phones
        speakers = torch.LongTensor([hps.data.spk2id[sid]]).to(device)
        audio = (
            net_g.infer(
                x_tst,
                x_tst_lengths,
                speakers,
                tones,
                lang_ids,
                bert,
                ja_bert,
                sdp_ratio=sdp_ratio,
                noise_scale=noise_scale,
                noise_scale_w=noise_scale_w,
                length_scale=length_scale,
            )[0][0, 0]
            .data.cpu()
            .float()
            .numpy()
        )
        del x_tst, tones, lang_ids, bert, x_tst_lengths, speakers
        torch.cuda.empty_cache()
        return audio


def generate_audio(slices, sdp_ratio, noise_scale, noise_scale_w, length_scale, speaker, language,hps,device,net_g):
    audio_list = []
    silence = np.zeros(hps.data.sampling_rate // 2)
    with torch.no_grad():
        for piece in slices:
            audio = infer(
                piece,
                sdp_ratio=sdp_ratio,
                noise_scale=noise_scale,
                noise_scale_w=noise_scale_w,
                length_scale=length_scale,
                sid=speaker,
                language=language,
                hps=hps,
                device=device,
                net_g = net_g
            )
            audio_list.append(audio)
            audio_list.append(silence)  # 将静音添加到列表中
    return audio_list


def tts_fn(text: str, speaker, sdp_ratio, noise_scale, noise_scale_w, length_scale, language,hps,device,net_g):
    audio_list = []
    if language == "mix":
        bool_valid, str_valid = re_matching.validate_text(text)
        if not bool_valid:
            return str_valid, (hps.data.sampling_rate, np.concatenate([np.zeros(hps.data.sampling_rate // 2)]))
        result = re_matching.text_matching(text)
        for one in result:
            _speaker = one.pop()
            for lang, content in one:
                audio_list.extend(
                    generate_audio(content.split("|"), sdp_ratio, noise_scale,
                                   noise_scale_w, length_scale, _speaker+'_'+lang.lower(), lang,hps,device,net_g)
                )
    else:
        audio_list.extend(
            generate_audio(text.split("|"), sdp_ratio, noise_scale, noise_scale_w, length_scale, speaker, 
                           language,hps,device,net_g))       
    audio_concat = np.concatenate(audio_list)
    return "Success", (hps.data.sampling_rate, audio_concat)

def convert_to_int(data):
    # 获取原始数据类型
    dtype = data.dtype
    
    # 根据类型转换到整数
    if dtype.kind == 'f': # 浮点数
        data = (data * 32767).astype(np.int16) 
    elif dtype.kind == 'i': # 整数
        pass  
    else:
        raise TypeError("Unsupported dtype")

    return data


 


