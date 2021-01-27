import sbm_win
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    vpath = sbm_win.VenvOperation.get_venv_path()
    return 'hello sbm\n',vpath

@app.route('/VenvList')
def get_venvlist():
    pass
    # venv_name = sbm_win.VenvOperation.get_venv_list()
    # venv_path = sbm_win.VenvOperation.get_venv_path()
    # return jsonify({'venv_name': venv_name,'venv_path':venv_path})

if __name__ == '__main__':
    app.run(debug=True)