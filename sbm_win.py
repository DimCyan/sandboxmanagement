import os
import re


class SbmInit:  # 待测试
    @staticmethod
    def get_interpreter_path():
        """获取解释器-解释器所在文件夹位置与此文件在同一目录下，并命名为《pyinterpreter》"""
        interpreter_path = os.path.abspath('') + r'\pyinterpreter\python.exe'
        return interpreter_path

    @staticmethod
    def update_pip(interpreter_path):
        """升级pip版本"""
        msg = os.popen(
            f'{interpreter_path} -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/').read()
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
    def set_vpath():
        """修改vnev文件路径"""
        os.environ['WORKON_HOME'] = r'D:\envs'
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
        # print(next_str)
        if next_str == []:
            return 'no venv'
        else:
            return next_str


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
            r"(?<===============================================================================).*?(?===============================================================================)",
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
    def create_file(vname, filename):
        """新建py文件"""
        vpath = VenvOperation.get_venv_path() + '\\' + f'{vname}' + '\\'
        filename = filename + '.py'
        msg = os.popen(f'cd {vpath} && type nul> {filename}').read()
        return msg

    @staticmethod
    def del_file(vname, filename):
        """删除文件"""
        vpath = VenvOperation.get_venv_path() + '\\' + f'{vname}' + '\\'
        filename = filename + '.py'
        msg = os.popen(f'cd {vpath} && del {filename}').read()
        return msg

    @staticmethod
    def rn_file(vname, filename, nfilename):
        """文件重命名"""
        vpath = VenvOperation.get_venv_path() + '\\' + f'{vname}' + '\\'
        filename = filename + '.py'
        nfilename = nfilename + '.py'
        msg = os.popen(f'cd {vpath} && rename {filename} {nfilename}').read()
        return msg

    @staticmethod
    def get_file_list(vpath):
        """获取文件夹下文件列表，文件类型（待测试和修改），修改为list类型，新增file_type方法！！！！！！！"""
        filelist = os.listdir(vpath)
        print(filelist)
        for filename in filelist:
            print(filename)
            filetype = os.path.splitext(filename)[-1]
            if filetype == '':
                pass
            else:
                print(filetype)
            filepath = os.path.join(vpath, filename)
            print(filepath)
            if os.path.isdir(filepath):
                print(filename + ' is dir')

# if __name__ == '__main__':
#     pl_msg = PackageOperation.get_plist('test')
#     print(pl_msg)