import requests,json
from get_music import download
# import download

class oneting:
    def __init__(self,p=False,l=False):
        self.headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
                   'referer':'https://h5.1ting.com/'}
        if l==True:
            print("该接口不支持下载歌词谢谢！搜索继续进行中...")
        
        self.p=p
    def search(self,songname,page=1):
        self.songname=songname
        self.page=page
        url='https://so.1ting.com/song/json?q={}&page={}&size=20'.format(self.songname,self.page)
        req=requests.get(url,headers=self.headers)
        d=req.json()
        self.song_name=[]
        self.singer_name=[]
        self.song_url=[]
        self.pic=[]

        songurl='https://h5.1ting.com/file?url='
        for i in d['results']:
            self.song_name.append(i['song_name'])
            self.pic.append("https:"+i['album_cover'])
            self.singer_name.append(i['singer_name'])
            self.song_url.append(songurl+i['song_filepath'].replace('.wma','.mp3'))
        return self.song_name,self.singer_name,self.song_url
    def prints(self):
        name=self.song_name
        singer=self.singer_name
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
                print("您输入的序号有问题，请用数字且用英文逗号分割谢谢！")
                return
            try:
                fname=name[i]+"-"+singer[i]+".mp3"
                url=song_url[i]
                if self.p==True:
                    self.get_music_pic(num=i)
                download.download(url,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
    def get_music_pic(self,num):
        try:
            url=self.pic[num]
            name=self.song_name[num]+"-"+self.singer_name[num]+'-'+"封面.jpg"
            download.download(url,name)
            print("\n歌曲封面下载完成，文件名称为:"+name)
        except:
            print("未找到该歌曲的封面！")
##a=oneting(l=True,p=True)
##a.search("11")
##a.prints()

