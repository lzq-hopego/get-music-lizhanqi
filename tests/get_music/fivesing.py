import requests,re
from get_music import download
# import download

class fivesing:
    def __init__(self,songtype,p=False,l=False):
        self.songtype=songtype
        self.headers={'referer': 'http://search.5sing.kugou.com/?keyword='+str("11"),
         "Accept" : "application/json, text/javascript, */*; q=0.01"}
        self.l=l
        self.p=p
    def search(self,songname,page=1):
        self.page=page
        self.songname=songname
        
        if self.songtype=='yc':
            typename='1'
        else:
            typename='2'
        self.headers['referer']=self.headers.get('referer')+self.songname
        url='http://search.5sing.kugou.com/home/json?keyword={}&sort=1&filter={}&page={}'.format(songname,typename,self.page)
        req=requests.get(url,headers=self.headers,timeout=1)
        d=req.json()
        self.song_id=[]
        self.song_name=[]
        self.singer_name=[]
        for i in d['list']:
            self.song_id.append(i['songId'])
            self.singer_name.append(i['nickName'])
            self.song_name.append(re.findall('<em class="keyword">(.*?)</em>',i['songName'])[0])
        return self.song_name,self.singer_name,self.song_id
    def prints(self):
        name=self.song_name
        singer=self.singer_name
        song_url=self.song_id
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
                fname=name[i]+"-"+singer[i]+".mp3"
                url=song_url[i]
                songurl=self.get_music_url(url)
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
                download.download(songurl,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')

    def get_music_url(self,songid):
        url2='http://service.5sing.kugou.com/song/getsongurl?songid={}&songtype={}'.format(songid,self.songtype)
        headers=self.headers
        headers['referer']='http://5sing.kugou.com/'+'/'+self.songtype+str(songid)
        req=requests.get(url2,headers=headers)
        d=req.json()
        self.pic=d['data']['user']['I']
        return d['data']['lqurl']
    def get_music_lrc(self,num):
        try:
            url='http://5sing.kugou.com/fm/m/json/lrc?songId={}&songType={}'.format(self.song_id[num],self.songtype)
            req=requests.get(url,timeout=3)
            txt=req.json()['txt']
            name=self.song_name[num]+"-"+self.singer_name[num]+'-'+"歌词.txt"
            with open(name,'w') as f:
                f.write(txt)
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的歌词！")
    def get_music_pic(self,num):
        try:
            url=self.pic
            name=self.song_name[num]+"-"+self.singer_name[num]+'-'+"封面.jpg"
            download.download(url,name)
            print("\n歌曲封面下载完成，文件名称为:"+name)
        except:
            print("未找到该歌曲的封面！")
##a=fivesing('fc',l=True,p=True)
##a.search("11")
##a.prints()
