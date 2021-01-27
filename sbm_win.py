import os
import re

# 待测试


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

# PASS


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
        """退出虚拟环境,pass"""
        os.popen('deactivate')

    @staticmethod
    def switch_env():
        """切换虚拟环境,与激活虚拟环境一致,pass"""
        pass

    @staticmethod
    def rm_env(vname):
        """删除虚拟环境"""
        msg = os.popen(f'rmvirtualenv {vname}').read()
        return msg

    @staticmethod
    def get_venv_path():
        """获取venv安装路径"""
        sys_get_path = os.popen('lsvirtualenv').read()
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
        if next_str == []:
            return 'no venv'
        else:
            return next_str

# PASS


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
        """获取虚拟环境内安装的第三方库列表"""
        cmd = 'pip list'
        msg = VenvOperation.activate_venv(vname, cmd)
        return msg

    @staticmethod
    def uninstall_package(pname, vname):
        """卸载第三方库"""
        cmd = f'pip uninstall {pname} --yes'
        msg = VenvOperation.activate_venv(vname, cmd)
        return msg

# PASS


class FileOperation():
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

# if __name__ == '__main__':
# interpreter_path = SbmInit.get_interpreter_path()
# 新增venv
# c_msg = VenvOperation.create_venv('my_env3')
# print(c_msg)

# 激活进入
# a_msg = VenvOperation.activate_venv('my_env','pip list')
# print(a_msg)
# 删除
# r_msg = VenvOperation.rm_env('my_env3')
# print(r_msg)
# 获取venv目录路径
# v_path = VenvOperation.get_venv_path()
# print(v_path)
# 打印venvlist
# venv_list = VenvOperation.get_venv_list()
# print(venv_list)

# 安装第三方库pillow
# i_msg = PackageOperation.install_package('pillow','my_env2')
# print(i_msg)

# 卸载第三方库
# u_msg = PackageOperation.uninstall_package('pillow','my_env2')
# print(u_msg)
# 打印第三方包列表
# p_list = PackageOperation.get_plist('my_env2')
# print(p_list)

# 新建文件到venv目录下
# f_msg = FileOperation.create_file('my_env2','testadd1')
# print(f_msg)
# 删除文件
# d_msg = FileOperation.del_file('my_env2','testadd')
# print(d_msg)
# 重命名文件
# rn_msg = FileOperation.rn_file('my_env2','testadd1','renamefile')
# print(rn_msg)
