import requests,json
from get_music import download

class oneting:
    def __init__(self):
        self.headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
                   'referer':'https://h5.1ting.com/'}
    def search(self,songname,page=1):
        self.songname=songname
        self.page=page
        url='https://so.1ting.com/song/json?q={}&page={}&size=20'.format(self.songname,self.page)
        req=requests.get(url,headers=self.headers)
        d=req.json()
        self.song_name=[]
        self.singer_name=[]
        self.song_url=[]

        songurl='https://h5.1ting.com/file?url='
        for i in d['results']:
            self.song_name.append(i['song_name'])
            self.singer_name.append(i['singer_name'])
            self.song_url.append(songurl+i['song_filepath'].replace('.wma','.mp3'))
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
                download.download(url,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
##a=oneting()
##a.search("爱人错过")
##a.prints()
##headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
##                   'referer':'https://h5.1ting.com/'}
##url='https://so.1ting.com/song/json?q=11&page=1&size=20'
##
##html=requests.get(url,headers=headers)
##print(html.text
