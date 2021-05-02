<div align="center">
  <img src="https://github.com/SimonWDC/sandboxmanagement/blob/main/static/favicon.png" alt="">
  <h1>SandboxManagement</h1>
  <blockquote>High-performance, visualized local sandbox management system </blockquote>
  <a href="https://github.com/SimonWDC/sandboxmanagement/releases/tag/v0.9_beta">
    <img src="https://img.shields.io/github/v/release/SimonWDC/sandboxmanagement?style=flat-square" alt="">
  </a>
  <a href="https://github.com/SimonWDC/sandboxmanagement/archive/refs/heads/main.zip">
    <img src="https://img.shields.io/github/languages/code-size/SimonWDC/sandboxmanagement?color=red&style=flat-square">
  </a>
  <a href="https://github.com/SimonWDC/sandboxmanagement/archive/refs/heads/main.zip">
    <img src="https://img.shields.io/github/downloads/SimonWDC/sandboxmanagement/total?style=flat-square">
  </a>
  <a href="https://github.com/SimonWDC/sandboxmanagement">
    <img src="https://img.shields.io/github/last-commit/SimonWDC/sandboxmanagement?color=orange&style=flat-square">
  </a>
  <a href="https://github.com/SimonWDC/sandboxmanagement/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/SimonWDC/sandboxmanagement?color=li&style=flat-square">
  </a>
</div>

## Overview
SandboxManagement(SBM) is a **high-performance, visualized local sandbox management system**. 
Users only need to decompress the compressed package and automatically configure the environment through scripts to 
help python beginners lower the barriers to programming learning. 
The concise visual page helps python developers manage projects efficiently and avoid site-packages between projects 
with the help of virtualenv and virtualenvwrapper-win libraries. Version conflict.

## Download & Install

1. Download the program and interpreter through 👉[link](https://github.com/SimonWDC/sandboxmanagement/releases).
(Support python version 3.X, if you need to change a different version of the interpreter, 
   you need to name the interpreter folder `pyinterpreter`)

2. For the first installation, after decompressing `sbm.zip`, double-click `firstrun.bat` to install .
   dependencies and upgrade pip (please do not close the window during the installation process)
   
   ![firstrun](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2016-47-51.gif)
   
3. After the installation is successful, double-click `runflask.bat` to start.
   
   ![runflask](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2016-53-46.gif)

## Features

1. The main interface is to display the virtual environment, enter the virtual environment name in the input box, 
   and click the Add button to create a virtual environment.

   ![create](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2016-56-20.gif)
   
2. Display the virtual environment name, path and creation date, 
   click on the name to view the list of site-packages installed in the virtual environment.

   ![view](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2016-57-00.gif)

3. Move the mouse to the upper right corner of the card to display the remove button, 
   click to remove the virtual environment.

   ![remove](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2016-57-52.gif)

4. Display the list of third-party libraries, enter the name of the third-party library in the input box, 
   click Install to install site-packages through the pip package manager, 
   move the mouse to the upper right corner of the site-package card to click uninstall.

   ![install](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2016-57-00.gif)

   ![uninstall](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2016-57-29.gif)

5. Click the button above to open the Vscode editor for Python programming and running Python code.

   ![code](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/GIF%202021-5-2%2017-05-06.gif)
