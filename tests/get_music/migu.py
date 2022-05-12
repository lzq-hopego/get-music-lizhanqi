import requests,json,sys
from get_music import download




class migu:
    def __init__(self):
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
    def search(self,songname,page=1):
        self.params['pageNo']=self.page=page
        self.params['text']=self.songname=songname
        req=requests.get(self.url,headers=self.head,params=self.params,timeout=1)
        res_data=json.loads(req.text)['songResultData']["result"]
        
        self.singers=[]
        self.song_name=[]
        self.song_url=[]

        for i in res_data:
            self.singers.append(i['singers'][0]['name'])
            song_id=i["contentId"]
            self.song_name.append(i['name'])
            rate_list=sorted(i["rateFormats"],key=lambda x:int(x["size"]),reverse=True)
            Songurl='https://freetyst.nf.migu.cn/'
            for i in rate_list:
                if "androidUrl" in list(i.keys()):
                    ftp=i['androidUrl'].replace("ftp://218.200.160.122:21/",Songurl)
                    break
                if 'url' in list(i.keys()):
                    ftp=i['url'].replace("ftp://218.200.160.122:21/",Songurl)
                    break
            self.song_url.append(ftp)
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
                download.download(url,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
##a=migu()
##a.search('爱人错过')
##a.prints()
##q="天路"
##def migu(q):
##    url="http://pd.musicapp.migu.cn/MIGUM2.0/v1.0/content/search_all.do"
##    head={"referer": "http://music.migu.cn/",
##          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/33",
##          
##        }
##    params = {
##            "ua": "Android_migu",
##            "version": "5.0.1",
##            "text": q,
##            "pageNo": "1",
##            "pageSize": "1",
##            "searchSwitch": '{"song":1,"album":0,"singer":0,"tagSong":0,"mvSong":0,"songlist":0,"bestShow":1}',
##        }
##
##    html=requests.get(url,headers=head,params=params,timeout=1)
##
##    res_data=json.loads(html.text)['songResultData']["result"]
##    singers=[]
##    song_name=[]
##    song_url=[]
##    print("——正在分析数据，请耐心等待——\n")
##
##    for i in res_data:
##        singers.append(i['singers'][0]['name'])
##        song_id=i["contentId"]
##        song_name.append(i['name'])
##        rate_list=sorted(i["rateFormats"],key=lambda x:int(x["size"]),reverse=True)
##        Songurl='https://freetyst.nf.migu.cn/'
##        for i in rate_list:
##            if "androidUrl" in list(i.keys()):
##                ftp=i['androidUrl'].replace("ftp://218.200.160.122:21/",Songurl)
##                break
##            if 'url' in list(i.keys()):
##                ftp=i['url'].replace("ftp://218.200.160.122:21/",Songurl)
##                break
##        song_url.append(ftp)
##
##    for i in range(0,len(singers)):
##        print("序号：{} \t{}——{}".format(i+1,song_name[i],singers[i]))
##    try:
##        a=int(input("请输入您需要下载的歌曲序号(不支持多个同时下载):"))-1
##    except:
##        print('\n\n\n——您未做出选择！程序即将自动退出！！！')
##        sys.exit()
##
##    songurl=song_url[a]
##    ##    rep=requests.get(song_url[a])
##    geshi=song_url[a].split(".")[-1]
##    if geshi=="flac":
##            print("由于歌曲品质过高，所以会占用很长的下载时间，请保持网络畅通，谢谢")
##    fname=song_name[a]+"-"+singers[a]+"."+geshi
##    download.download(songurl,fname,ouput=True)
##    ##    with open("音乐/"+song_name[a]+"-"+singers[a]+"."+geshi,'wb')as f:
##    ##        f.write(rep.content)
##
##    print("\n\n"+singers[a]+'唱的'+song_name[a]+'下载完成啦！')
##    print("已保存至当前目录下")
##    print('\n≧∀≦\感谢您对本程序的使用，祝您生活愉快！')
