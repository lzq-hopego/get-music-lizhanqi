import requests
from get_music import download
from rich.console import Console
# import download
console=Console()
class oneting:
    def __init__(self,p=False,l=False):
        self.headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
                   'referer':'https://h5.1ting.com/'}
        self.l = l
        self.p = p
        self.api='一听音乐'
    def search(self,songname,page=1):
        self.song_name = songname
        self.page = page
        url = 'https://so.1ting.com/song/json?q={}&page={}&size=20'.format(self.song_name,self.page)
        req = requests.get(url,headers=self.headers,timeout=1)
        d=req.json()
        self.songname=[]
        self.singername=[]
        self.songs_url=[]
        self.pic=[]

        songurl='https://h5.1ting.com/file?url='
        for i in d['results']:
            self.songname.append(i['song_name'])
            self.pic.append("https:"+i['album_cover'])
            self.singername.append(i['singer_name'])
            self.songs_url.append(songurl+i['song_filepath'].replace('.wma','.mp3'))
        return self.songname,self.singername,self.songs_url
    def prints(self):
        pass
    def get_music_url(self,url):
        return url
    def get_music_lrc(self,num,return_url=False):
        if return_url:
                return "找不到歌词"
        console.print("[b green]该接口不支持下载歌词谢谢！搜索继续进行中...")
    def get_music_pic(self,num,return_url=False):
        try:
            url=self.pic[num]
            if return_url:
                return url
            name=self.songname[num]+"-"+self.singername[num]+'-'+"封面.jpg"
            download.download(url,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
##测试代码
##a=oneting(l=True,p=True)
##a.search("11")
##a.prints()

