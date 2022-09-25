import requests,json
from get_music import download
from rich.console import Console
from rich.table import Table
# import download
console=Console()
class kuwo:
    def __init__(self,p=False,l=False):
        self.l=l
        self.p=p
        self.api='酷我音乐'
    def search(self,songname,page=1):
        self.page=page
        self.songname=songname
        head={'Cookie': 'gid=75fc1b5f-eb95-4729-b003-720c762f08b7; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660743549; _ga=GA1.2.1866439872.1660743590; _gid=GA1.2.1454874071.1660743590; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660745907; kw_token=DHJNKLIK778',
        'csrf': 'DHJNKLIK778',
        'Host': 'www.kuwo.cn',
        'Referer': 'http://www.kuwo.cn/search/list?key=test',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
        url='http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=20&httpsStatus=1&reqId=8be68b90-1e37-11ed-9b24-a14423fc8744'.format(songname,str(self.page))
        response=requests.get(url=url,headers=head)
        dict2=json.loads(response.text)
        misicInfo=dict2['data']['list']  # 歌曲信息的列表
        self.musicNames=list()   # 歌曲名称的列表
        self.singer=[]
        self.song_url=[]   # 存储歌曲下载链接的列表
        self.pic=[]
##        return misicInfo
        for i in range(len(misicInfo)):
##            songurl=get_url(misicInfo[i]['rid'])
##            if songurl != '' :
##            print(misicInfo[i]['artist'].replace('&nbsp;',''))
            self.singer.append(misicInfo[i]['artist'])
            self.musicNames.append(misicInfo[i]['name'].replace("|",'').replace('&nbsp;','').replace('cover:',''))
            self.song_url.append(misicInfo[i]['rid'])
            self.pic.append(misicInfo[i]['pic'])
        return self.musicNames,self.singer,self.song_url
    def prints(self):
        name=self.musicNames
        singer=self.singer
        song_url=self.song_url
        table = Table(style='purple',title='[b green]get-music-lizhanqi')
        table.add_column('[red]序号',justify='center')
        table.add_column('[yellow]歌曲名',justify='center',overflow=True)
        table.add_column('[blue]歌手',justify='center',overflow=True)
        table.add_column('[green]平台',justify='center',overflow=True)
        for i in range(0,len(name)):
            table.add_row('[b red]'+str(i+1),'[yellow]'+name[i],'[blue]'+singer[i],'[b green]'+self.api,end_section=True)
        console.print(table)
        songs=console.input('[b green]请选择您要下载哪一首歌，直接输入[b red]序号[/]就行\n如需下载多个请用[b red]英文逗号[/]分割即可，[b blue]例如1,2[/]\n输入[b red]0[/]可以继续搜索[b red]下一页[/]\n输入[b red]-1[/]可以继续搜索[b red]上一页[/]\n如果不需要下载多个，请直接输入序号就行:')
        if songs=='':
            console.print('[b red]\n\n\n——您未做出选择！程序即将自动退出！！！')
            return
        elif songs=='0':
            self.search(self.songname,page=self.page+1)
            self.prints()
            return
        elif songs=='-1':
            if self.page-1==0:
                console.print("[b red]\n已经是第一页啦！")
                return 
            self.search(self.songname,page=self.page-1)
            self.prints()
            return
        song_list=songs.split(",")
        for i in song_list:
            try:
                i=int(i)-1
            except ValueError:
                console.print("[b red]您输入的序号有问题，请用英文逗号分割谢谢！")
                return
            try:
                fname=name[i]+"-"+singer[i]+".mp3"
                url=song_url[i]
                songurl=self.get_music_url(url)
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
##                print(fname,songurl)
               
                if songurl==None:
                    console.print("[b red]很抱歉由于某种原因无法为您下载"+singer[i]+'唱的'+name[i]+'的歌')
                    return
                download.download(songurl,fname,ouput=True)
                console.print('[b red]'+singer[i]+'唱的'+name[i]+'下载完成啦！')
                console.print("[b red]已保存至当前目录下")
            except IndexError:
                console.print("[b red]您输入的序号不在程序给出的序号范围！")
                return
        console.print('[b green]\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')


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
    def get_music_pic(self,num):
        try:
            url=self.pic[num]
            name=self.musicNames[num]+"-"+self.singer[num]+'-'+"封面.jpg"
            req=requests.get(url,timeout=1)
            with open(name,'wb') as f:
                f.write(req.content)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
    def get_music_lrc(self,num):
        try:
            url='http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId='+str(self.song_url[num])
            html=requests.get(url,timeout=1)
            text=html.json()['data']['lrclist']
            s=''
            for i in text:
                s+='['+i['time']+']'+'    '+i['lineLyric']+'\n'
            name=self.musicNames[num]+"-"+self.singer[num]+'-'+".歌词.txt"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w') as f:
                f.write(s)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
##测试代码
##a=kuwo(p=True,l=True)
##a.search('11')
##a.prints()
##input()




