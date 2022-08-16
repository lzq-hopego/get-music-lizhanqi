import requests,json,sys
from get_music import download
from rich.console import Console
from rich.table import Table
# import download
console=Console()
class kugou:
    def __init__(self,p=False,l=False):
        self.headers={
        'UserAgent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
        'Referer' : 'http://m.kugou.com/rank/info/8888',
        'Cookie' : 'UM_distinctid=161d629254c6fd-0b48b34076df63-6b1b1279-1fa400-161d629255b64c; kg_mid=cb9402e79b3c2b7d4fc13cbc85423190; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1523818922; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1523819865; Hm_lvt_c0eb0e71efad9184bda4158ff5385e91=1523819798; Hm_lpvt_c0eb0e71efad9184bda4158ff5385e91=1523820047; musicwo17=kugou'
        }
        self.l=l
        self.p=p
        self.api='酷狗音乐'
    def search(self,songname,page=1):
        self.page=page
        self.song_name=songname
        self.url="http://mobilecdngz.kugou.com/api/v3/search/song?tag=10&page="+str(self.page)+"&tagtype=%E5%85%A8%E9%83%A8&area_code=1&plat=2&sver=5&api_ver=1&showtype=10&version=8969&keyword="+self.song_name
        req=requests.get(self.url,headers=self.headers,timeout=1)
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
    def prints(self):
        name=self.songname
        singer=self.singername
        song_url=self.songs_url
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
            self.search(self.song_name,page=self.page+1)
            self.prints()
            return
        elif songs=='-1':
            if self.page-1==0:
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
                songurl=self.get_music_url(url)
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
                download.download(songurl,fname,ouput=True)
                console.print('[b red]'+singer[i]+'唱的'+name[i]+'下载完成啦！')
                console.print("[b red]已保存至当前目录下")
            except IndexError:
                console.print("[b red]您输入的序号不在程序给出的序号范围！")
                return
        console.print('[b green]\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')

    def get_music_url(self,ls):
        try:
            url='http://m.kugou.com/app/i/getSongInfo.php?cmd=playInfo&hash='+ls[0]
            d=requests.get(url,headers=self.headers).json()
            self.d=d
            return d['backup_url'][0]
        except:
            url="https://www.kugou.com/yy/index.php?r=play/getdata&hash="+ls[0]+"&album_id="+str(ls[1]) 
            d=json.loads(requests.get(url,headers=self.headers,timeout=1).text)
            self.d=d
            if d["data"]["play_url"]=='':
                return '未能成功获取音乐下载地址'
                sys.exit()
            else:
                return d["data"]["play_url"]
    def get_music_lrc(self,num):
        try:
            url='http://m.kugou.com/app/i/krc.php?cmd=100&timelength=999999&hash='+self.songs_url[num][0]
            name=self.songname[num]+'-'+self.singername[num]+'-'+'歌词.txt'
            html=requests.get(url)
            html.encoding='utf-8'
            txt=html.text
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w',encoding='utf-8') as f:
                f.write(txt)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            try:
                text=self.d['data']['lyrics']
                name=self.songname[num]+'-'+self.singername[num]+'-'+'歌词.txt'
                
                with open(name,'w',encoding='utf-8') as f:
                    f.write(text)
                console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
            except:
                console.print("[b red]未找到该歌曲的歌词！")
        
            
    def get_music_pic(self,num):
        try:
            img=self.d['album_img'].replace('{size}','150')
            name=self.songname[num]+'-'+self.singername[num]+'-'+'封面.jpg'
            download.download(img,name)
            console.print("[b green]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            try:
                img=self.d['data']['img']
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
