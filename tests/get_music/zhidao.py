import requests,re,sys
from rich import console
import urllib.parse
from rich.table import Table
console=console.Console()

    
def search():
    console.print('[b red]此命令用于在网络中查找网友分享的有关您需要下载的歌曲网盘链接!\n\n')
    songname=console.input('[b green]请输入您想下载的歌曲:')
    url='https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=utf-8&dyTabStr=MCw0LDUsMSw2LDMsNyw4LDIsOQ%3D%3D&word={} 歌曲 百度网盘'.format(songname)
    headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            "Referer":'https://zhidao.baidu.com',
            "Host": "zhidao.baidu.com"
            }

    s=requests.session()

    html=s.get(url,headers=headers,timeout=5)
    html.encoding='utf-8'

    div=re.findall(r'<dd class="dd answer">(.*?)<\/dd>',html.text)

    pan_url=[]
    pwd=[]
    for i in div:
        if 'pan.baidu.com' in i:
            if '提取码:' in i:
                pwd.append(i.split('提取码:')[-1].strip()[:4])
            elif '提取码：'in i:
                pwd.append(i.split('提取码：')[-1].strip()[:4])
            else:
                break
            pan_url.append(re.findall('http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',i)[0])

            
    if len(pan_url)==0:
        console.print('[b red] \n很抱歉，我们通过其他渠道仍然无法检索到[b green]{}[/]'.format(songname))
        sys.exit()
    table = Table(style='purple',title='[b green]百度网盘资源')
    table.add_column('[red]链接',justify='center',overflow=True)
    table.add_column('[yellow]提取码',justify='center',overflow=True)
    table.add_column('[blue]轻松链',justify='center',overflow=True)

    for i in range(len(pan_url)):
        table.add_row('[b red]'+pan_url[i],'[yellow]'+pwd[i],'[blue]'+pan_url[i]+'?pwd='+pwd[i],end_section=True)
    console.print('[b red]本程序不转存，链接为网友分享，轻松链可不需要输入密码直接打开，有时不稳定。')
    console.print('[b red]我们为您找到了如下表中的链接中的数据和您输入的[b green]{}[/]相符,您可复制后在百度网盘（浏览器）下载'.format(songname))
    console.print(table)

