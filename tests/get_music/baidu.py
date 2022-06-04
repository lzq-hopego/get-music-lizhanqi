

import requests
import re
import time
import hashlib
import sys
import os
from get_music import download
# import download

class baidu:
    def __init__(self,p=False,l=False):
        self.headers = {
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
        self.l=l
        self.p=p
    def search(self,songname,page=1):
        self.songname=songname
        self.page=page
        params = (
        ('word', self.songname),
        )
        response = requests.get('https://music.taihe.com/search', headers=self.headers,params=params,timeout=1)
        url_fenye = 'https://music.taihe.com/search?word={}&pageNo={}'.format(songname,str(self.page))
        response = requests.get(url=url_fenye, headers=self.headers,timeout=1)
        text=response.text
        self.tsids = re.findall(r'<a href="/song/(.*?)"', text, re.S)
        self.song_name=re.findall(r'<a href="/artist/.*?".*?>(.*?)</a>', text, re.S)
        self.sings=re.findall(r'<a href="/song/.*?".*?>(.*?)</a>', text, re.S)
        return self.song_name,self.sings,self.tsids

    def prints(self):
        name=self.sings
        singer=self.song_name
        song_url=self.tsids
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
                download.download(songurl,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
    def get_music_url(self,songid):
        r = f"TSID={songid}&appid=16073360&timestamp={str(int(time.time()))}0b50b02fd0d73a9c4c8c3a781c30845f"
        sign = hashlib.md5(r.encode(encoding='UTF-8')).hexdigest()
        # print(sign) # 获取到的就是每一首歌曲的sign值，下面构造params
        params = (
        ('sign', sign),
        ('appid', '16073360'),
        ('TSID', songid),
        ('timestamp', str(int(time.time()))),
        )
        # 具体歌曲的相关属性
        song_info = requests.get('https://music.taihe.com/v1/song/tracklink',params=params, timeout=5).json()[
         'data']
##        singer_name = song_info['artist'][0]['name']  # 歌手名
##        Song_name = song_info['title']  # 歌名
        self.lrc=song_info['lyric']
        self.pic=song_info['pic']
        return song_info['path']  # 音频地址
    def get_music_lrc(self,num):
        try:
            name=self.sings[num]+"-"+self.song_name[num]+'-'+"歌词.lrc"
            download.download(self.lrc,name)
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的歌词！")
    def get_music_pic(self,num):
        try:
            name=self.sings[num]+"-"+self.song_name[num]+'-'+"封面.jpg"
            download.download(self.pic,name)
            print("\n歌曲封面下载完成，文件名称为:"+name)
        except:
            print("未找到该歌曲的封面！")

##测试代码
##a=baidu(p=True)
##a.search('11')
##a.prints()
