# PythonNVP

## Python Network verification program - Python 网络验证程序
有任何的Bug和想法请留言 我会在能力范围内解决 本程序的初衷是为了让作者发布的程序能更好的管理 

有任何问题可联系

Q 2583981930

Feel free to leave any bugs or ideas you have. I'll do my best to address them within my capabilities. The purpose of this program is to enhance the management of the author's released software.

For any inquiries, please contact:

ohczzz666@outlook.com

## Installation - 安装

您可以直接下载 `Releases`中打包好的 `backend.py` 也可以自行进行构建

You can directly download the packaged `backend.py` from the `Releases` section, or you can build them yourself.

### Self built - 自行构建
#### Requirements - 必要条件

`$ pip install -r requirements.txt`

or

```
# login.py requirements
base64==1.7.1
requests==2.26.0
psutil==5.8.0

# server.py requirements
Flask==2.0.2
openpyxl==3.0.9

# Backend.py requirements
openpyxl==3.0.9
```
#### Packaged - 打包
```
$ Pyinstaller -F login.py

$ Pyinstaller -F server.py

$ Pyinstaller -F backend.py
```
## Usage - 用法

### Login - 登录端

login.py
```python
login_url = #服务器IP地址 - Server IP Address
```
```
if response.status_code == 200:
#添加启动代码 - Add startup code
```
```
elif response.status_code == 402:
#添加启动代码 - Add startup code
```

### Server - 服务端

server.py 
```
app.run(host='IP', port= 端口 - port , debug=True)
```
```
xlsx_filename = "xlsx的文件名称 - The file name of xlsx"
```
### Background - 后台
backend.py 
```
columns = ["Key", "Machine Code", "Used", "Creation Time", "Generated By", "F/T"]
#key                秘钥-secret key
#Machine Code       电脑机器码-machine code
#Used               激活时间-activation time
#Creation Time      创建时间-creation time
#Generated By key   创建来源-sreate source
#F/T                key是否被激活-Is the key activated
```
```
xlsx_filename = "可更改xlsx的文件名称"
```
## 问题解决 [English](QAEnglish.md)

Q 我的登录无法连接到服务器怎么办？

A 请查看端口是否开放 公网ip服务端建议设置成0.0.0.0.

Q 这个程序安全性高吗？

A 如果您是为了安全性 来使用我的程序的话 建议您放弃使用我的程序 一个通过web验证 Excel文件的程序 不能说安如磐石吧 也只能说媲美马奇诺防线了 如果您的目标是针对于一些不会编程语言的用户的话 那么这个程序是不错的选择.

Q 我有没有办法提高安全性呢？

A 你可以尝试将xlsx 改为SQL 更改返回代码 或者对整个程序进行加密.

Q 我的Generated By key显示为{ture}是怎么回事？

A 那极有可能这个程序中可能存在的漏洞被你的用户发现了 他通过这种方式创建了一个Key 因为正常创建的Key只会显示 {backend} 如果出现 请将log文件发给我.
## Update log - 更新日志

0.2 2024.2.12 首次上传了PythonNVP
0.3 2024.2.19 为 `Server` 和 `backend` 加入了 `config` 方便打包后的配置
## 赞助

如果你愿意赞助我元子 我将感激涕零

<img src="https://s2.loli.net/2024/02/12/TwYR6UobfWLiy3u.png" alt="VX" width="186.25" height="253.5"><img src="https://s2.loli.net/2024/02/12/6KO3qmCwsIWo4ce.jpg" alt="ZFB" width="190.25" height="253.5">
