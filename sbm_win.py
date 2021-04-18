import os
import re
import time
import json


class SbmInit:
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
    def open_vscode():
        """打开编辑器及设置默认解释器路径"""
        interpreter_path = os.path.abspath('') + r'\pyinterpreter\python.exe'
        setting_path = os.path.abspath('') + r'\Code\data\user-data\User\settings.json'
        py_path = {'python.pythonPath': interpreter_path}
        with open(setting_path, "r+", encoding='utf-8') as jsonFile:
            json.dump(py_path, jsonFile)
        code_path = os.path.abspath('') + r'\Code'
        code_cmd_result = os.popen(f'cd {code_path} && Code.exe')
        return code_cmd_result


class VenvOperation:
    @staticmethod
    def set_vpath():
        """修改vnev文件路径"""
        base_path = os.path.abspath('') + r'\pyinterpreter\Scripts'
        os.environ['WORKON_HOME'] = fr'{base_path}'
        return base_path

    @staticmethod
    def create_venv(vname):
        """新建虚拟环境"""
        VenvOperation.set_vpath()
        scripts_path = SbmInit.get_scripts_path()
        msg = os.popen(f'cd /d {scripts_path} && mkvirtualenv {vname}').read()
        return msg

    @staticmethod
    def activate_venv(vname, cmd=None):
        """激活虚拟环境并进入"""
        VenvOperation.set_vpath()
        scripts_path = SbmInit.get_scripts_path()
        if cmd:
            msg = os.popen(
                rf'cd /d {scripts_path}\{vname}\Scripts && {cmd}').read()
        else:
            msg = os.popen(rf'cd /d {scripts_path}\{vname}\Scripts').read()
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
        scripts_path = SbmInit.get_scripts_path()
        msg = os.popen(f'cd /d {scripts_path} && rmvirtualenv {vname}').read()
        return msg

    @staticmethod
    def get_venv_path():
        """获取venv安装路径"""
        VenvOperation.set_vpath()
        scripts_path = SbmInit.get_scripts_path()
        sys_get_path = os.popen(f'cd /d {scripts_path} && lsvirtualenv').read()
        searchobj = re.findall(r'"(.*)"', sys_get_path)
        return searchobj[0]

    @staticmethod
    def get_venv_list():
        """获取所有虚拟环境名称"""
        VenvOperation.set_vpath()
        scripts_path = SbmInit.get_scripts_path()
        sys_get_name = os.popen(f'cd /d {scripts_path} && lsvirtualenv').read()
        first_str = "=============================================================================="
        head, sep, tail = sys_get_name.partition(first_str)
        clean_str = tail
        next_str = clean_str.split('\n')
        while '' in next_str:
            next_str.remove('')
        if not next_str:
            return 'no venv'
        else:
            return next_str

    @staticmethod
    def get_venv_mtime(vpath):
        """获取虚拟环境修改日期"""
        return time.strftime(
            "%Y-%m-%d %H:%M:%S",
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
        """获取虚拟环境内安装的第三方库列表，返回名称列表，版本列表"""
        cmd = 'pip list'
        contents = VenvOperation.activate_venv(vname, cmd)
        first_str = "---------- -------"
        head, sep, tail = contents.partition(first_str)
        clean_str = tail
        next_str = clean_str.split('\n')
        while '' in next_str:
            next_str.remove('')
        p_name_list = []
        p_version_list = []
        for i in next_str:
            head, sep, tail = i.partition(' ')
            p_name_list.append(head)
            p_version_list.append(tail.replace(" ", ""))
        return p_name_list, p_version_list

    @staticmethod
    def uninstall_package(pname, vname):
        """卸载第三方库"""
        cmd = f'pip uninstall {pname} --yes'
        msg = VenvOperation.activate_venv(vname, cmd)
        return msg


if __name__ == '__main__':
    SbmInit.open_vscode()
