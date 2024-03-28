import os
import zipfile
import shutil

current_dir = os.getcwd()
zip_file = "update.zip"
os.system('taskkill /im Cs2开服辅助.exe /f')
for root, dirs, files in os.walk(current_dir):
    for file_name in files:
        if file_name not in ["update.exe", "update.zip"]:
            os.remove(os.path.join(root, file_name))
    for dir_name in dirs:
        if dir_name not in ["update.exe", "update.zip"]:
            shutil.rmtree(os.path.join(root, dir_name), ignore_errors=True)
    # 解压ZIP文件到当前目录
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            file_info.filename = file_info.filename.encode('cp437').decode('gbk')
            zip_ref.extract(file_info, current_dir)

print("更新完成！")
