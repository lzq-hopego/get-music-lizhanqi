import requests,json,sys
from get_music import download
# import download



class migu:
    def __init__(self,p=False,l=False):
        self.head={"referer": "http://music.migu.cn/",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/33",
            }
        self.url="http://pd.musicapp.migu.cn/MIGUM2.0/v1.0/content/search_all.do"
        self.params = {
            "ua": "Android_migu",
            "version": "5.0.1",
            "text": '',
            "pageNo": "1",
            "pageSize": "1",
            "searchSwitch": '{"song":1,"album":0,"singer":0,"tagSong":0,"mvSong":0,"songlist":0,"bestShow":1}',
        }
        self.l=l
        self.p=p
    def search(self,songname,page=1):
        self.params['pageNo']=self.page=page
        self.params['text']=self.songname=songname
        req=requests.get(self.url,headers=self.head,params=self.params,timeout=3)
        res_data=json.loads(req.text)['songResultData']["result"]
        self.singers=[]
        self.song_name=[]
        self.song_url=[]

        self.pic=[]
        self.id=[]
        for i in res_data:
            self.singers.append(i['singers'][0]['name'])
            self.id.append(i["copyrightId"])
            self.song_name.append(i['name'])
            rate_list=sorted(i["rateFormats"],key=lambda x:int(x["size"]),reverse=True)
            Songurl='https://freetyst.nf.migu.cn/'
            self.pic.append(i["imgItems"][0]['img'])
            for i in rate_list:
                if "androidUrl" in list(i.keys()):
                    ftp=i['androidUrl'].replace("ftp://218.200.160.122:21/",Songurl)
                    break
                if 'url' in list(i.keys()):
                    ftp=i['url'].replace("ftp://218.200.160.122:21/",Songurl)
                    break
            self.song_url.append(ftp)
        return self.song_name,self.singers,self.song_url
    def prints(self):
        name=self.song_name
        singer=self.singers
        song_url=self.song_url
        for i in range(0,len(name)):
            print("序号{}\t\t{}————{}".format(i+1,name[i],singer[i]))
        songs=input('请选择您要下载哪一首歌，直接输入序号就行\n如需下载多个请用逗号分割即可，例如1,2\n输入0可以继续搜索下一页\n如果不需要下载多个，请直接输入序号就行：')
        if songs=='':
            print('\n\n\n——您未做出选择！程序即将自动退出！！！')
            return
        elif songs=='0':
            self.search(self.songname,page=self.page+1)
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
                
                fname=name[i]+"-"+singer[i]+"."+song_url[i].split(".")[-1]
                url=song_url[i]
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
                download.download(url,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
    def get_music_lrc(self,num):
        try:
            headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
             'accept' :"application/json, text/plain, */*",
             'referer':'http://music.migu.cn/v3/music/player/audio',
             }
            url='https://music.migu.cn/v3/api/music/audioPlayer/getLyric?copyrightId='+str(self.id[num])
            html=requests.get(url,headers=headers)
            txt=html.json()['lyric']
            name=self.song_name[num]+"-"+self.singers[num]+'-'+"歌词.txt"
            with open(name,'w') as f:
                f.write(txt)
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的歌词！")
        
    def get_music_pic(self,num):
        try:
            url=self.pic[num]
            name=self.song_name[num]+"-"+self.singers[num]+'-'+"封面.jpg"
            download.download(url,name)
            print("\n歌曲封面下载完成，文件名称为:"+name)
        except:
            print("未找到该歌曲的封面！")
##a=migu(l=True,p=True)
##a.search('爱人错过')
##a.prints()
