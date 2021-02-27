@echo off
echo Pleae Wait and Don't close this window!!!!!
cd pyinterpreter
python -m pip install --upgrade pip
cd Scripts
pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install virtualenvwrapper-win -i https://pypi.tuna.tsinghua.edu.cn/simple