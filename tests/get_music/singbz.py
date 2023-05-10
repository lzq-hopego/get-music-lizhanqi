import requests,re,json
import urllib.parse
from rich.console import Console
console=Console()

class singbz:
    def __init__(self,p=False,l=False):
        self.api='5Sing伴奏'
        self.l=l
        self.p=p
        
    def search(self,songname,page=1):
        self.song_name=songname
        self.page=page
        songname=urllib.parse.quote(songname)
        headers={'referer': 'http://search.5sing.kugou.com/?keyword=',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
                 "Accept" : "application/json, text/javascript, */*; q=0.01"}
        headers['referer']=headers.get('referer')+songname
        url='http://search.5sing.kugou.com/home/json?keyword={}&sort=1&page={}&filter=3&type=0'.format(songname,page)
        req=requests.get(url,headers=headers,timeout=3)
        d=req.json()
        self.songs_url=[]
        self.songname=[]
        self.singername=[]
        for i in d['list']:
                    self.songs_url.append(i['songId'])
                    self.singername.append(i['originSinger']+'-'+i['nickName'])
                    self.songname.append(i['songName'].replace('<em class="keyword">','').replace('</em>',''))

        return self.songname,self.singername,self.songs_url
    
    def get_music_url(self,songid):
        
        jx='http://service.5sing.kugou.com/song/getsongurl?songid={}&songtype=bz&from=web&version=6.6.72&_=1673862766682'.format(songid)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
                          }

        req=requests.get(jx,headers=headers,timeout=1)
        txt=json.loads(req.text[1:-1])
        if txt['message'] != '成功':
            console.print('[b red]无法解析，或出现故障，故障代码:'+txt['code'])

        song_squrl=txt['data']['squrl']
        if song_squrl=='':
            song_squrl=txt['data']['squrl_backup']
            
        song_lqurl=txt['data']['lqurl']
        if song_lqurl=='':
            song_lqurl=txt['data']['lqurl_backup']
        downloadurl=song_squrl
        if downloadurl=='':
            downloadurl=song_lqurl
        return downloadurl
    def get_music_lrc(self,num,return_url=False):
        console.print('[b red]本接口不支持歌词！')
    def get_music_pic(self,num,return_url=False):
        console.print('[b red]本接口不支持封面！')
