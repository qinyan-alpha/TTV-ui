import configparser
import zipfile
import os
import shutil
import subprocess


config = configparser.ConfigParser()
config.read('config.ini')
allow_update = config.get('setting','allow_update')

    
def unzip_and_move_files(zip_file_path):
    # 获取ZIP文件的目录和文件名
    zip_dir, zip_filename = os.path.split(zip_file_path)

    # 创建目标文件夹
    target_folder = os.path.join(zip_dir, os.path.splitext(zip_filename)[0])
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 解压ZIP文件到目标文件夹
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(target_folder)

    # 移动文件到当前目录
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if file != 'startui.py' and file != 'logs' and file != 'config.ini' and file != 'startui(with cmd).py':
                src_file = os.path.join(root, file)
                dst_file = os.path.join(zip_dir, file)
                shutil.copy(src_file, dst_file)
                print(file)

    # 删除目标文件夹
    shutil.rmtree(target_folder)
    os.remove(zip_file_path)

if  __name__ == '__main__':    
    if allow_update == 'yes':
        now_version = config.get('setting','version')
        update_version = "{:.2f}".format(float(now_version) + 0.01)
        need_zip = update_version + 'zip'    
        unzip_and_move_files(need_zip)
        allow_update = 'no'
        config.set('setting', 'allow_update', allow_update)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            
    bat_file_path = 'Text to voice.bat'
    subprocess.call(bat_file_path) 