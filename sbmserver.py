import sbm_win
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # 防止jsonify自动按照字母排序


@app.route('/')
@app.route('/index')
def index():
    vpath = sbm_win.VenvOperation.get_venv_path()
    venv_name = sbm_win.VenvOperation.get_venv_list()
    if venv_name == 'no venv':# 无虚拟环境
        return render_template('index2.html',venv_name=venv_name,
        vpath=vpath)
    else:# 有虚拟环境
        env_path = []
        for env_name in venv_name:
            sub_vpath = vpath + f'\\{env_name}'
            env_path.append(sub_vpath)
        # return jsonify({'vpath': vpath, 'venv_name':
        # venv_name,'env_path':env_path})
        return render_template(
            'index1.html',
            venv_name=venv_name,
            vpath=vpath,
            env_path=env_path)

@app.route('/create_venv')
def c_venv(vname):
    c_msg = sbm_win.VenvOperation.create_venv(vname)
    return c_msg

@app.route('/remove_venv')
def rm_venv(vname):
    rm_msg = sbm_win.VenvOperation.rm_env(vname)
    return rm_msg

@app.route('/activate_venv')
def ac_venv(vname,cmd):
    ac_msg = sbm_win.VenvOperation.activate_venv(vname,cmd)
    return ac_msg


if __name__ == '__main__':
    app.run(debug=True)
