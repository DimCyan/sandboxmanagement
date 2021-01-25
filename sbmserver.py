import sbm_win
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello sbm'

if __name__ == '__main__':
    app.run(debug=True)