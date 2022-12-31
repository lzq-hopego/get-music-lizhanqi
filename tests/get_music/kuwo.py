import requests,json
from get_music import download
from rich.console import Console
##import download
console=Console()
class kuwo:
    def __init__(self,p=False,l=False):
        self.l=l
        self.p=p
        self.api='酷我音乐'
    def search(self,songname,page=1):
        self.page=page
        self.song_name=songname
        head={'Cookie': 'gid=75fc1b5f-eb95-4729-b003-720c762f08b7; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660743549; _ga=GA1.2.1866439872.1660743590; _gid=GA1.2.1454874071.1660743590; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660745907; kw_token=DHJNKLIK778',
        'csrf': 'DHJNKLIK778',
        'Host': 'www.kuwo.cn',
        'Referer': 'http://www.kuwo.cn/search/list?key=test',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
        url='http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=20&httpsStatus=1&reqId=8be68b90-1e37-11ed-9b24-a14423fc8744'.format(self.song_name,str(self.page))
        response=requests.get(url=url,headers=head)
        dict2=json.loads(response.text)
        misicInfo=dict2['data']['list']  # 歌曲信息的列表
        self.songname=list()   # 歌曲名称的列表
        self.singername=[]
        self.songs_url=[]   # 存储歌曲下载链接的列表
        self.pic=[]
        for i in range(len(misicInfo)):
            self.singername.append(misicInfo[i]['artist'])
            self.songname.append(misicInfo[i]['name'].replace("|",'').replace('&nbsp;','').replace('cover:',''))
            self.songs_url.append(misicInfo[i]['rid'])
            self.pic.append(misicInfo[i]['pic'])
        return self.songname,self.singername,self.songs_url
    def prints(self):
        pass


    def get_music_url(self,songid):
        url2='http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=9e58f6a0-b88e-11ec-a21e-535a6948e2ff'.format(songid)
        headers2={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
        response2=requests.get(url=url2,headers=headers2)
        dict3=json.loads(response2.text)
        self.d=dict3
        try:
            url=dict3['data']['url']
        except:
            return ''
        return url
    def get_music_pic(self,num,return_url=False):
        try:
            url=self.pic[num]
            if return_url:
                return url
            name=self.songname[num]+"-"+self.singername[num]+'-'+"封面.jpg"
            req=requests.get(url,timeout=1)
            with open(name,'wb') as f:
                f.write(req.content)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
    def get_music_lrc(self,num,return_url=False):
        try:
            url='http://kuwo.cn/newh5/singles/songinfoandlrc?musicId='+str(self.songs_url[num])
            html=requests.get(url,timeout=1)
            text=html.json()['data']['lrclist']
            s=''
            for i in text:
                s+='['+i['time']+']'+'    '+i['lineLyric']+'\n'
            if return_url:
                return s
            name=self.songname[num]+"-"+self.singername[num]+'-'+".歌词.txt"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w') as f:
                f.write(s)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
##测试代码
####a=kuwo(p=True,l=True)
####a.search('11')
####a.get_music_pic(0,return_url=True)
####a.get_music_lrc(0,return_url=True)
##a.prints()
##input()




