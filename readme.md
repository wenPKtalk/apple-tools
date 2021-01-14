# 安装python虚拟环境
```
pip3 install virtualenv
```
1. 创建一个虚拟环境

```
virtualenv venv
```
[如何和vscode或者pycharm关联](https://segmentfault.com/a/1190000017955152)

2. 安装python3依赖
```
pip3 install -r requirements.txt
```
## word转txt
将word放到word目录下，执行
```
python3 word2txt.py --path "word的绝对路径"
```