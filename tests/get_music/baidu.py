

import requests
import re
import time
import hashlib
import sys
import os
##pic=True
##lrc=True

def baidu(keywords):
##    pass
##    keywords = "海底"
    path="音乐"
    headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    params = (
    ('word', keywords),
    )
    # 参数timeout=5 防止访问超时
    response = requests.get('https://music.taihe.com/search', headers=headers,params=params)
    # 歌曲页码数
    ##page_NUM = re.findall(r'<li class="number">(.*?)</li>', response.text, re.S)
    ##print(page_NUM)

    # 演示获取第一页歌曲tsid
    url_fenye = f'https://music.taihe.com/search?word={keywords}&pageNo=1'
    response = requests.get(url=url_fenye, headers=headers)
    text=response.text
    tsids = re.findall(r'<a href="/song/(.*?)"', text, re.S)
    song_name=re.findall(r'<a href="/artist/.*?".*?>(.*?)</a>', text, re.S)
    sings=re.findall(r'<a href="/song/.*?".*?>(.*?)</a>', text, re.S)
##    print(len(song_name))
    if len(song_name)==len(sings):
        s=len(song_name)
    if len(song_name)<len(sings):
        s=len(song_name)
    if len(song_name)>len(sings):
        s=len(sings)
    for i in range(0,s):
        print("序号：{} \t {}——{}".format(i+1,sings[i],song_name[i]))
        
    try:
        try:
            a=input("请输入下载序号(不支持多个同时下载)：").split(",")
        except:
            a=input("请输入下载序号(不支持多个同时下载)：").split(",")
    except:
        print('\n\n\n——您未做出选择！程序即将自动退出！！！')
        sys.exit()
    for i in a:
        try:
            i=int(i)-1
            tsid = tsids[i]
        except:
            print('\n\n\n——您未做出选择(或没有输入正确的序号)！程序即将自动退出！！！')
            sys.exit()
        
        
        r = f"TSID={tsid}&appid=16073360&timestamp={str(int(time.time()))}0b50b02fd0d73a9c4c8c3a781c30845f"
        sign = hashlib.md5(r.encode(encoding='UTF-8')).hexdigest()
        # print(sign) # 获取到的就是每一首歌曲的sign值，下面构造params
        params = (
        ('sign', sign),
        ('appid', '16073360'),
        ('TSID', tsid),
        ('timestamp', str(int(time.time()))),
        )
        # 具体歌曲的相关属性
        song_info = requests.get('https://music.taihe.com/v1/song/tracklink',params=params, timeout=5).json()[
         'data']
        singer_name = song_info['artist'][0]['name']  # 歌手名
        Song_name = song_info['title']  # 歌名
        song_link = song_info['path']  # 音频地址
        lrc_link = song_info['lyric']  # 歌词地址
        pic_url=song_info['pic']
        weather=input("是否下载歌词(直接回车默认只下载歌曲)(yes/no)：")
        if weather in ['y',"Y",'yes','YES']:
            path=os.getcwd()+'\\音乐\\'+Song_name+"_"+singer_name
            try:
                os.mkdir(path)
            except:
                pass
            if lrc_link:
                geci=requests.get(lrc_link)
                with open(path+"/"+Song_name+"-"+singer_name+".lrc",'wb') as f:
                    f.write(geci.content)
            else:
                print("\n未找到当前歌曲的歌词")
            if pic_url:
                haibao=requests.get(pic_url)
                with open(path+"\\"+Song_name+"-"+singer_name+".jpg",'wb') as f:
                    f.write(haibao.content)
            else:
                print("\n为找当前歌曲的封面")
            

            
        gequ=requests.get(song_link)
        with open(path+"/"+Song_name+"-"+singer_name+".mp3",'wb') as f:
                f.write(gequ.content)
            
    print("\n歌曲已保存至{}".format(os.getcwd()+"\\"+path))
    print('\n≧∀≦\n感谢您对本程序的使用，祝您生活愉快！')
    sys.exit()
##    print(singer_name)
##    print(Song_name)
##    print(song_link)
##    print(lrc_link)
