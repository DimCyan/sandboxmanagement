import os


"""获取解释器-解释器所在文件夹位置与此文件在同一目录下，并命名为《pyinterpreter》"""


def get_interpreter():
    interpreter_path = os.path.abspath('') + '/pyinterpreter/python.exe'
    return interpreter_path


"""升级pip版本"""


def update_pip(interpreter_path):
    msg = os.popen(f'{interpreter_path} -m pip install --upgrade pip')
    return msg


"""更改环境变量"""


def set_env(interpreter_path):
    os.system(f'set Path={interpreter_path};%Path%')
    env_path = os.popen('set Path')
    return env_path


if __name__ == '__main__':
    interpreter_path = get_interpreter()
    # update_pip(interpreter_path)
    # set_env(interpreter_path)
