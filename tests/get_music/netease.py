import requests,json
from get_music import download
from rich.console import Console
# import download
console=Console()

class netease:
    def __init__(self,p=False,l=False):
        self.url='http://music.163.com/api/cloudsearch/pc'
        self.headers={'referer':'http://music.163.com/',
        'proxy':"false",
        'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
        self.data={'s':'',
        'type':1,
        'offset':1,
        'limit':20}
        self.l=l
        self.p=p
        self.api='网易云音乐'
    def search(self,songname,page=0):
        self.data['offset']=self.page=page
        self.data['s']=self.song_name=songname
        req=requests.post(self.url,headers=self.headers,data=self.data,timeout=1)
        d=json.loads(req.text)
        song_url=['http://music.163.com/song/media/outer/url?id=','.mp3']
        songs=d["result"]['songs']
        self.songname=[]
        self.songs_url=[]
        self.singername=[]

        self.id=[]
        self.pic=[]
        for i in songs:
                self.songs_url.append(str(i['id']).join(song_url))
                self.songname.append(i["name"])
                self.singername.append(i['ar'][0]["name"])
                self.id.append(i['id'])
                self.pic.append(i['al']['picUrl'])
        return self.songname,self.singername,self.songs_url
    def get_music_url(self,url):
        if 'http:' not in url:
            return 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(url)
        return url
    def get_music_lrc(self,num,return_url=False):
        headers = {
                "user-agent" : "Mozilla/5.0",
                "Referer" : "http://music.163.com",
                "Host" : "music.163.com"
            }
        try:
            song_id=self.id[num]
            if not isinstance(song_id, str):
                song_id = str(song_id)
            url = f"http://music.163.com/api/song/lyric?id={song_id}+&lv=1&tv=-1"
            r = requests.get(url, headers=headers,timeout=1)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            json_obj = json.loads(r.text)
            if return_url:
                return json_obj["lrc"]["lyric"]
            name=self.songname[num]+"-"+self.songername[num]+'-'+"歌词.txt"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w') as f:
                f.write(json_obj["lrc"]["lyric"])
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            if type(num)==str:
                url = f"http://music.163.com/api/song/lyric?id={num}+&lv=1&tv=-1"
                r = requests.get(url, headers=headers,timeout=1)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                json_obj = json.loads(r.text)
                return json_obj["lrc"]["lyric"]

            else:
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
##a=netease(l=True,p=True)
##d=a.search("11")
##a.prints()
##input()
