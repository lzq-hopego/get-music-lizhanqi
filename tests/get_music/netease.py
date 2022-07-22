import requests,json
from get_music import download
# import download


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
        for i in range(0,len(name)):
            print("序号{}\t\t{}————{}".format(i+1,name[i],singer[i]))
        songs=input('请选择您要下载哪一首歌，直接输入序号就行\n如需下载多个请用逗号分割即可，例如1,2\n输入0可以继续搜索下一页\n输入-1可以继续搜索上一页\n如果不需要下载多个，请直接输入序号就行：')
        if songs=='':
            print('\n\n\n——您未做出选择！程序即将自动退出！！！')
            return
        elif songs=='0':
            self.search(self.songname,page=self.page+1)
            self.prints()
            return
        elif songs=='-1':
            if self.page-1==-1:
                print("\n已经是第一页啦！")
                return 
            self.search(self.song_name,page=self.page-1)
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
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的歌词！")
    def get_music_pic(self,num):
        try:
            url=self.pic[num]
            name=self.song_name[num]+"-"+self.songer_name[num]+'-'+"封面.jpg"
            download.download(url,name)
            print("\n歌曲封面下载完成，文件名称为:"+name)
        except:
            print("未找到该歌曲的封面！")
##测试代码
##a=netease(l=True,p=True)
##d=a.search("11")
##a.prints()
##input()
