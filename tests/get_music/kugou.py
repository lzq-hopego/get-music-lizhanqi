import requests,json
from get_music import download
# import download

class kugou:
    def __init__(self,p=False,l=False):
        self.headers={
        'UserAgent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
        'Referer' : 'http://m.kugou.com/rank/info/8888',
        'Cookie' : 'UM_distinctid=161d629254c6fd-0b48b34076df63-6b1b1279-1fa400-161d629255b64c; kg_mid=cb9402e79b3c2b7d4fc13cbc85423190; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1523818922; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1523819865; Hm_lvt_c0eb0e71efad9184bda4158ff5385e91=1523819798; Hm_lpvt_c0eb0e71efad9184bda4158ff5385e91=1523820047; musicwo17=kugou'
        }
        self.l=l
        self.p=p
    def search(self,songname,page=1):
        self.page=page
        self.song_name=songname
        self.url="http://mobilecdngz.kugou.com/api/v3/search/song?tag=1&page="+str(self.page)+"&tagtype=%E5%85%A8%E9%83%A8&area_code=1&plat=2&sver=5&api_ver=1&showtype=20&version=8969&keyword="+self.song_name
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
        for i in range(0,len(name)):
            print("序号{}\t\t{}————{}".format(i+1,name[i],singer[i]))
        songs=input('请选择您要下载哪一首歌，直接输入序号就行\n如需下载多个请用逗号分割即可，例如1,2\n输入0可以继续搜索下一页\n如果不需要下载多个，请直接输入序号就行：')
        if songs=='':
            print('\n\n\n——您未做出选择！程序即将自动退出！！！')
            return
        elif songs=='0':
            self.search(self.song_name,page=self.page+1)
            self.prints()
            return 
        song_list=songs.split(",")
        for i in song_list:
            try:
                i=int(i)-1
            except ValueError:
                print("您输入的序号有问题，请用英文逗号分割谢谢！")
                return
            try:
                fname=name[i]+"-"+singer[i]+".mp3"
                url=song_url[i]
                song_url=self.get_music_url(url)
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
##                print(song_url)
                download.download(song_url,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')

    def get_music_url(self,ls):
        url="https://www.kugou.com/yy/index.php?r=play/getdata&hash="+ls[0]+"&album_id="+str(ls[1]) 
        d=json.loads(requests.get(url,headers=self.headers,timeout=1).text)
        self.d=d
        return d["data"]["play_url"]
    def get_music_lrc(self,num):
        try:
            text=self.d['data']['lyrics']
            name=self.songname[num]+'-'+self.singername[num]+'-'+'歌词.txt'
            with open(name,'w',encoding='utf-8') as f:
                f.write(text)
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的歌词！")
    def get_music_pic(self,num):
        try:
            img=self.d['data']['img']
            name=self.songname[num]+'-'+self.singername[num]+'-'+'封面.jpg'
            download.download(img,name)
            print("\n歌曲封面下载完成，文件名称为:"+name)
        except:
            print("未找到该歌曲的封面！")

##a=kugou(l=True,p=True)
##a.search('11')
##a.prints()
##input()
