import requests,re
from get_music import download
from rich.console import Console
# import download
console=Console()

class fivesing:
    def __init__(self,songtype,p=False,l=False):
        self.songtype=songtype
        self.headers={'referer': 'http://search.5sing.kugou.com/?keyword='+str("11"),
         "Accept" : "application/json, text/javascript, */*; q=0.01"}
        self.l=l
        self.p=p
        if songtype=='yc':
            self.api='51原唱'
        else:
            self.api='51翻唱'
    def search(self,songname,page=1):
        self.page=page
        self.song_name=songname
        
        if self.songtype=='yc':
            typename='1'
        else:
            typename='2'
        self.headers['referer']=self.headers.get('referer')+self.song_name
        url='http://search.5sing.kugou.com/home/json?keyword={}&sort=1&filter={}&page={}'.format(self.song_name,typename,self.page)
        req=requests.get(url,headers=self.headers,timeout=1)
        d=req.json()
        self.songs_url=[]
        self.songname=[]
        self.singername=[]
        for i in d['list']:
            self.songs_url.append(i['songId'])
            self.singername.append(i['nickName'])
            self.songname.append(re.findall('<em class="keyword">(.*?)</em>',i['songName'])[0])
        return self.songname,self.singername,self.songs_url
    def prints(self):
        name=self.songname
        singer=self.singername
        song_url=self.songs_url
        

    def get_music_url(self,songid):
        url2='http://service.5sing.kugou.com/song/getsongurl?songid={}&songtype={}'.format(songid,self.songtype)
        headers=self.headers
        headers['referer']='http://5sing.kugou.com/'+'/'+self.songtype+str(songid)
        req=requests.get(url2,headers=headers)
        d=req.json()
        self.pic=d['data']['user']['I']
        return d['data']['lqurl']
    def get_music_lrc(self,num,return_url=False):
        try:
            url='http://5sing.kugou.com/fm/m/json/lrc?songId={}&songType={}'.format(self.song_id[num],self.songtype)
            req=requests.get(url,timeout=1)
            txt=req.json()['txt']
            if return_url:
                return txt
            name=self.songname[num]+"-"+self.singername[num]+'-'+"歌词.txt"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w') as f:
                f.write(txt)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
    def get_music_pic(self,num,return_url=False):
        try:
            url=self.pic
            name=self.songname[num]+"-"+self.singername[num]+'-'+"封面.jpg"
            if return_url:
                return url
            download.download(url,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
##测试代码
##a=fivesing('fc',l=True,p=True)
##a.search("11")
##a.prints()
