import requests,re
from rich.console import Console
def ver(ip=True):
    console=Console()
    version = '1.0.6'
    console.print("[green]当前版本:"+"v"+version)
    url = 'https://pypi.org/project/get-music-lizhanqi/#history'
    try:
        with console.status("[b green]检查最新版中..."):
            html = requests.get(url,timeout = 1)
            txt = html.text
            crad = re.findall(r' <a class="card release__card" href="/project/get-music-lizhanqi/(.*?)/">',txt,re.S)
            ver = crad[0]
            ver1 = version.split('.')
            ver2 = ver.split('.')
            ls= []
            for i in range(3):
                v1 = ver1[i]
                v2 = ver2[i]
                if v2 > v1:
                    ls.append(False)
                elif v2 == v1:
                    ls.append(True)
                else:
                    ls.append(False)
        if False in ls:
            console.print('[b red]最新版本是:v'+ver+',你可以用"pip install --upgrade get-music-lizhanqi"命令进行更新')
        else:
           console.print('[b red]最新版本是:v'+ver+',您已是最新版本')
        if ip==True:
            try:
                url = 'http://api.ip33.com/ip/search?s='                     
                d = requests.get(url,timeout=1).json()                                                       
                console.print('\n[b green]本机外网ip地址为:[b red]{}[/]，归属:[b red]{}[/]'.format(d['ip'],d['area']))
            except:
                pass
    except:
        console.print("[b red]获取最新版本信息失败！请检查是否是网络的问题！")


