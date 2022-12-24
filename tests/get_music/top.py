import requests,re
from rich.console import Console
from rich.table import Table
from get_music import kugou,netease,download
from get_music import qq as qqmusic
from get_music import kuwo
import sys


def qq():
    url='https://y.qq.com/n/ryqq/toplist/26'
    html=requests.get(url,timeout=1)
    html.encoding='utf-8'

    txt=html.text

    lt=re.findall(r'<a title="(.*?)" href="/n/ryqq/songDetail/(.*?)"',txt)

    name,music_id=zip(*lt)

    singer=re.findall(r'<a class="playlist__author" title="(.*?)"',txt)

    if((len(name)==len(music_id)==len(singer))==False):
        singer=[]
        div=re.findall(r'<div class="songlist__artist">(.*?)</div>',txt)
        for i in div:
            if '<!-- -->' in i:
                singer.append('和'.join(re.findall(r'<a class="playlist__author" title="(.*?)"',i)))
            else:
                singer.append(re.findall(r'<a class="playlist__author" title="(.*?)"',i)[0])
    return list(name),singer,list(music_id)

def kw():
    s=requests.session()
    head1={'Cookie': '_ga=GA1.2.1158784231.1649567141; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1649527110,1649567138,1649755011',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.7062 SLBChan/33',
           'Host': 'www.kuwo.cn',
           'Upgrade-Insecure-Requests': '1',
           'Connection': 'keep-alive'
           }
    head={'Accept': 'application/json, text/plain, */*',
      'Referer': 'http://www.kuwo.cn/rankList',
      'csrf': '4M57QR4C1S8',
      'Host': 'www.kuwo.cn',
          'Connection': 'keep-alive',
      'Cookie': '_ga=GA1.2.1158784231.1649567141; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1671888291; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1671888291; kw_token=4M57QR4C1S8; _gid=GA1.2.368264343.1671888291; _gat=1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
    s.get('http://www.kuwo.cn/rankList',headers=head1)
    html=s.get('http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=16&pn=1&rn=30&httpsStatus=1&reqId=c5f29300-8373-11ed-bc47-1dc98d5c838f',headers=head).json()

    songname=[]
    singer=[]
    songid=[]
    for i in html['data']['musicList']:
        songname.append(i['album'])
        singer.append(i['artist'])
        songid.append(i['rid'])
    return songname,singer,songid
    
def kg():
    url='https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62",
             "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"'
             }
    req=requests.get(url,headers=headers,timeout=1)
    song=re.findall(r"features.*\[(.*?)\]",req.text)[0]

    songname=re.findall(r'- (.*?)"',song)
    singer=re.findall(r'"author_name":"(.*?)"',song)
    hash_name=re.findall(r'"Hash":"(.*?)"',song)
    hash_id=re.findall(r'"album_id":(.*?),',song)
    for i in range(len(songname)):
        songname[i]=songname[i].encode('utf-8').decode('unicode_escape')
        singer[i]=singer[i].encode('utf-8').decode('unicode_escape')
    hash_list=list(zip(hash_name,hash_id))
    return songname,singer,hash_list

def wy():
    url='https://music.163.com/discover/toplist?id=3778678'
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
         'referer': 'https://music.163.com/',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
         }
    html=requests.get(url,headers=headers,timeout=1)
    html.encoding='utf-8'
    txt=html.text
    song_id=re.findall(',"id":(.*?),',txt)[::2]
    song=re.findall(',"name":"(.*?)"',txt)
    song = sorted(list(set(song)), key=song.index)
    songname=song[::2]
    singer=song[1::2]
    return songname,singer,song_id


def prints():
    console=Console()
    table = Table(style='purple',title='[b green]get-music-lizhanqi热歌榜单')
    table.add_column('[red]序号',justify='center')
    table.add_column('[yellow]歌曲名',justify='center',overflow=True)
    table.add_column('[blue]歌手',justify='center',overflow=True)
    table.add_column('[green]平台',justify='center',overflow=True)
    s=1
    api_num=0
    song=[]
    api=['QQ音乐','酷狗音乐','网易云音乐','酷我音乐']
    with console.status("[b green]飞速获取资料中..."):
        ls=[qq(),kg(),wy(),kw()]
        d={'QQ音乐':qqmusic.qq(),'酷狗音乐':kugou.kugou(),'网易云音乐':netease.netease(),'酷我音乐':kuwo.kuwo()}

    for i in ls:
        for j in range(6):
                table.add_row('[b red]'+str(s),'[yellow]'+i[0][j],'[blue]'+i[1][j],'[b green]'+api[api_num],end_section=True)
                s+=1
                song.append([i[0][j],i[1][j],i[2][j],api[api_num]])
        else:
            api_num+=1
    console.print(table)
    songs=console.input('[b green]请选择您要下载哪一首歌，直接输入[b red]序号[/]就行\n如需下载多个请用[b red]英文逗号[/]分割即可，[b blue]例如1,2[/]\n如果不需要下载多个，请直接输入序号就行(不想下载就直接回车)[b red]>[/]')
    songs=songs.split(',')
    for i in songs:
        try:
            i=int(i)
        except:
            console.print('[b red]\n\n\n——请输入数字！！！')
            continue
        if i=='':
            console.print('[b red]\n\n\n——您未做出选择！程序即将自动退出！！！')
            continue 
        elif i<1 or i>24:
            console.print('[b red]\n\n\n——输入的序号错误！！！')
            continue
        try:
            url=d[song[i-1][-1]].get_music_url(song[i-1][-2])
        except:
            console.print("[b red]无法解析下载链接！该歌曲可能收费或接口失效！如有疑问可联系3101978435@qq.com")
        name=song[i-1][0]+"-"+song[i-1][1]+".mp3"
        if url != None:
            download.download(url,name)
        else:
            console.print("[b red]无法解析下载链接！")
    
if __name__=='__main__':
    prints()
