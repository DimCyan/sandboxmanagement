import os
import re


class SbmInit:
    @staticmethod
    def get_interpreter_path():
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

    """
    @staticmethod
    import tkinter as tk
    from tkinter import filedialog
    def p_location():
        # 选择项目位置
        root = tk.Tk()
        root.withdraw()
        folderpath = filedialog.askdirectory()
        os.system(f'cd {folderpath} && mkdir pylocation')
        folderpath = folderpath + r'\pylocation'
        return folderpath
    """


class VenvOperation:
    @staticmethod
    def create_venv(vname):
        """新建虚拟环境"""
        msg = os.popen(f'mkvirtualenv {vname}').read()
        return msg

    @staticmethod
    def activate_venv(vname, cmd=None):
        """激活虚拟环境并进入"""
        if cmd:
            msg = os.popen(f'workon {vname} && {cmd}').read()
        else:
            msg = os.popen(f'workon {vname}').read()
        return msg

    @staticmethod
    def exit_env():
        """退出虚拟环境"""
        os.popen('deactivate')

    @staticmethod
    def switch_env():
        """切换虚拟环境,与激活虚拟环境一致"""
        pass

    @staticmethod
    def rm_env(vname):
        """删除虚拟环境"""
        msg = os.popen(f'rmvirtualenv {vname}')
        return msg

    @staticmethod
    def get_venv_path():
        """获取venv安装路径"""
        sys_get_path = os.popen('lsvirtualvenv').read()
        searchObj = re.findall(r'"(.*)"', sys_get_path)
        return searchObj[0]

    @staticmethod
    def get_venv_list():
        """获取所有虚拟环境名称"""
        sys_get_name = os.popen('lsvirtualenv').read()
        first_str = "=============================================================================="
        head, sep, tail = sys_get_name.partition(first_str)
        clean_str = tail
        next_str = clean_str.split('\n')
        while '' in next_str:
            next_str.remove('')
        print(next_str)


class PackageOperation:
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


class FileOperation():
    @staticmethod
    def create_pyfiles(vpath, filename):
        """新建py文件"""
        filename = filename + '.py'
        msg = os.popen(f'cd {vpath} && touch {filename}').read()
        return msg


if __name__ == '__main__':
    interpreter_path = SbmInit.get_interpreter_path()
