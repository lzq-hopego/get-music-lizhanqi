import requests,sys,json
from get_music import download
from rich.console import Console
from rich.table import Table
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
        self.sname = sname
        self.page=page
        url='http://m.music.migu.cn/migu/remoting/scr_search_tag?keyword={}&type={}&pgc={}&rows={}'.format(self.sname,2,int(self.page),10)
        req=requests.get(url,headers=self.head,timeout=1).json()
        self.songname=[]
        self.singer=[]
        self.songurl=[]
        self.id=[]
        self.pic=[]
        pic=[]
        for i in req['musics']:
            self.songname.append(i['songName'])
            self.singer.append(i['artist'])
            self.songurl.append(i['mp3'])
            self.id.append(i['copyrightId'])
            self.pic.append(i['cover'])
        return self.songname,self.singer,self.songurl
    def prints(self):
        name=self.songname
        singer=self.singer
        song_url=self.songurl
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
            self.search(self.sname,page=self.page+1)
            self.prints()
            return
        elif songs=='-1':
            if self.page-1==0:
                console.print("[b red]\n已经是第一页啦！")
                return 
            self.search(self.sname,page=self.page-1)
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
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
                download.download(url,fname,ouput=True)
                console.print('[b red]'+singer[i]+'唱的'+name[i]+'下载完成啦！')
                console.print("[b red]已保存至当前目录下")
            except IndexError:
                console.print("[b red]您输入的序号不在程序给出的序号范围！")
                return
        console.print('[green]\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
    def get_music_lrc(self,num):
        try:
            headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
             'accept' :"application/json, text/plain, */*",
             'referer':'http://music.migu.cn/v3/music/player/audio',
             }
            url='https://music.migu.cn/v3/api/music/audioPlayer/getLyric?copyrightId='+str(self.id[num])
            html=requests.get(url,headers=headers).json()['lyric']
            name=self.songname[num]+"-"+self.singer[num]+'-'+"歌词.txt"
            with open(name,'w') as f:
                f.write(html)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
        
    def get_music_pic(self,num):
        try:
            url=self.pic[num]
            name=self.songname[num]+"-"+self.singer[num]+'-'+"封面.jpg"
            download.download(url,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
##测试代码
##a=migu(l=True,p=True)
##a.search('周杰伦')
##a.prints()
