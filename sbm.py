import os
import tkinter as tk
from tkinter import filedialog


def get_interpreter():
    """获取解释器-解释器所在文件夹位置与此文件在同一目录下，并命名为《pyinterpreter》"""
    interpreter_path = os.path.abspath('') + '/pyinterpreter/python.exe'
    return interpreter_path


def update_pip(interpreter_path):
    """升级pip版本"""
    msg = os.popen(f'{interpreter_path} -m pip install --upgrade pip')
    return msg


def set_env(interpreter_path):
    """更改环境变量"""
    os.system(f'set Path={interpreter_path};%Path%')
    env_path = os.popen('set Path')
    return env_path


def p_location():
    """选择项目位置"""
    root = tk.Tk()
    root.withdraw()
    folderpath = filedialog.askdirectory()
    os.system(f'cd {folderpath} && mkdir pylocation')
    folderpath = folderpath + '/pylocation'
    return folderpath


def create_venv(folderpath, vname):
    """新建虚拟环境"""
    os.popen(f'cd {folderpath} && virtualenv {vname}')
    vpath = folderpath + '/vname'
    return vpath


def activate_venv(vpath, cmd=None):
    """激活虚拟环境并进入"""
    if cmd:
        msg = os.popen(f'{vpath}/Scripts/activate && {cmd}')
    else:
        msg = os.popen(f'{vpath}/Scripts/activate')
    return msg


def create_pyfiles(vpath, filename):
    """新建py文件"""
    filename = filename + '.py'
    msg = os.popen(f'cd {vpath} && touch {filename}')
    return msg


def exit_env():
    """退出虚拟环境"""
    os.popen('deactivate')


def switch_env(vpath):
    """切换虚拟环境"""
    activate_venv(vpath)


def install_package(vpath, pname):
    """安装第三方库"""
    cmd = f'pip install {pname}'
    msg = activate_venv(vpath, cmd)
    return msg


def get_plist(vpath):
    """获取虚拟环境内安装的第三方库列表"""
    cmd = 'pip list'
    msg = activate_venv(vpath, cmd)
    return msg


def uninstall_package(vpath, pname):
    """卸载第三方库"""
    cmd = f'pip uninstall {pname}'
    msg = activate_venv(vpath, cmd)
    return msg


if __name__ == '__main__':
    interpreter_path = get_interpreter()
    folderpath = p_location()
    create_venv(folderpath)
    # update_pip(interpreter_path)
    # set_env(interpreter_path)
