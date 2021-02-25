import sbm_win
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__,template_folder='./templates',static_folder='./static')
# app.config['JSON_SORT_KEYS'] = False  # 防止jsonify自动按照字母排序


@app.route('/', methods=['GET', 'POST'])
def index():
    # sbm_win.SbmInit.upgrade_pip()
    if request.method == 'POST':
        c_submit = request.form.get('create')
        if c_submit == '➕':
            vname = request.form.get('name')
            c_msg = sbm_win.VenvOperation.create_venv(vname)
            print(c_msg)
            return redirect('/')
    else:
        vpath = sbm_win.VenvOperation.get_venv_path()
        venv_name = sbm_win.VenvOperation.get_venv_list()
        if venv_name == 'no venv':
            return render_template(
                'index.html',
                venv_name=venv_name,
                vpath=vpath)
        else:
            env_path = []
            for env_name in venv_name:
                sub_vpath = vpath + f'\\{env_name}'
                env_path.append(sub_vpath)
            env_mtime = []
            for path in env_path:
                path_mtime = sbm_win.VenvOperation.get_venv_mtime(path)
                env_mtime.append(path_mtime)
            venv_info = []
            for i in range(len(venv_name)):
                info = {
                    'vname': venv_name[i],
                    'vpath': env_path[i],
                    'mtime': env_mtime[i]}
                venv_info.append(info)
            print(venv_info)
        return render_template(
            'index.html',
            venv_info=venv_info,
            vpath=vpath,
        )


@app.route('/delete/<name>')
def rm_venv(name):
    rm_msg = sbm_win.VenvOperation.rm_env(name)
    print(rm_msg)
    return redirect('/')


@app.route('/detail/<name>', methods=['GET', 'POST'])
def get_venv_detail(name=None):
    if request.method == 'POST':
        c_submit = request.form.get('install')
        if c_submit == '📌':
            pname = request.form.get('name')
            i_msg = sbm_win.PackageOperation.install_package(pname, name)
            print(i_msg)
            return redirect(url_for('get_venv_detail', name=name))
    else:
        p_name_list = sbm_win.PackageOperation.get_plist(name)[0]
        p_version_list = sbm_win.PackageOperation.get_plist(name)[1]
        p_info = []
        for i in range(len(p_name_list)):
            info = {
                'p_name': p_name_list[i],
                'p_version': p_version_list[i]}
            p_info.append(info)
        print(p_info)
        return render_template('detail.html', vname=name, p_info=p_info)


@app.route('/uninstall/<vname>/<name>')
def uninstall_package(vname, name):
    pname = name.split('-')[0]
    un_msg = sbm_win.PackageOperation.uninstall_package(pname, vname)
    print(un_msg)
    return redirect(url_for('get_venv_detail', name=vname))


if __name__ == '__main__':
    app.run(debug=True)
