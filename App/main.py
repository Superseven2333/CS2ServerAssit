import glob
import os
import shutil
import time
import zipfile

import psutil
import webview
import win32api
import win32ui
import win32con
import requests

local = os.getcwd()


def check_file():
    os.startfile("steam://rungameid/730")
    process_list = [p for p in psutil.process_iter(attrs=['pid', 'name', 'exe']) if p.info['name'] == 'cs2.exe']

    if process_list:
        # 获取第一个进程的可执行文件路径
        cs2_executable_path = process_list[0].info['exe']

        # 获取CS2程序的根目录
        cs2_root_directory = os.path.dirname(cs2_executable_path)
        with open("data/data.txt", "w") as file:
            file.write(cs2_root_directory)


file_list = []


def map_list():
    with open('data/data.txt', 'r', encoding='UTF-8') as file:
        file_content = file.read()
    os.chdir(file_content)
    os.chdir("../../")
    os.chdir("./csgo/maps")

    maps_folder = os.getcwd()
    for file_path in glob.glob(os.path.join("*.vpk")):
        file_name = os.path.basename(file_path)
        file_list.append(file_name)
        os.chdir(local)
    os.chdir(file_content)
    os.chdir("../../")
    os.chdir("../../")
    os.chdir("../")
    os.chdir("./workshop/content/730")

    def find_vpk_files(folder_path):
        vpk_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".vpk"):
                    vpk_files.append(os.path.join(root, file))
        return vpk_files

    folder_path = "../"
    vpk_files = find_vpk_files(folder_path)
    for i in vpk_files:
        file_path = i
        shutil.copy(file_path, maps_folder)
    os.chdir(local)
    with open('data/maplist.txt', 'w', encoding='UTF-8') as file:
        for a in file_list:
            file.write(a + '|')


with open('data/data.txt', 'r', encoding='UTF-8') as file:
    game_text = file.read()

if game_text == '':
    result = win32api.MessageBox(0, "请先进行环境检测", "提示", win32con.MB_YESNO)
    if result == win32con.IDYES:
        os.startfile("steam://rungameid/730")
        time.sleep(8)
        process_list = [p for p in psutil.process_iter(attrs=['pid', 'name', 'exe']) if p.info['name'] == 'cs2.exe']
        target_process = 'cs2.exe'
        if process_list:
            # 获取第一个进程的可执行文件路径
            cs2_executable_path = process_list[0].info['exe']
            # 获取CS2程序的根目录
            cs2_root_directory = os.path.dirname(cs2_executable_path)
            with open("data/data.txt", "w") as file:
                file.write(cs2_root_directory)
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == target_process:
                    proc.kill()
                    Tresult = win32api.MessageBox(0, "需要重启软件", "提示", win32con.MB_YESNO)
                    if Tresult == win32con.IDYES:
                        os.system("taskkill /im Cs2开服辅助.exe /f")
                    else:
                        os.system("taskkill /im Cs2开服辅助.exe /f")


    elif result == win32con.IDNO:
        pass
    else:
        pass


