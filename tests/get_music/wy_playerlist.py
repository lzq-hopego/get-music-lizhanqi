import requests,re
from get_music.netease import netease
from get_music.download import download

def wy_playerlist(url,pic=False,lrc=False):
    wy=netease()
    s=requests.session()

    s.headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
               }
    s.get("https://music.163.com/",timeout=1)
    '''7101557391'''
    page_url='https://music.163.com/playlist?id='
    if 'music.163.com' in url:
        page_url=url
    else:
        page_url+=url
    html=s.get(page_url,timeout=1)
    html.encoding='utf-8'
    txt=html.text
    user_name=re.findall('<a href=".*" class="s-fc7">(.*?)<\/a>',txt)[0]
    init_time=re.findall('<span class="time s-fc4">(.*?)&nbsp;创建<\/span>',txt)[0]

    li=re.findall('<ul class="f-hide">(.*?)<\/ul>',txt)[0]


    netease_url='http://music.163.com'
    songs_url=['http://music.163.com/song/media/outer/url?id=','.mp3']

    ls=re.findall('<a href="(.*?)">(.*?)</a>',li)
        
    urls,song_name=zip(*ls)

    print('本歌单由“'+user_name+"”创建,创建时间："+init_time)
    print("为了您后面下载歌曲时的安全考虑，暂时不会打印出歌手,下载完成后会自动保存歌手名字")
    print("平台限制，只能打印出10首哦")
    for i in range(len(urls)):
        print("序号:{}\t{}".format(i+1,song_name[i]))

    songs=input('请选择您要下载哪一首歌，直接输入序号就行\n如需下载多个不连续的请用英文逗号分割即可，例如1,2\n如需下载多个连续的请用-分割即可，例如1-3\n如需全部下载，请输入all\n如果不需要下载多个，请直接输入序号就行:')
    if songs=='':
        print('\n\n\n——您未做出选择！程序即将自动退出！！！')
        return
    if songs=='all':
        song_list=[x+1 for x in range(len(song_name))]
    elif '-' in songs:
        song_list=[x+1 for x in range(int(songs.split('-')[0]),int(songs.split('-')[-1])+1)]
    else:
        song_list=songs.split(",")
        if len(song_list)==1:
            song_list=songs.split("，")

    for i in song_list:
        i=int(i)-1
        try:
            html=s.get(netease_url+urls[i],timeout=1)
            html.encoding='utf-8'
            txt=html.text
            song_id=urls[i].split('=')[-1]
            song_url=(song_id).join(songs_url)
            p=re.findall(r'<p class="des s-fc4">(.*?)<\/p>',txt)[0]
            singer=(re.findall(r'<span title="(.*?)">',p)[0]).replace('amp;','')
            download(song_url,song_name[i]+"-"+singer+".mp3")
            if pic:
                img_url=re.findall('<img src=".*" class="j-img" data-src="(.*?)">',txt)[0]
                download(img_url,song_name[i]+"-"+singer+".jpg")
            if lrc:
                txt=wy.get_music_lrc(song_id)
                with open(song_name[i]+"-"+singer+".txt",'w') as f:
                    f.write(txt)
        except:
            print('\n\n\n——无法下载或解析歌曲！！！')
