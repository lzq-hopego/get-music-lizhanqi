import requests
from get_music import download
from rich.console import Console
# import download
console=Console()



class migu:
    def __init__(self,p=False,l=False):
        self.head={
            'referer':'http://m.music.migu.cn',
            'proxy':'false',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }
        self.l=l
        self.p=p
        self.api='咪咕音乐'
    def search(self,sname,page=1):
        self.song_name = sname
        self.page=page
        url='http://m.music.migu.cn/migu/remoting/scr_search_tag?keyword={}&type={}&pgc={}&rows={}'.format(self.song_name,2,int(self.page),10)
        req=requests.get(url,headers=self.head,timeout=1).json()
        self.songname=[]
        self.singername=[]
        self.songs_url=[]
        self.id=[]
        self.pic=[]
        pic=[]
        for i in req['musics']:
            self.songname.append(i['songName'])
            self.singername.append(i['artist'])
            self.songs_url.append(i['mp3'])
            self.id.append(i['copyrightId'])
            self.pic.append(i['cover'])
        return self.songname,self.singername,self.songs_url
##    def prints(self):
##        pass
    def get_music_url(self,url):
        return url
    def get_music_lrc(self,num,return_url=False):
        try:
            headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
             'accept' :"application/json, text/plain, */*",
             'referer':'http://music.migu.cn/v3/music/player/audio',
             }
            url='https://music.migu.cn/v3/api/music/audioPlayer/getLyric?copyrightId='+str(self.id[num])
            html=requests.get(url,headers=headers).json()['lyric']
            if return_url:
                return html
            name=self.songname[num]+"-"+self.singername[num]+'-'+"歌词.txt"
            with open(name,'w') as f:
                f.write(html)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
        
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
##a=migu(l=True,p=True)
##a.search('周杰伦')
##a.prints()
