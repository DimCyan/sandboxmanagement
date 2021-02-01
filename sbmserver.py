import sbm_win
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # 防止jsonify自动按照字母排序


@app.route('/')
def index():
    vpath = sbm_win.VenvOperation.get_venv_path()
    venv_name = sbm_win.VenvOperation.get_venv_list()
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


if __name__ == '__main__':
    app.run(debug=True)
