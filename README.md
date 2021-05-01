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

---
## Overview
SandboxManagement(SBM) is a **high-performance, visualized local sandbox management system**. 
Users only need to decompress the compressed package and automatically configure the environment through scripts to 
help python beginners lower the barriers to programming learning. 
The concise visual page helps python developers manage projects efficiently and avoid site-packages between projects 
with the help of virtualenv and virtualenvwrapper-win libraries. Version conflict.

## Install

Download the program and interpreter through 👉🖱[link](https://github.com/SimonWDC/sandboxmanagement/releases/tag/v0.1)
(Support python version 3.X, if you need to change a different version of the interpreter, you need to name the interpreter folder `pyinterpreter`)

## 使用

1. 第一次安装，解压`sandboxmanagement.zip`后，双击`firstrun.bat`安装依赖和升级pip（安装过程中请不要关闭窗口）

   ![](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/Snipaste_2021-02-16_21-45-11.png)

   ![](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/Snipaste_2021-02-16_21-45-46.png)

2. 安装成功后，双击`runflask.bat`启动

   ![](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/Snipaste_2021-02-16_21-46-14.png)

3. 主界面为显示虚拟环境，在输入框中输入虚拟环境名称，点击新增按钮新增虚拟环境

   ![](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/Snipaste_2021-02-16_21-48-13.png)

   显示虚拟环境名称、路径和创建日期，点击名称可查看虚拟环境pip安装的第三方库列表

   ![](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/Snipaste_2021-02-16_21-49-17.png)

4. 鼠标移动到卡片右上角显示删除按钮，点击删除虚拟环境

   ![](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/Snipaste_2021-02-16_21-49-39.png)

5. 显示第三方库列表，在输入框中输入第三方库名称，点击安装可通过pip安装第三方库，鼠标移动到第三方库卡片右上角可点击卸载第三方库

   ![](https://github.com/SimonWDC/sandboxmanagement/blob/main/img/Snipaste_2021-02-16_21-51-13.png)
