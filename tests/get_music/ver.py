import requests,re
def ver():
    version='0.0.64'
    print("当前版本:"+"v"+version)
    url='https://pypi.org/project/get-music-lizhanqi/#history'
    try:
        html=requests.get(url,timeout=1)
        txt=html.text
        crad=re.findall(r' <a class="card release__card" href="/project/get-music-lizhanqi/(.*?)/">',txt,re.S)
        ver=crad[0]
        v1=int(version.split('.')[-1])
        v2=int(ver.split('.')[-1])
        if v2 > v1:
            print('最新版本是:v'+ver+',你可以用"pip install --upgrade get-music-lizhanqi"命令进行更新')
        elif v2 ==v1:
            print('最新版本是:v'+ver+',您已是最新版本')
        else:
            print("测试用户")
    except:
        print("获取最新版本信息失败！请检查是否是网络的问题！")
