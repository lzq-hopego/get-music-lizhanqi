import requests,re,sys
from lxml import etree
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
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "zhidao.baidu.com",
            "Cookie":'BIDUPSID=247EF8962DC8C1C730FFFA55664D7C8A; PSTM=1627959722; __yjs_duid=1_101c882fe9a77545c7475b8defee40e91627959766009; ZFY=iWGPqno6tedMftpANOy1Cpb9d88MGOB8EiT6VDuJErE:C; BAIDUID=AE4EB64957A11585DE2B8734E4E9DE73:FG=1; BAIDUID_BFESS=AE4EB64957A11585DE2B8734E4E9DE73:FG=1; BDRCVFR[FIXrT5n2Tgt]=mk3SLVN4HKm; H_PS_PSSID=26350; BA_HECTOR=0425ag85al842l2h2g80573m1hhtv2o18; delPer=0; PSINO=2; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; session_id=16629750764287329664041787431; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1662720058,1662975077; shitong_key_id=2; ZD_ENTRY=empty; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1662975174; ab_sr=1.0.1_MzJiNzA3MzI5NDk5ZjIyM2NjNDViMzI0OTdiNGZjYWM5MGM2ODA5Y2UzY2E1MmIzNWU4MWU5YmI0ZGFkYTczOWIyNzg0OGYzZDE0NmMzZjBlMzk3YjdkMjg5OTgwZjVlYzljZGQ1M2RhOTkzMzE3ZjUwOWYwM2NlOGNlZmUyNjUxNjQzYmFjYjRlNDI2Y2RmNmNjMjJkMDZkOTI1NmJhNg==; shitong_data=5d7e69fe55d45e90c9169bfbb75f310a070886c471fc8cecf18562c01704ff6695f5dc217146d8a3684a1fad81645768d36cfe1f545913125bddc64b2b98de57517eaa97d478a362325778ba5ef8127f9246ecac5c2cb70fbb3ef3c0715f4931; shitong_sign=d434c564'
            }

    s=requests.session()

    html=s.get(url,headers=headers,timeout=5)
    html.encoding='gbk'
    txt=etree.HTML(html.text)
    div=txt.xpath('/html/body/div[2]/section/div/div/div/div[2]/div')[0]
    dl=[]
    for i in div:
        if i.tag=='dl':
            dl.append(i)
    pan_url=[]
    pwd=[]
    for i in dl:
        for j in range(1,3):
            s=''.join(i.xpath('./dd[{}]/text()'.format(j))).strip()
            if s=='':
                continue
            if 'pan.baidu.com' in s:
                pan_url.append(re.findall('http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', s)[0])
                if '提取码:' in s:
                    pwd.append(s.split('提取码:')[-1].strip()[:4])
                else:
                    pwd.append(s.split('提取码：')[-1].strip()[:4])
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

