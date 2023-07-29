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
        head={'Accept': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Connection': 'keep-alive', 'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1690602130; _ga=GA1.2.2146219107.1690602130; _gid=GA1.2.231277200.1690602130; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1690603342; _ga_ETPBRPM9ML=GS1.2.1690602130.1.1.1690603342.60.0.0; Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=3dYFF6zG6WBPtTS6KPGZ7jDBP5tfSN4A', 'Host': 'kuwo.cn', 'Referer': 'https://kuwo.cn/search/list?key=%E5%8D%9C%E5%8D%A6', 'https': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"', 'Sec-Ch-Ua': '"Windows"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Windows"', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Secret': '6d38232abcb2974e886caf10d0b2cacb76e5bed28a8778c9284978b7f7f7237a0233c6c3'}
        url='http://kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=20&httpsStatus=1&reqId=8be68b90-1e37-11ed-9b24-a14423fc8744'.format(self.song_name,str(self.page))
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
            try:
                self.pic.append(misicInfo[i]['pic'])
            except:
                self.pic.append('')
        return self.songname,self.singername,self.songs_url
    def prints(self):
        pass


    def get_music_url(self,songid):
        url2='https://kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=7a499ad0-2dc7-11ee-9b11-d573dcd2a9d2&plat=web_www&from='.format(songid)
        head={'Host':'kuwo.cn',
              'Cookie':'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1690625730; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1690625730; _ga=GA1.2.438975400.1690625730; _gid=GA1.2.265176886.1690625730; _gat=1; _ga_ETPBRPM9ML=GS1.2.1690625730.1.0.1690625730.60.0.0; Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=rWSMW8NykzdryGC2ejXpscaj3k5NZPrF',
              'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
              'Secret':'2c0b2921adbca370d5418932dda1dacf58dfa1f8ce8e5de14b17399ffee9657d021b5fd1'
              }
        response2=requests.get(url=url2,headers=head)
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
        head={'Host':'kuwo.cn',
              'Cookie':'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1690625730; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1690625730; _ga=GA1.2.438975400.1690625730; _gid=GA1.2.265176886.1690625730; _gat=1; _ga_ETPBRPM9ML=GS1.2.1690625730.1.0.1690625730.60.0.0; Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=rWSMW8NykzdryGC2ejXpscaj3k5NZPrF',
              'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
              'Secret':'2c0b2921adbca370d5418932dda1dacf58dfa1f8ce8e5de14b17399ffee9657d021b5fd1'
              }
        try:
            url='http://kuwo.cn/newh5/singles/songinfoandlrc?musicId='+str(self.songs_url[num])
            html=requests.get(url,timeout=3,headers=head)
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
##a=kuwo(p=True,l=True)
##a.search('卜卦')
####a.get_music_pic(0,return_url=True)
####a.get_music_lrc(0,return_url=True)
##a.prints()




