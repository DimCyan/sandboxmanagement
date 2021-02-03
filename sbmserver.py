import sbm_win
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__, template_folder='./templates')
# app.config['JSON_SORT_KEYS'] = False  # 防止jsonify自动按照字母排序


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        c_submit = request.form.get('create')
        if c_submit == '新增':
            vname = request.form.get('name')
            c_msg = sbm_win.VenvOperation.create_venv(vname)
            print(c_msg)
            return redirect('/')
        r_submit = request.form.get('remove')
        if r_submit == '删除':
            vname = request.form.get('name')
            rm_msg = sbm_win.VenvOperation.rm_env(vname)
            print(rm_msg)
            return redirect('/')
    else:
        vpath = sbm_win.VenvOperation.get_venv_path()
        venv_name = sbm_win.VenvOperation.get_venv_list()
        if venv_name == 'no venv':
            return render_template(
                'index2.html',
                venv_name=venv_name,
                vpath=vpath)
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


@app.route('/detail/<name>')
def get_venv_detail(name):
    print(name)
    # plist = sbm_win.PackageOperation.get_plist(name)



if __name__ == '__main__':
    app.run(debug=True)
