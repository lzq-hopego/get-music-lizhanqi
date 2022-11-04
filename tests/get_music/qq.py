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
        self.song_name = songname
        url='https://shc6.y.qq.com/soso/fcgi-bin/search_for_qq_cp?w={}&p={}&n=10&format=json'.format(self.song_name,self.page)
        d=requests.get(url,headers=self.headers,timeout=1).json()
        ls=d['data']['song']['list']
        self.songname=[]
        self.singername=[]
        self.songs_url=[]
        self.mid=[]
        for i in ls:
            self.mid.append(i['albummid'])
            self.songname.append(i['songname'])
            self.singername.append(','.join([i['name'] for i in i['singer']]))
            self.songs_url.append(i['songmid'])
        return self.songname,self.singername,self.songs_url
    def prints(self):
        pass

    def get_music_url(self,songid):
        url_part = "https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D".format(songid)
        music_document_html_json = requests.get(url_part,timeout=1).text
        music_document_html_dict = json.loads(music_document_html_json)  #将文件从json格式转化为字典格式
        music_url_part = music_document_html_dict["req_0"]["data"]["midurlinfo"][0]["purl"]
        if music_url_part != '':
            return music_document_html_dict['req_0']['data']['sip'][0]+music_url_part

    def get_music_pic(self,num,return_url=False):
        try:
            url='https://y.gtimg.cn/music/photo_new/T002R300x300M000'+self.mid[num]+'.jpg'
            if return_url:
                return url
            name=self.songname[num]+"-"+self.singername[num]+'-'+"封面.jpg"
            download.download(url,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:
            console.print("[b red]未找到该歌曲的封面！")
    def get_music_lrc(self,num,return_url=False):
        try:
            name=self.songname[num]+"-"+self.singername[num]+'-'+"歌词.txt"
            headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
             'referer' : 'https://m.y.qq.com'}
            url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg?songmid={}&format=json&nobase64=1&songtype=0&callback=c'.format(self.song_url[num])
            html=requests.get(url,headers=headers,timeout=1)
            html.encoding='utf-8'
            d = unescape(html.text).split('"lyric":"')[-1][:-3]
            if return_url:
                return d
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
