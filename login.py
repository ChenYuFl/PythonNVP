import base64
import requests
import psutil

def get_machine_code():
    machine_code = str(psutil.cpu_freq().current) + str(psutil.virtual_memory().total)
    encoded_machine_code = machine_code.encode("utf-8")
    encoded_machine_code_base64 = base64.b64encode(encoded_machine_code).decode("utf-8")
    return encoded_machine_code_base64
def login(api_key):
    machine_code = get_machine_code()
    if machine_code is None:
        print("无法获取机器码，登录失败")
        return
    #将login_url改为自己的IP 例 IP为0.0.0.0 端口 5000 就输入 http://0.0.0.0:50000/login
    login_url = "http://127.0.0.1:50000/login"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"machine_code": machine_code}

    response = requests.post(login_url, headers=headers, data=data)

    if response.status_code == 200:
        print("登录成功")
        #在这里添加启动命令
    elif response.status_code == 402:
        print("首次使用密钥，不进行机器码验证，直接记录首次激活时间")
        #在这里添加启动命令
    elif response.status_code == 401 and "Invalid machine code" in response.json().get("message", ""):
        print("机器码验证失败")
    else:
        print(f"登录失败，服务器响应: {response.text}")

def run_interface():
    print("成功登录后执行的操作")

if __name__ == "__main__":
    api_key = input("请输入 API Key: ")
    login(api_key)
