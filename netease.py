import requests,json
from get_music import download
from rich.console import Console
from rich.table import Table
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
        self.data['s']=self.songname=songname
        req=requests.post(self.url,headers=self.headers,data=self.data,timeout=1)
        d=json.loads(req.text)
##        return d
        song_url=['http://music.163.com/song/media/outer/url?id=','.mp3']
        songs=d["result"]['songs']
        self.song_name=[]
        self.song_id=[]
        self.songer_name=[]

        self.id=[]
        self.pic=[]
        for i in songs:
                self.song_id.append(str(i['id']).join(song_url))
                self.song_name.append(i["name"])
                self.songer_name.append(i['ar'][0]["name"])
                self.id.append(i['id'])
                self.pic.append(i['al']['picUrl'])
        return self.song_name,self.songer_name,self.song_id
    def prints(self):
        name=self.song_name
        singer=self.songer_name
        song_url=self.song_id
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
            if self.page-1==-1:
                console.print("[b red]\n已经是第一页啦！")
                return 
            self.search(self.song_name,page=self.page-1)
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
        console.print('[b green]\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
    def get_music_lrc(self,num):
        try:
            song_id=self.id[num]
            headers = {
                "user-agent" : "Mozilla/5.0",
                "Referer" : "http://music.163.com",
                "Host" : "music.163.com"
            }
            if not isinstance(song_id, str):
                song_id = str(song_id)
            url = f"http://music.163.com/api/song/lyric?id={song_id}+&lv=1&tv=-1"
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            json_obj = json.loads(r.text)
            name=self.song_name[num]+"-"+self.songer_name[num]+'-'+"歌词.txt"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w') as f:
                f.write(json_obj["lrc"]["lyric"])
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
    def get_music_pic(self,num):
        try:
            url=self.pic[num]
            name=self.song_name[num]+"-"+self.songer_name[num]+'-'+"封面.jpg"
            download.download(url,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
##测试代码
##a=netease(l=True,p=True)
##d=a.search("11")
##a.prints()
##input()
