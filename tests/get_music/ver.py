import requests,re
def ver():
    url='https://pypi.org/project/get-music-lizhanqi/#history'
    html=requests.get(url)
    txt=html.text
    crad=re.findall(r' <a class="card release__card" href="/project/get-music-lizhanqi/(.*?)/">',txt,re.S)
    ver=crad[0]
    print('最新版本是:v'+ver+',你可以用"pip install --upgrade get-music-lizhanqi"命令进行更新')
