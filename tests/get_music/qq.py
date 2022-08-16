import requests
import json,re,sys,html
import urllib.parse
from get_music import download
from rich.console import Console
from rich.table import Table
# import download
console=Console()

class qq:
    def __init__(self,p=False,l=False):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/33',
            'referer':'https://m.y.qq.com/'
            }
        self.l=l
        self.p=p
        self.api='QQ音乐'
    def search(self,songname,page=1):
        self.page = page
        self.songname = songname
        url='https://shc6.y.qq.com/soso/fcgi-bin/search_for_qq_cp?w={}&p={}&n=10&format=json'.format(self.songname,self.page)
        d=requests.get(url,headers=self.headers,timeout=1).json()
        ls=d['data']['song']['list']
        self.song_name=[]
        self.singer_name=[]
        self.song_url=[]
        self.mid=[]
        for i in ls:
            self.mid.append(i['albummid'])
            self.song_name.append(i['songname'])
            self.singer_name.append(','.join([i['name'] for i in i['singer']]))
            self.song_url.append(i['songmid'])
        return self.song_name,self.singer_name,self.song_url
    def prints(self):
        name=self.song_name
        singer=self.singer_name
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
                songid=song_url[i]
                songurl=self.get_music_url(songid)
##                print(get_music_url)
                if songurl==None:
                    console.print("[b red]很抱歉由于某种原因无法为您下载"+singer[i]+'唱的'+name[i]+'的歌')
                    return
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
    def get_music_url(self,songid):
        url_part = "https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D".format(songid)
        music_document_html_json = requests.get(url_part,timeout=1).text
        music_document_html_dict = json.loads(music_document_html_json)  #将文件从json格式转化为字典格式
        music_url_part = music_document_html_dict["req_0"]["data"]["midurlinfo"][0]["purl"]
        if music_url_part != '':
            return music_document_html_dict['req_0']['data']['sip'][0]+music_url_part

    def get_music_pic(self,num):
        try:
            url='https://y.gtimg.cn/music/photo_new/T002R300x300M000'+self.mid[num]+'.jpg'
            name=self.song_name[num]+"-"+self.singer_name[num]+'-'+"封面.jpg"
            download.download(url,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
    def get_music_lrc(self,num):
        try:
            name=self.song_name[num]+"-"+self.singer_name[num]+'-'+"歌词.txt"
            headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
             'referer' : 'https://m.y.qq.com'}
            url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg?songmid={}&format=json&nobase64=1&songtype=0&callback=c'.format(self.song_url[num])
            html=requests.get(url,headers=headers,timeout=1)
            html.encoding='utf-8'
            d = unescape(html.text).split('"lyric":"')[-1][:-3]
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w',encoding='utf-8') as f:
                f.write(d)
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            console.print("[b red]未找到该歌曲的歌词！")
def unescape(string):
    string = urllib.parse.unquote(string)
    quoted = html.unescape(string).encode(sys.getfilesystemencoding()).decode('utf-8')
    #转成中文
    return re.sub(r'%u([a-fA-F0-9]{4}|[a-fA-F0-9]{2})', lambda m: chr(int(m.group(1), 16)), quoted)

##测试代码
##a=qq(l=True)
##a.search('11')
##a.get_music_lrc(1)
##a.prints()
##input()
