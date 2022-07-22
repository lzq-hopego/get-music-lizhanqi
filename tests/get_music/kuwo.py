import requests,json
from get_music import download
# import download

class kuwo:
    def __init__(self,p=False,l=False):
        self.headers = {
                "Cookie": "_ga=GA1.2.2021007609.1602479334; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1602479334,1602673632; _gid=GA1.2.168402150.1602673633; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1602673824; kw_token=5LER5W4ZD1C",
                "csrf": "5LER5W4ZD1C",
                "Referer": "{}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            }
        self.l=l
        self.p=p
    def search(self,songname,page=1):
        self.page=page
        self.songname=songname
        referer='https://www.kuwo.cn/search/list?key={}'.format(songname)
        self.headers['Referer']="{}".format(referer)
        url='https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=20&httpsStatus=1'.format(songname,str(self.page))
        response=requests.get(url=url,headers=self.headers)
        dict2=json.loads(response.text)
        misicInfo=dict2['data']['list']  # 歌曲信息的列表
        self.musicNames=list()   # 歌曲名称的列表
        self.singer=[]
        self.song_url=[]   # 存储歌曲下载链接的列表
        self.pic=[]
##        return misicInfo
        for i in range(len(misicInfo)):
##            songurl=get_url(misicInfo[i]['rid'])
##            if songurl != '' :
##            print(misicInfo[i]['artist'].replace('&nbsp;',''))
            self.singer.append(misicInfo[i]['artist'])
            self.musicNames.append(misicInfo[i]['name'].replace("|",'').replace('&nbsp;','').replace('cover:',''))
            self.song_url.append(misicInfo[i]['rid'])
            self.pic.append(misicInfo[i]['pic'])
        return self.musicNames,self.singer,self.song_url
    def prints(self):
        name=self.musicNames
        singer=self.singer
        song_url=self.song_url
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
            if self.page-1==0:
                print("\n已经是第一页啦！")
                return 
            self.search(self.songname,page=self.page-1)
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
##                print(fname,songurl)
               
                if songurl==None:
                    print("很抱歉由于某种原因无法为您下载"+singer[i]+'唱的'+name[i]+'的歌')
                    return
                download.download(songurl,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')


    def get_music_url(self,songid):
        url2='http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=9e58f6a0-b88e-11ec-a21e-535a6948e2ff'.format(songid)
        headers2={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
        response2=requests.get(url=url2,headers=headers2)
        dict3=json.loads(response2.text)
        self.d=dict3
        try:
            url=dict3['data']['url']
        except:
            return ''
        return url
    def get_music_pic(self,num):
        try:
            url=self.pic[num]
            name=self.musicNames[num]+"-"+self.singer[num]+'-'+"封面.jpg"
            req=requests.get(url,timeout=1)
            with open(name,'wb') as f:
                f.write(req.content)
            print("\n歌曲封面下载完成，文件名称为:"+name)
        except:
            print("未找到该歌曲的封面！")
    def get_music_lrc(self,num):
        try:
            url='http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId='+str(self.song_url[num])
            html=requests.get(url,timeout=1)
            text=html.json()['data']['lrclist']
            s=''
            for i in text:
                s+='['+i['time']+']'+'    '+i['lineLyric']+'\n'
            name=self.musicNames[num]+"-"+self.singer[num]+'-'+".歌词.txt"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w') as f:
                f.write(s)
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的歌词！")
##测试代码
##a=kuwo(p=True,l=True)
##a.search('11')
##a.prints()
##input()




