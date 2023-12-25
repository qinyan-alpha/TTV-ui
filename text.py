from PySide6.QtWidgets import QApplication, QWidget , QVBoxLayout,QLabel,QMainWindow
from PySide6.QtGui import QFont,QPixmap,QMouseEvent
from PySide6.QtCore import Qt,QTimer,QPropertyAnimation, QRect,QEasingCurve,QThread, Signal
import sys
sys.path.append('.')
from Ui_demoui import Ui_MainWindow
import os
import utils
import torch
import sys
from models import SynthesizerTrn
from text.symbols import symbols
import time
from infering import tts_fn,convert_to_int
import scipy
import logging
import simpleaudio as sa
import threading
import configparser

logging.getLogger("numba").setLevel(logging.WARNING)
logging.getLogger("markdown_it").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("matplotlib").setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.INFO, format="| %(name)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
update_url = config.get('setting','update_url')


class Loadingwindow(QMainWindow):
    def __init__(self):
        self.infering = False
        self.run = False
        self.model = None
        self.value1 = 0.2
        self.value2 = 1
        self.value3 = 0.9
        self.value4 = 0.9
        self.duration = 0
        self.audio_data = None
        self.sample_rate = None
        self.play = False
        self.play_time = 0
        self.play_start = False        
        self.t3 = 0
        self.t4 = 0
        self.visiable = True
        self.max = False
        self.min = False
        self.start_pos = None
        self.outboder = False
              
        self.speaker = self.config = self.device = self._device = self.hps = self.result = self.net_g = None                             
        log_folder = "./logs"
                
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        widgets.btn_home_2.clicked.connect(self.buttonClick)
        widgets.toggleLeftBox.clicked.connect(self.buttonClick)
        widgets.inferbutton.clicked.connect(self.inferbutton)
        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.pushButton_2.clicked.connect(self.inferparsersetting_visiable)
        widgets.save.clicked.connect(self.buttonClick)
        widgets.play.clicked.connect(self.play_threading)
        widgets.closeAppBtn.clicked.connect(self.close)
        widgets.maximizeRestoreAppBtn.clicked.connect(self.max_windows)
        widgets.minimizeAppBtn.clicked.connect(self.min_windows)
        widgets.changeoutboderAppBtn.clicked.connect(self.buttonClick)
        widgets.lineEdit.setText(update_url)
        widgets.lineEdit.textChanged.connect(self.updateurl)
        
        folder_names = [name for name in os.listdir(log_folder) if os.path.isdir(os.path.join(log_folder, name))]
        #print(type(folder_names))
        widgets.comboBox_3.addItems(folder_names)
        widgets.comboBox_3.currentIndexChanged.connect(self.handle_combobox3_selection)
        widgets.comboBox_4.currentIndexChanged.connect(self.handle_combobox4_selection)
        widgets.devicecomboBox.currentIndexChanged.connect(self.handle_device_selection)
        widgets.horizontalSlider1.valueChanged.connect(self.handle_slider_change)
        widgets.horizontalSlider2.valueChanged.connect(self.handle_slider_change)
        widgets.horizontalSlider3.valueChanged.connect(self.handle_slider_change)
        widgets.horizontalSlider4.valueChanged.connect(self.handle_slider_change)
        widgets.horizontalSlider4.valueChanged.connect(self.handle_slider_change)
        widgets.wavslider.sliderMoved.connect(self.wavslidermove)       
        self.handle_combobox3_selection()
        self.now_device()
        self.handle_device_selection()        
        play_thread1 = threading.Thread(target=self.play_threading1)
        play_thread2 = threading.Thread(target=self.play_threading2)
        play_thread1.start()
        play_thread2.start()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #widgets.toggleLeftBox.connect(self.buttonClick)

        

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        # SHOW HOME PAGE
        if btnName == "btn_home_2":
            widgets.stackedWidget.setCurrentWidget(widgets.page_1)
        if btnName == "toggleLeftBox":
            widgets.stackedWidget.setCurrentWidget(widgets.page_setting)              
        if btnName == "pushButton":
            if self.run == False:
                self.run = True
                if self.model :
                    widgets.pushButton.setEnabled(False)
                    widgets.pushButton.setStyleSheet("background-image: url(:/icon/uiimage/button/icons/cil-media-stop.png);background-color: rgb(40, 44, 52);")
                    widgets.stateshow.setText("加载模型中")
                    self.runmodel()
                    widgets.pushButton.setStyleSheet("background-image: url(:/icon/uiimage/button/icons/cil-media-stop.png);border-radius: 0px;")                    
                    widgets.stateshow.setText("加载模型完成")
                    widgets.pushButton.setEnabled(True)
                else:                    
                    print("不存在模型或者模型格式不对")
                    widgets.stateshow.setText("不存在模型或者模型格式不对")
                    widgets.pushButton.setStyleSheet("background-image: url(:/icon/uiimage/button/icons/cil-ban.png);border-radius: 0px;")                                                                        
                pass
            else :
                self.run = False
                widgets.pushButton.setStyleSheet("background-image: url(:/icon/uiimage/button/icons/cil-media-play.png);")
        if btnName == "save":
            if self.result:
                hps = self.hps
                audio_data = self.result[1][1]
                audio_data = convert_to_int(audio_data)
                self.audio_data = audio_data
                self.sample_rate = hps.data.sampling_rate                
                duration = len(audio_data) / hps.data.sampling_rate
                scipy.io.wavfile.write('./test.wav', hps.data.sampling_rate, audio_data)
                print(duration,type(duration))
                self.duration = round(duration,1)
                widgets.stateshow.setText("保存临时音频成功")
        if btnName == "changeoutboderAppBtn":
            if self.outboder == True:
                self.outboder = False
                self.setWindowFlags(Qt.FramelessWindowHint)
            else:
                self.outboder = True
                self.setWindowFlags(Qt.Window)
                self.show()                
                pass
                
                                                           

    def play_threading(self):
        if self.result:
            hps = self.hps
            audio_data = self.result[1][1]
            audio_data = convert_to_int(audio_data)
            self.audio_data = audio_data
            self.sample_rate = hps.data.sampling_rate                                       
            self.duration = len(self.audio_data) / self.hps.data.sampling_rate 
            if self.play == True:
                self.play = False
            elif  self.play == False:
                self.play = True
            self.t4 = self.t3
            self.t3 = time.time()
                             

                

    def handle_combobox3_selection(self):
        selected_folder = widgets.comboBox_3.currentText()
        widgets.comboBox_4.clear()
        if selected_folder != "": 
            print(f'当前选择模型为:{selected_folder}')
            self.model = 'logs\\' + selected_folder+'\\G_lastest.pth'
            print(self.model)
            self.config = 'logs\\' + selected_folder+'\\config.json'
            model_information = 'model:'+self.model+'\n'+'config:'+self.config
            widgets.model_information.setText(model_information)
            hps = utils.get_hparams_from_file(self.config)
            speaker_ids = hps.data.spk2id
            speakers = list(speaker_ids.keys())
            widgets.comboBox_4.addItems(speakers)
            self.speaker = widgets.comboBox_4.currentText()
            self.hps = hps
            print(self.speaker)
            
    def handle_combobox4_selection(self):
       if widgets.comboBox_4.currentText():
            self.speaker =  widgets.comboBox_4.currentText()
            print(self.speaker)


    def now_device(self):
        if torch.cuda.is_available():
            devices = []
            device_count = torch.cuda.device_count()
            for i in range(device_count):
                device_name = torch.cuda.get_device_name(i)
                devices.append(device_name)
            widgets.devicecomboBox.addItems(devices)
                
                  
    def handle_device_selection(self):
        self.device = widgets.devicecomboBox.currentIndex()
        

    def handle_slider_change(self):
        btn = self.sender()
        btnName = btn.objectName()
        if   btnName == 'horizontalSlider':
            pass
        if   btnName == 'horizontalSlider1':      
            value1 = widgets.horizontalSlider1.value()
            widgets.rate1.setText(str(round((value1*0.1),1)))
            self.value1 = value1
        if   btnName == 'horizontalSlider2':      
            value2 = widgets.horizontalSlider2.value()
            widgets.rate2.setText(str(round((value2*0.1),1)))
            self.value2 = value2
        if   btnName == 'horizontalSlider3':      
            value3 = widgets.horizontalSlider3.value()
            widgets.rate3.setText(str(round((value3*0.1),1)))
            self.value3 = value3
        if   btnName == 'horizontalSlider4':      
            value4 = widgets.horizontalSlider4.value()
            widgets.rate4.setText(str(round((value4*0.1),1)))
            self.value4 = value4                                        
        
     
    def runmodel(self):
        hps = self.hps
        if self.device == 0:
            self._device = (
                "cuda:0"
                if torch.cuda.is_available()
                else (
                    "mps"
                    if sys.platform == "darwin" and torch.backends.mps.is_available()
                    else "cpu"
                )
            )
            print(self._device)
        else:
            self._device = "cuda:"+str(int(self.device)-1)
            print(self._device)
        net_g = SynthesizerTrn(
            len(symbols),
            hps.data.filter_length // 2 + 1,
            hps.train.segment_size // hps.data.hop_length,
            n_speakers=hps.data.n_speakers,
            **hps.model,
        ).to(self._device) 
        self.net_g= net_g                  
        _ = utils.load_checkpoint(self.model, net_g, None, skip_optimizer=True)
    

    

    def inferparsersetting_visiable(self):        
        if self.visiable == False:
            widgets.inferparsersetting.setVisible(True)
            self.visiable = True
            widgets.pushButton_2.setStyleSheet("background-image: url(:/icons/images/icons/cil-arrow-bottom.png;background-repeat: no-repeat;background-position: center;")
                                                                                                
                                                                                                
        elif self.visiable == True:
            widgets.inferparsersetting.setVisible(False)
            self.visiable = False
            widgets.pushButton_2.setStyleSheet("background-image: url(:/icon/uiimage/button/icons/cil-arrow-top.png);background-repeat: no-repeat;background-position: center;")


    def play_threading1(self):
        play_obj = None
        while True:
            if self.result:           
                while True:
                    #print(self.play,self.play_start,self.play_time)
                    if self.play == True and self.play_start == False and self.play_time == 0:                            
                        play_obj = sa.play_buffer(audio_data=self.audio_data, # 获取音频数据
                                                sample_rate=self.sample_rate,# 采样率
                                                num_channels=1,#声道数,1为单声道,2为立体声
                                                bytes_per_sample=2)#样本字节数,通常是2(16位)或3(24位)
                        self.play_start = True
                        self.t1 = time.time()
                        self.play_change = False
                        widgets.stateshow.setText("播放")                        
                        self.play_stop = -1
                    elif self.play == False and play_obj and self.play_start == True:
                        play_obj.stop()
                        self.t3 = time.time() #暂停时间
                        self.play_start = False
                        self.play_change = True
                        #print('执行停止')
                        self.play_stop = -(self.play_stop)
                        print(self.play_stop)
                        #新的断点一
                        widgets.stateshow.setText("暂停")
                    elif self.play == True and self.play_start == False and self.play_time != 0:                                
                        played_samples = int(self.sample_rate * self.play_time)
                        new_audio_data = self.audio_data[played_samples:]
                        self.play_obj = sa.play_buffer(audio_data=new_audio_data, # 获取音频数据
                                                sample_rate=self.sample_rate,# 采样率
                                                num_channels=1,#声道数,1为单声道,2为立体声
                                                bytes_per_sample=2)#样本字节数,通常是2(16位)或3(24位)
                        self.play_start = True
                        #self.play_change = False
                        self.t4 = time.time() #重新执行时间
                        #print('执行片段')                                                                                                                                                                                  
                    time.sleep(0.1)                     
            time.sleep(0.1)            

    def play_threading2(self):
        while True:
            if  self.result:
                while True:
                    if self.play_start == True and self.play_time<self.duration and self.play == True:
                        time.sleep(0.01)
                        self.t2 = time.time() #更新时间
                        self.play_time += 0.02
                        widgets.wavslider.setValue(int(self.play_time * 100 / self.duration))
                        print(self.play_time,self.duration)
                        #show1,show2 = round(self.play_time,1),round(self.duration,1)
                        #widgets.wavnowvalue.setText(str(show1)+'/'+str(show2))
                    elif self.play_start == True and self.play_time>self.duration and self.play == True:
                        self.play_start = False
                        self.play = False
                        self.open = False 
                        self.play_time = 0
                        self.play_stop == -1
                        widgets.wavslider.setValue(0)
                    else:
                        time.sleep(0.1)
            time.sleep(0.1)
            
    def wavslidermove(self):
        wavsvalue = widgets.wavslider.value()
        print(wavsvalue)
        self.play_time = self.duration*wavsvalue/100
        print(self.play_time,self.duration)
        self.play = False
        self.play_start = False                        
                 
    
    def inferbutton(self):
        if self.run ==  False:
            pass
        else:                   
            widgets.inferbutton.setText("推理音频中")
            widgets.stateshow.setText("推理音频中")
            widgets.inferbutton.setEnabled(False)
            inferthreading = threading.Thread(target=self.infer)
            inferthreading.start()
            
            
    def infer(self):
            text = widgets.textEdit.toPlainText()
            print(text)
            hps = self.hps
            print(self._device)                
            language = widgets.comboBox_5.currentText()                
            (speaker, sdp_ratio, noise_scale, noise_scale_w, length_scale,
            ) = (self.speaker,self.value1,self.value2,self.value3,self.value4)
            self.result = tts_fn(text=text,
                        sdp_ratio=sdp_ratio,
                        noise_scale=noise_scale,
                        noise_scale_w=noise_scale_w,
                        length_scale=length_scale,
                        language=language,
                        speaker=speaker,
                        hps = hps,
                        device = self._device,
                        net_g = self.net_g,)                                
            print('推理完成')
            widgets.stateshow.setText("推理完成")                                            
            widgets.inferbutton.setText("推理")
            widgets.inferbutton.setEnabled(True)
            self.infering = True
            
    def close_app(self):
        self.close()
    
    def max_windows(self):
        if self.max == True:
            self.showNormal()
            self.max = False
        elif self.max == False:
            self.showMaximized()
            self.max = True
    
    def min_windows(self):
        if self.min == True:
            self.showNormal()
            self.min = False
        elif self.min == False:
            self.showMinimized()
            self.min = True

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        # PRINT MOUSE EVENTS
        #self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            self.mousePrsee = True
            self.offsetx = event.globalPosition().x() - self.pos().x()
            self.offsety = event.globalPosition().y() - self.pos().y()
            #print('按下')
            
    def mouseMoveEvent(self, event):
        if self.mousePrsee == True:
            x = event.globalPosition().x() - self.offsetx
            y = event.globalPosition().y() - self.offsety
            self.move(x, y)
        
            
    def mouseReleaseEvent(self, event):
        #self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            self.mousePrsee = False
            #print('松开')
             
    def updateurl(self):
        update_url = widgets.lineEdit.text()
        config.set('setting', 'update_url', update_url)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def get_update(self):
        pass          
                                                

if  __name__ == '__main__':
    app =   QApplication([])
    window = Loadingwindow()
    pixmap = QPixmap("icon.ico")
    app.setWindowIcon(pixmap)    
    window.show()
    app.exec() 