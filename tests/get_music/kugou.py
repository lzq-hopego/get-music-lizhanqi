import requests,json,sys,re
from get_music import download
from rich.console import Console
# import download
console=Console()
class kugou:
    def __init__(self,p=False,l=False):
        self.l=l
        self.p=p
        self.api='酷狗音乐'
    def search(self,songname,page=1):
        self.page=page
        self.song_name=songname
        headers={
        'UserAgent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
        'Referer' : 'http://m.kugou.com/rank/info/8888',
        'Cookie' : 'UM_distinctid=161d629254c6fd-0b48b34076df63-6b1b1279-1fa400-161d629255b64c; kg_mid=cb9402e79b3c2b7d4fc13cbc85423190; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1523818922; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1523819865; Hm_lvt_c0eb0e71efad9184bda4158ff5385e91=1523819798; Hm_lpvt_c0eb0e71efad9184bda4158ff5385e91=1523820047; musicwo17=kugou'
        }
        self.url="http://mobilecdngz.kugou.com/api/v3/search/song?tag=10&page="+str(self.page)+"&tagtype=%E5%85%A8%E9%83%A8&area_code=1&plat=2&sver=5&api_ver=1&showtype=10&version=8969&keyword="+self.song_name
        req=requests.get(self.url,headers=headers,timeout=1)
        d=json.loads(req.text)
        songs_list=d['data']['info']
        self.songs_url=[]
        self.songname=[]
        self.singername=[]
        for i in songs_list:
            l=[]
            self.songname.append(i['songname'])
            self.singername.append(i['singername'])
            l.append(i["hash"])
            l.append(i["album_id"])
            self.songs_url.append(l)
        return self.songname,self.singername,self.songs_url
##    def prints(self):
##        pass
    def get_music_url(self,ls):
        headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62",
             "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"'
             ,'cookie': 'kg_mid=6f1f6d9d081fde37857f5df3963daa26; kg_dfid=2mSWBz38IvHG3mhgPf44QaF4; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1670383226,1670384489; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1670397821'
                 }
        try:
            url='http://m.kugou.com/app/i/getSongInfo.php?cmd=playInfo&hash={}'.format(ls[0])
            d=requests.get(url,headers=headers).json()
            self.d=d
            return d['backup_url'][0]
        except:
            url="https://www.kugou.com/yy/index.php?r=play/getdata&hash={}&album_id={}" .format(ls[0],ls[1])
            d=requests.get(url,headers=headers,timeout=1).json()
            self.d=d
            if d["data"]["play_url"]=='':
                return '未能成功获取音乐下载地址'
                sys.exit()
            else:
                return d["data"]["play_url"]
    def get_music_lrc(self,num,return_url=False):
        try:
            url='http://m.kugou.com/app/i/krc.php?cmd=100&timelength=999999&hash='+self.songs_url[num][0]
            name=self.songname[num]+'-'+self.singername[num]+'-'+'歌词.txt'
            html=requests.get(url)
            html.encoding='utf-8'
            txt=html.text
            if return_url:
                return txt
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w',encoding='utf-8') as f:
                f.write(txt)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            try:
                text=self.d['data']['lyrics']
                name=self.songname[num]+'-'+self.singername[num]+'-'+'歌词.txt'
                if return_url:
                    return text
                with open(name,'w',encoding='utf-8') as f:
                    f.write(text)
                console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
            except:
                console.print("[b red]未找到该歌曲的歌词！")
        
            
    def get_music_pic(self,num,return_url=False):
        try:
            img=self.d['album_img'].replace('{size}','150')
            name=self.songname[num]+'-'+self.singername[num]+'-'+'封面.jpg'
            if return_url:
                return img
            download.download(img,name)
            console.print("[b green]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            try:
                img=self.d['data']['img']
                if return_url:
                    return img
                name=self.songname[num]+'-'+self.singername[num]+'-'+'封面.jpg'
                download.download(img,name)
                console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
            except:
                console.print("[b red]未找到该歌曲的封面！")
##测试代码
##a=kugou(l=True,p=True)
##a.search('love story')
##a.prints()
##input()
