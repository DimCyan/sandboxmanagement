import os
import tkinter as tk
from tkinter import filedialog


class SbmInit:
    @staticmethod
    def get_interpreter():
        """获取解释器-解释器所在文件夹位置与此文件在同一目录下，并命名为《pyinterpreter》"""
        interpreter_path = os.path.abspath('') + r'\pyinterpreter\python.exe'
        return interpreter_path

    @staticmethod
    def update_pip(interpreter_path):
        """升级pip版本"""
        msg = os.popen(
            f'{interpreter_path} -m pip install --upgrade pip').read()
        return msg

    @staticmethod
    def set_env(interpreter_path):
        """更改环境变量"""
        os.system(f'set Path={interpreter_path};%Path%')
        env_path = os.popen('set Path').read()
        return env_path

    @staticmethod
    def p_location():
        """选择项目位置"""
        root = tk.Tk()
        root.withdraw()
        folderpath = filedialog.askdirectory()
        os.system(f'cd {folderpath} && mkdir pylocation')
        folderpath = folderpath + r'\pylocation'
        return folderpath


class VenvOperation:
    @staticmethod
    def create_venv(folderpath, vname):
        """新建虚拟环境"""
        os.popen(f'cd {folderpath} && virtualenv {vname}').read()
        vpath = folderpath + rf'\{vname}'
        return vpath

    @staticmethod
    def activate_venv(vpath, cmd=None):
        """激活虚拟环境并进入"""
        if cmd:
            msg = os.popen(rf'{vpath}\Scripts\activate && {cmd}').read()
        else:
            msg = os.popen(rf'{vpath}\Scripts\activate').read()
        return msg

    @staticmethod
    def exit_env():
        """退出虚拟环境"""
        os.popen('deactivate')

    def switch_env(self, vpath):
        """切换虚拟环境"""
        self.activate_venv(vpath)


class ackageOperation:
    @staticmethod
    def install_package(pname, vpath=None):
        """安装第三方库"""
        cmd = f'pip install {pname} -i https://pypi.tuna.tsinghua.edu.cn/simple/'
        if vpath:
            msg = VenvOperation.activate_venv(vpath, cmd)
            return msg
        else:
            msg = os.popen(cmd).read()
            return msg

    @staticmethod
    def get_plist(vpath):
        """获取虚拟环境内安装的第三方库列表"""
        cmd = 'pip list'
        msg = VenvOperation.activate_venv(vpath, cmd)
        return msg

    @staticmethod
    def uninstall_package(vpath, pname):
        """卸载第三方库"""
        cmd = f'pip uninstall {pname}'
        msg = VenvOperation.activate_venv(vpath, cmd)
        return msg


class file_operation():
    @staticmethod
    def create_pyfiles(vpath, filename):
        """新建py文件"""
        filename = filename + '.py'
        msg = os.popen(f'cd {vpath} && touch {filename}').read()
        return msg


if __name__ == '__main__':
    interpreter_path = SbmInit.get_interpreter()
    # folderpath = p_location()
    # create_venv(folderpath)
    # update_pip(interpreter_path)
    # set_env(interpreter_path)
