

import requests
import re
import time
import hashlib

from rich.console import Console
# import download
console=Console()

class baidu:
    def __init__(self,p=False,l=False):
        self.headers = {
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
        self.l=l
        self.p=p
        self.api='千千静听'
    def search(self,songname,page=1):
        self.song_name=songname
        self.page=page
        params = (
        ('word', self.song_name),
        )
##        response = requests.get('https://music.taihe.com/search', headers=self.headers,params=params,timeout=1)
        url_fenye = 'https://music.taihe.com/search?word={}&pageNo={}'.format(self.song_name,str(self.page))
        response = requests.get(url=url_fenye, headers=self.headers,timeout=1)
        text=response.text
        self.songs_url = re.findall(r'<a href="/song/(.*?)"', text, re.S)
        self.singername=re.findall(r'<a href="/artist/.*?".*?>(.*?)</a>', text, re.S)
        self.songname=re.findall(r'<a href="/song/.*?".*?>(.*?)</a>', text, re.S)
        return self.songname,self.singername,self.songs_url

##    def prints(self):
##        pass

    def get_music_url(self,songid):
        r = f"TSID={songid}&appid=16073360&timestamp={str(int(time.time()))}0b50b02fd0d73a9c4c8c3a781c30845f"
        sign = hashlib.md5(r.encode(encoding='UTF-8')).hexdigest()
        # print(sign) # 获取到的就是每一首歌曲的sign值，下面构造params
        params = (
        ('sign', sign),
        ('appid', '16073360'),
        ('TSID', songid),
        ('timestamp', str(int(time.time()))),
        )
        # 具体歌曲的相关属性
        song_info = requests.get('https://music.taihe.com/v1/song/tracklink',params=params, timeout=1).json()[
         'data']
        self.lrc=song_info['lyric']
        self.pic=song_info['pic']
        return song_info['path']  # 音频地址
    def get_music_lrc(self,num,return_url=False):
        try:
            name=self.songname[num]+"-"+self.singername[num]+'-'+"歌词.lrc"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            if return_url:
                return self.lrc
            download.download(self.lrc,name)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
    def get_music_pic(self,num,return_url=False):
        try:
            name=self.songname[num]+"-"+self.singername[num]+'-'+"封面.jpg"
            if return_url:
                return self.pic
            download.download(self.pic,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")

##测试代码
##a=baidu(p=True)
##a.search('11')
##a.prints()
