import requests
from lxml import etree
from rich.console import Console
from rich.table import Table
from get_music import kugou,netease,download
from get_music import qq as qqmusic
import sys
console=Console()

def qq():
    url='https://y.qq.com/n/ryqq/toplist/26'
    html=requests.get(url)
    html.encoding='utf-8'
    txt=etree.HTML(html.text)
    ul=txt.xpath('/html/body/div/div/div[2]/div[2]/div[3]/ul[2]')[0]
    li=ul.xpath('./li')

    songname=[]
    for i in li[0::2]:
        a=i.xpath('./div/div[3]/span/a[2]')[0]
        songname.append(a.attrib.get('title'))
    singer=[]
    for i in li[1::2]:
        a=i.xpath('./div/div[3]/span/a[2]')[0]
        singer.append(a.attrib.get('title'))
    return songname,singer

def kg():
    url='https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
    req=requests.get(url)
    html=etree.HTML(req.text)
    ul=html.xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/ul')[0]
    li=ul.xpath('./li')
    ls=[]
    for i in li:
        ls.append(i.attrib.get('title'))
    songname=[]
    singer=[]
    for i in ls:
        a,b=i.split(' - ')
        singer.append(a)
        songname.append(b)
    return songname,singer
    
def wy():
    url='https://music.163.com/discover/toplist?id=3778678'
    html=requests.get(url)
    html.encoding='utf-8'
    txt=etree.HTML(html.text)
    ul=txt.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/ul')[0]
    li=ul.xpath('./li')
    songname=[]
    for i in li[:22]:
        songname.append(i.xpath('./a/text()')[0])
    return songname
songname=[]
singer=[]
with console.status("[b green]飞速获取资料中..."):
    a,b=qq()
    c,d=kg()
    e=wy()
songname.extend(a[:6])
songname.extend(c[:6])
songname.extend(e[:6])
singer.extend(b[:6])
singer.extend(d[:6])
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
    else:
        api='网易云音乐'
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
        if url==None:
            console.print('[b red]该歌曲无法下载!')
        else:
            download.download(url,name)
    elif i<=12:
        kugou=kugou.kugou()
        kugou.search(songname[i-1])
        url=kugou.get_music_url(kugou.songs_url[0])
        if url==None:
            console.print('[b red]该歌曲无法下载!')
        else:
            download.download(url,name)
    else:
        netease=netease.netease()
        netease.search(songname[i-1])
        url=netease.song_id[0]
        if url==None:
            console.print('[b red]该歌曲无法下载!')
        else:
            download.download(url,name)
