import sbm_win
from flask import Flask, render_template, request, jsonify,redirect

app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False  # 防止jsonify自动按照字母排序


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        vname = request.form.get('name')
        c_msg = sbm_win.VenvOperation.create_venv(vname)
        print(c_msg)
        return redirect('/')
        # return vname
    else:
        vpath = sbm_win.VenvOperation.get_venv_path()
        venv_name = sbm_win.VenvOperation.get_venv_list()
        if venv_name == 'no venv':
            return render_template('index2.html',venv_name=venv_name,vpath=vpath)
        else:
            env_path = []
            for env_name in venv_name:
                sub_vpath = vpath + f'\\{env_name}'
                env_path.append(sub_vpath)
        return render_template(
            'index1.html',
            venv_name=venv_name,
            vpath=vpath,
            env_path=env_path)


@app.route('/remove_venv',methods=['GET','POST'])
def rm_venv():
    if request.method == 'POST':
        vname = request.values.get('vname')
        rm_msg = sbm_win.VenvOperation.rm_env(vname)
        return rm_msg
    else:
        pass

@app.route('/activate_venv',methods=['POST',])
def ac_venv():
    if request.method == 'POST':
        vname = request.values.get('vname')
        ac_msg = sbm_win.VenvOperation.activate_venv(vname)
        return ac_msg
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
