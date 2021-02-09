import os
import re
import time
import tkinter as tk
from tkinter import filedialog

from werkzeug.utils import secure_filename


class SbmInit:  # 待测试
    @staticmethod
    def get_interpreter_path():
        """获取解释器-解释器所在文件夹位置与此文件在同一目录下，并命名为《pyinterpreter》"""
        interpreter_path = os.path.abspath('') + r'\pyinterpreter\python.exe'
        return interpreter_path

    @staticmethod
    def get_scripts_path():
        """获取pip位置"""
        scriptes_path = os.path.abspath('') + r'\pyinterpreter\Scripts'
        return scriptes_path

    @staticmethod
    def upgrade_pip(interpreter_path):
        """升级pip版本"""
        scripts_path = SbmInit.get_scripts_path()
        msg = os.popen(
            f'cd /d {scripts_path} && {interpreter_path} -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/').read()
        return msg

    @staticmethod
    def get_pyf_path():
        """选择py脚本"""
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.askopenfilename()
        return filepath


class VenvOperation:
    @staticmethod
    def set_vpath():
        """修改vnev文件路径"""
        base_path = os.path.abspath('') + r'\Envs'
        # os.environ['WORKON_HOME'] = r'D:\envs'
        os.environ['WORKON_HOME'] = fr'{base_path}'
        # pass

    @staticmethod
    def create_venv(vname):
        """新建虚拟环境"""
        VenvOperation.set_vpath()
        msg = os.popen(f'mkvirtualenv {vname}').read()
        return msg

    @staticmethod
    def activate_venv(vname, cmd=None):
        """激活虚拟环境并进入"""
        VenvOperation.set_vpath()
        if cmd:
            msg = os.popen(f'workon {vname} && {cmd}').read()
        else:
            msg = os.popen(f'workon {vname}').read()
        return msg

    @staticmethod
    def exit_env():
        """退出虚拟环境,pass"""
        VenvOperation.set_vpath()
        os.popen('deactivate')

    @staticmethod
    def switch_env():
        """切换虚拟环境,与激活虚拟环境一致,pass"""
        pass

    @staticmethod
    def rm_env(vname):
        """删除虚拟环境"""
        VenvOperation.set_vpath()
        msg = os.popen(f'rmvirtualenv {vname}').read()
        return msg

    @staticmethod
    def get_venv_path():
        """获取venv安装路径"""
        VenvOperation.set_vpath()
        sys_get_path = os.popen('lsvirtualenv').read()
        searchObj = re.findall(r'"(.*)"', sys_get_path)
        return searchObj[0]

    @staticmethod
    def get_venv_list():
        """获取所有虚拟环境名称"""
        VenvOperation.set_vpath()
        sys_get_name = os.popen('lsvirtualenv').read()
        first_str = "=============================================================================="
        head, sep, tail = sys_get_name.partition(first_str)
        clean_str = tail
        next_str = clean_str.split('\n')
        while '' in next_str:
            next_str.remove('')
        if next_str == []:
            return 'no venv'
        else:
            return next_str

    @staticmethod
    def get_venv_mtime(vpath):
        """获取虚拟环境修改日期"""
        return time.strftime(
            "%Y--%m--%d %H:%M:%S",
            time.localtime(
                os.path.getmtime(vpath)))


class PackageOperation:
    @staticmethod
    def install_package(pname, vname=None):
        """安装第三方库"""
        cmd = f'pip install {pname} -i https://pypi.tuna.tsinghua.edu.cn/simple/'
        if vname is not None:
            msg = VenvOperation.activate_venv(vname, cmd)
            return msg
        else:
            msg = os.popen(cmd).read()
            return '安装在虚拟环境外\n', msg

    @staticmethod
    def get_plist(vname):
        """获取虚拟环境内安装的第三方库列表,需修改！！！！！！！！"""
        cmd = 'lssitepackages'
        contents = VenvOperation.activate_venv(vname, cmd)
        mylist = re.findall(
            r"(?<===============================================================================).*?"
            r"(?===============================================================================)",
            contents, re.DOTALL)
        mylist = mylist[0].split('\n')
        while '' in mylist:
            mylist.remove('')
        return mylist[:-2]

    @staticmethod
    def uninstall_package(pname, vname):
        """卸载第三方库"""
        cmd = f'pip uninstall {pname} --yes'
        msg = VenvOperation.activate_venv(vname, cmd)
        return msg


class FileOperation:
    @staticmethod
    def get_file_path(file):
        """获取上传文件的路径"""
        basepath = os.path.dirname('')
        upload_path = os.path.join(basepath, r'static\uploads',
                                   secure_filename(file.filename))
        file.save(upload_path)
        return upload_path