class Api:
    def __init__(self):
        self.vac = True
        self.wksp = False
        self.map = ''
        self.gametype = ''

    def ChangeCfg(self):
        cfgfile = os.chdir(game_text)
        cfgfile = os.chdir("../../")
        cfgfile = os.chdir("../../")
        cfgfile = os.chdir("./csgo/cfg")
        os.startfile("server.cfg")
        os.chdir(local)

    def is_process_running(process_name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                return True
        return False

    def shutdown(self):
        os.system("taskkill /im Cs2开服辅助.exe /f")

    def map_list(self, selected_name):
        global map
        self.map = selected_name

    def mode_list(self, select_name):
        global gametype
        self.gametype = select_name

    def vactf(self, truefalse):
        self.vac = truefalse

    def wksptf(self, truefalse):
        self.wksp = truefalse

    def startpy(self, ip, port, maxplayers, rcname):
        target_process = 'cs2.exe'
        vac = str(self.vac)
        wksp = str(self.wksp)
        map = self.map
        gametype = self.gametype

        with open('data/type.txt', 'w', encoding='UTF-8') as file:
            file.write(str(port) + "|" + str(ip) + "|" + str(maxplayers) + "|" + map + "|" + vac + "|" + gametype)

        RunLocal = os.getcwd()

        if not Api.is_process_running(target_process):
            if wksp == "True":
                if vac == "True":
                    with open("data/data.txt", "r", encoding='UTF-8') as file:
                        file_content = file.read()

                    os.chdir(file_content)
                    command = f"start cs2.exe -dedicated -maxplayers {maxplayers} -console +map de_mirage -high -port {port} -ip {ip} -console +host_workshop_map {map} +hostname {rcname}"
                    if str(gametype) == '休闲':
                        command += " +game_type 0 +game_mode 0 +exec server.cfg"
                    elif str(gametype) == '竞技':
                        command += " +game_type 0 +game_mode 1 +exec server.cfg"
                    elif str(gametype) == '死斗':
                        command += " +game_type 1 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '回防':
                        command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                    elif str(gametype) == '搭档':
                        command += " +game_type 0 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '军备':
                        command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                    os.system(command)
                    os.chdir(RunLocal)
                else:
                    with open("data/data.txt", "r", encoding='UTF-8') as file:
                        file_content = file.read()

                    os.chdir(file_content)
                    command = f"start cs2.exe -dedicated -maxplayers {maxplayers} -console +map de_mirage -high -port {port} -ip {ip} -console +host_workshop_map {map} -insecure +hostname {rcname}"
                    if str(gametype) == '休闲':
                        command += " +game_type 0 +game_mode 0 +exec server.cfg"
                    elif str(gametype) == '竞技':
                        command += " +game_type 0 +game_mode 1 +exec server.cfg"
                    elif str(gametype) == '死斗':
                        command += " +game_type 1 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '回防':
                        command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                    elif str(gametype) == '搭档':
                        command += " +game_type 0 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '军备':
                        command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                    os.system(command)
                    os.chdir(RunLocal)
            else:
                if vac == "True":
                    with open("data/data.txt", "r", encoding='UTF-8') as file:
                        file_content = file.read()

                    os.chdir(file_content)
                    command = f"start cs2.exe -dedicated -maxplayers {maxplayers} -console +map {map} -high -port {port} -ip {ip} -console +hostname {rcname}"
                    if str(gametype) == '休闲':
                        command += " +game_type 0 +game_mode 0 +exec server.cfg"
                    elif str(gametype) == '竞技':
                        command += " +game_type 0 +game_mode 1 +exec server.cfg"
                    elif str(gametype) == '死斗':
                        command += " +game_type 1 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '回防':
                        command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                    elif str(gametype) == '搭档':
                        command += " +game_type 0 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '军备':
                        command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                    os.system(command)
                    os.chdir(RunLocal)
                else:
                    with open("data/data.txt", "r", encoding='UTF-8') as file:
                        file_content = file.read()

                    os.chdir(file_content)
                    command = f"start cs2.exe -dedicated -insecure -maxplayers {maxplayers} -console +map {map} -high -port {port} -ip {ip} -console +hostname {rcname}"
                    if str(gametype) == '休闲':
                        command += " +game_type 0 +game_mode 0 +exec server.cfg"
                    elif str(gametype) == '竞技':
                        command += " +game_type 0 +game_mode 1 +exec server.cfg"
                    elif str(gametype) == '死斗':
                        command += " +game_type 1 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '回防':
                        command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                    elif str(gametype) == '搭档':
                        command += " +game_type 0 +game_mode 2 +exec server.cfg"
                    elif str(gametype) == '军备':
                        command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                    os.system(command)
                    os.chdir(RunLocal)
        else:
            Kresult = win32api.MessageBox(0, "CS2正在运行", "提示", win32con.MB_YESNO)
            if Kresult == win32con.IDYES:
                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] == target_process:
                        proc.kill()
                        if wksp == "True":
                            if vac == "True":
                                with open("data/data.txt", "r", encoding='UTF-8') as file:
                                    file_content = file.read()

                                os.chdir(file_content)
                                command = f"start cs2.exe -dedicated -maxplayers {maxplayers} -console +map de_mirage -high -port {port} -ip {ip} -console +host_workshop_map {map} +hostname {rcname}"
                                if str(gametype) == '休闲':
                                    command += " +game_type 0 +game_mode 0 +exec server.cfg"
                                elif str(gametype) == '竞技':
                                    command += " +game_type 0 +game_mode 1 +exec server.cfg"
                                elif str(gametype) == '死斗':
                                    command += " +game_type 1 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '回防':
                                    command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                                elif str(gametype) == '搭档':
                                    command += " +game_type 0 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '军备':
                                    command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                                os.system(command)
                                os.chdir(RunLocal)
                            else:
                                with open("data/data.txt", "r", encoding='UTF-8') as file:
                                    file_content = file.read()

                                os.chdir(file_content)
                                command = f"start cs2.exe -dedicated -maxplayers {maxplayers} -console +map de_mirage -high -port {port} -ip {ip} -console +host_workshop_map {map} -insecure +hostname {rcname}"
                                if str(gametype) == '休闲':
                                    command += " +game_type 0 +game_mode 0 +exec server.cfg"
                                elif str(gametype) == '竞技':
                                    command += " +game_type 0 +game_mode 1 +exec server.cfg"
                                elif str(gametype) == '死斗':
                                    command += " +game_type 1 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '回防':
                                    command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                                elif str(gametype) == '搭档':
                                    command += " +game_type 0 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '军备':
                                    command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                                os.system(command)
                                os.chdir(RunLocal)
                        else:
                            if vac == "True":
                                with open("data/data.txt", "r", encoding='UTF-8') as file:
                                    file_content = file.read()

                                os.chdir(file_content)
                                command = f"start cs2.exe -dedicated -maxplayers {maxplayers} -console +map {map} -high -port {port} -ip {ip} -console +hostname {rcname}"
                                if str(gametype) == '休闲':
                                    command += " +game_type 0 +game_mode 0 +exec server.cfg"
                                elif str(gametype) == '竞技':
                                    command += " +game_type 0 +game_mode 1 +exec server.cfg"
                                elif str(gametype) == '死斗':
                                    command += " +game_type 1 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '回防':
                                    command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                                elif str(gametype) == '搭档':
                                    command += " +game_type 0 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '军备':
                                    command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                                os.system(command)
                                os.chdir(RunLocal)
                            else:
                                with open("data/data.txt", "r", encoding='UTF-8') as file:
                                    file_content = file.read()

                                os.chdir(file_content)
                                command = f"start cs2.exe -dedicated -insecure -maxplayers {maxplayers} -console +map {map} -high -port {port} -ip {ip} -console +hostname {rcname}"
                                if str(gametype) == '休闲':
                                    command += " +game_type 0 +game_mode 0 +exec server.cfg"
                                elif str(gametype) == '竞技':
                                    command += " +game_type 0 +game_mode 1 +exec server.cfg"
                                elif str(gametype) == '死斗':
                                    command += " +game_type 1 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '回防':
                                    command += " +sv_skirmish_id 12 +game_type 0 +game_mode 0 +exec gamemode_retakecasual.cfg +exec server.cfg"
                                elif str(gametype) == '搭档':
                                    command += " +game_type 0 +game_mode 2 +exec server.cfg"
                                elif str(gametype) == '军备':
                                    command += " +game_type 1 +game_mode 0 +exec server.cfg +sv_skirmish_id 10"

                                os.system(command)
                                os.chdir(RunLocal)

    def update(self):
        version = "V1.17"
        content = requests.get("xg.frp.one:43810")
        content = content.text
        if version == content:
            win32api.MessageBox(0, "已是最新", "检查更新", win32con.MB_OK)
        elif content != version:
            r = win32api.MessageBox(0, "检查到最新版本", "检查更新", win32con.MB_YESNO)
            if r == win32con.IDYES:
                resp = requests.get("" + content)
                save = './' + 'update' + '.zip'
                with open(save, 'wb') as file:
                    file.write(resp.content)
                re = win32api.MessageBox(0, "现在更新?", " ", win32con.MB_YESNO)
                if re == win32con.IDYES:
                    os.system("1.bat")

                else:
                    pass
            else:
                pass

    def check_file(self):
        target_process = 'cs2.exe'
        os.startfile("steam://rungameid/730")
        time.sleep(5.5)
        if not Api.is_process_running(target_process):
            process_list = [p for p in psutil.process_iter(attrs=['pid', 'name', 'exe']) if p.info['name'] == 'cs2.exe']

            if process_list:
                # 获取第一个进程的可执行文件路径
                cs2_executable_path = process_list[0].info['exe']

                # 获取CS2程序的根目录
                cs2_root_directory = os.path.dirname(cs2_executable_path)
                with open("data/data.txt", "w") as file:
                    file.write(cs2_root_directory)
                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] == target_process:
                        proc.kill()
        else:
            time.sleep(5.5)
            process_list = [p for p in psutil.process_iter(attrs=['pid', 'name', 'exe']) if p.info['name'] == 'cs2.exe']

            if process_list:
                # 获取第一个进程的可执行文件路径
                cs2_executable_path = process_list[0].info['exe']

                # 获取CS2程序的根目录
                cs2_root_directory = os.path.dirname(cs2_executable_path)
                with open("data/data.txt", "w") as file:
                    file.write(cs2_root_directory)
                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] == target_process:
                        proc.kill()

    def vac_fix(self):
        os.system('net start "steam client service"')
        process_list = [p for p in psutil.process_iter(attrs=['pid', 'name', 'exe']) if
                        p.info['name'] == 'steamservice.exe']

        if process_list:
            # 获取第一个进程的可执行文件路径
            steamservice_executable_path = process_list[0].info['exe']

            # 获取CS2程序的根目录
            steamservice_root_directory = os.path.dirname(steamservice_executable_path)

        process_list2 = [p for p in psutil.process_iter(attrs=['pid', 'name', 'exe']) if
                         p.info['name'] == 'steam.exe']

        if process_list2:
            # 获取第一个进程的可执行文件路径
            steam_executable_path = process_list[0].info['exe']

            # 获取CS2程序的根目录
            steam_root_directory = os.path.dirname(steam_executable_path)

        os.system(steamservice_root_directory + " /install")
        os.system(steamservice_root_directory + " /repair")

        os.system('taskkill /f /im %s' % 'steam.exe')
        os.system("start" + str(steam_root_directory))

    def install_plugins(self):
        os.chdir(local)
        zipF = win32ui.CreateFileDialog(1)
        zipF.SetOFNInitialDir('xxxxxxxxx')
        zipF.DoModal()
        fileName = zipF.GetPathName()
        with open("data/data.txt", "r", encoding='UTF-8') as file:
            file_content = file.read()
        os.chdir(file_content)
        os.chdir("../../")
        os.chdir("./csgo")
        extract =os.getcwd()

        with zipfile.ZipFile(fileName, 'r') as zip_ref:
            zip_ref.extractall(extract)
            os.chdir(local)

        os.chdir(local)
        Nname = "gameinfo.gi"
        ONa="gameinfo1.gi"
        os.remove(extract+"/gameinfo.gi")
        shutil.copy("./data/gameinfo1.gi",extract)
        os.rename(os.path.join(extract, ONa), os.path.join(extract, Nname))
        win32api.MessageBox(0, "安装成功", "提示", win32con.MB_YESNO)

    def uninstall_plugins_gi(self):
        os.chdir(local)
        with open("data/data.txt", "r", encoding='UTF-8') as file:
            file_content = file.read()
        os.chdir(file_content)
        os.chdir("../../")
        os.chdir("./csgo")
        extract =os.getcwd()
        os.remove(extract+"/gameinfo.gi")
        os.chdir(local)
        shutil.copy("./data/gameinfo.gi", extract)
        win32api.MessageBox(0, "卸载插件引导成功", "提示", win32con.MB_YESNO)

    def uninstall_plugins(self):
        os.chdir(local)
        with open("data/data.txt", "r", encoding='UTF-8') as file:
            file_content = file.read()
        os.chdir(file_content)
        os.chdir("../../")
        os.chdir("./csgo")
        extract =os.getcwd()
        shutil.rmtree(extract+"/addons")
        win32api.MessageBox(0, "卸载插件文件成功", "提示", win32con.MB_YESNO)
# def steamcmd(self):
#     # 构建SteamCMD命令
#     command = subprocess.Popen(['./steamcmd.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
#
#     # 执行SteamCMD命令
#     subprocess.run(command, capture_output=True, text=True,encoding="UTF-8")
#     command.stdin.write('login anonymous\n')
#     command.stdin.flush()
#     output = command.stdout.readline()
#     # print(output.strip())  # 输出控制台输出



if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Cs2开服辅助', 'data/index.html', frameless=True, js_api=api, width=350, height=400)
    map_list()
    webview.start()
