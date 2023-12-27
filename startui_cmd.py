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
            if file != 'startui.py' and file != 'logs' and file != 'config.ini' and file != 'startui_cmd.py':
                src_file = os.path.join(root, file)
                dst_file = os.path.join(zip_dir, file)
                shutil.copy(src_file, dst_file)
                print(file)
            if file == 'config.ini':
                src_file = os.path.join(root, file)
                dst_file = os.path.join(zip_dir, 'config_new.ini')
                shutil.copy(src_file, dst_file)                

    # 删除目标文件夹
    shutil.rmtree(target_folder)
    

if  __name__ == '__main__':    
    if allow_update == 'yes':
        config_new = configparser.ConfigParser()
        config_new.read('config_new.ini')        
        now_version = config.get('setting','version')
        update_version = "{:.2f}".format(float(now_version) + 0.01)    
        unzip_and_move_files('TTV-ui-main.zip')
        allow_update = 'no'
        config.set('setting', 'allow_update', allow_update)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        if config_new.has_option('setting', 'version'):
            new_version = config_new.get('setting', 'version')
            config.set('setting', 'version', new_version)
        for section in config_new.sections():
            for option in config_new.options(section):
                if not config.has_option(section, option):
                    value = config_new.get(section, option)
                    config.set(section, option, value)
        with open('config.ini', 'w') as config_file:
            config.write(config_file)    
    bat_file_path = 'Text to voice.bat'
    subprocess.call(bat_file_path)