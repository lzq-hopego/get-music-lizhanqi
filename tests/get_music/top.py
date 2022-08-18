import requests
import json
from lxml import etree
from rich.console import Console
from rich.table import Table
from get_music import kugou,netease,download
from get_music import qq as qqmusic
from get_music import kuwo
import sys
console=Console()

def qq():
    url='https://y.qq.com/n/ryqq/toplist/26'
    html=requests.get(url,timeout=1)
    html.encoding='utf-8'
    txt=etree.HTML(html.text)
    ul=txt.xpath('/html/body/div/div/div[2]/div[2]/div[3]/ul[2]')[0]
    li=ul.xpath('./li')

    songname=[]
    singer=[]
    for i in li[:6]:
        songname.append(i.xpath("./div/div[3]/span/a[2]/text()")[0])
        singer.append(i.xpath("./div/div[4]/a/text()")[0])
    return songname,singer

def kg():
    url='https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
    req=requests.get(url,timeout=1)
    html=etree.HTML(req.text)
    ul=html.xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/ul')[0]
    li=ul.xpath('./li')
    ls=[]
    for i in li:
        ls.append(i.attrib.get('title'))
    songname=[]
    singer=[]
    for i in ls[:6]:
        a,b=i.split(' - ')
        singer.append(a)
        songname.append(b)
    return songname,singer
    
def wy():
    url='https://music.163.com/discover/toplist?id=3778678'
    html=requests.get(url,timeout=1)
    html.encoding='utf-8'
    txt=etree.HTML(html.text)

    s=txt.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/textarea')[0].xpath('./text()')
    ls=list(s)
    d=json.loads(ls[0])
    songname=[]
    singer=[]
    for i in d[:6]:
        songname.append(i['name'])
        singer.append(i['artists'][0]['name'])
    return songname,singer
def kw():
    head={'Accept': 'application/json, text/plain, */*',
      'Referer': 'http://www.kuwo.cn/rankList',
      'csrf': 'VNMA3J2ABKA',
      'Cookie': 'reqid=61a94060X686eX4fe7Xbb9bX54cf26169318; gid=75fc1b5f-eb95-4729-b003-720c762f08b7; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660743549; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660743590; _ga=GA1.2.1866439872.1660743590; _gid=GA1.2.1454874071.1660743590; kw_token=VNMA3J2ABKA',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
    html=requests.get('http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=1&rn=30&httpsStatus=1&reqId=877c1ed0-1e32-11ed-b818-b31c6b0e7674',headers=head,timeout=1).json()

    songname=[]
    singer=[]
    songid=[]
    for i in html['data']['musicList'][:6]:
        songname.append(i['album'])
        singer.append(i['artist'])
        songid.append(i['rid'])
    return songname,singer,songid
songname=[]
singer=[]
with console.status("[b green]飞速获取资料中..."):
    a,b=qq()
    c,d=kg()
    e,f=wy()
    g,h,songid=kw()
songname.extend(a)
songname.extend(c)
songname.extend(e)
songname.extend(g)
singer.extend(b)
singer.extend(d)
singer.extend(f)
singer.extend(h)
del a,b,c,d,e,f,g,h
for i in range(6):
    singer.append('none')
table = Table(style='purple',title='[b green]get-music-lizhanqi热歌榜单')
table.add_column('[red]序号',justify='center')
table.add_column('[yellow]歌曲名',justify='center',overflow=True)
table.add_column('[blue]歌手',justify='center',overflow=True)
table.add_column('[green]平台',justify='center',overflow=True)
for i in range(len(songname)):
    if i<6:
        api='QQ音乐'
    elif i<12:
        api='酷狗音乐'
    elif i<18:
        api='网易云音乐'
    else:
        api='酷我音乐'
    table.add_row('[b red]'+str(i+1),'[yellow]'+songname[i],'[blue]'+singer[i],'[b green]'+api,end_section=True)
console.print(table)
songs=console.input('[b green]请选择您要下载哪一首歌，直接输入[b red]序号[/]就行\n如需下载多个请用[b red]英文逗号[/]分割即可，[b blue]例如1,2[/]\n如果不需要下载多个，请直接输入序号就行(不想下载就直接回车)[b red]>[/]')
if songs=='':
    console.print('[b red]\n\n\n——您未做出选择！程序即将自动退出！！！')
    sys.exit()
for i in songs.split(','):
    i=int(i)
    name=songname[i-1]+'-'+singer[i-1]+'.mp3'
    if i<=6:
        qq=qqmusic.qq()
        qq.search(songname[i-1])
        url=qq.get_music_url(qq.song_url[0])
        if url==None or url=='':
            console.print('[b red]下载链接为空，可能是无法解析下载链接或接口失效')
        else:
            download.download(url,name)
    elif i<=12:
        kugou=kugou.kugou()
        kugou.search(songname[i-1])
        url=kugou.get_music_url(kugou.songs_url[0])
        if url==None or url=='':
            console.print('[b red]下载链接为空，可能是无法解析下载链接或接口失效')
        else:
            download.download(url,name)
    elif i<=18:
        netease=netease.netease()
        netease.search(songname[i-1])
        url=netease.song_id[0]
        if url==None or url=='':
            console.print('[b red]下载链接为空，可能是无法解析下载链接或接口失效')
        else:
            download.download(url,name)
    else:
        kuwo=kuwo.kuwo()
        url=kuwo.get_music_url(songid[i-18-1])
        if url==None or url=='':
            console.print('[b red]下载链接为空，可能是无法解析下载链接或接口失效')
        else:
            download.download(url,name)
