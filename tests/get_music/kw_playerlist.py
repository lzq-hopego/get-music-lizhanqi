import requests,re
from get_music.kuwo import kuwo
from get_music.download import download

def kw_playerlist(url,pic=False,lrc=False):
    kw=kuwo()
    pic=False
    lrc=False
    headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Lenovo L78051 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/4125 MicroMessenger/8.0.15.2020(0x28000F31) Process/toolsmp WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64'
             ,'Host': 'm.kuwo.cn'}
    page_url='http://m.kuwo.cn/newh5app/playlist_detail/{}?t=weixin&from=ar'
    if 'm.kuwo.cn' in url:
        page_url=url
    else:
        page_url=page_url.format(url)
        
    s=requests.session()

    html=s.get(page_url,headers=headers,timeout=1)

    txt=html.text
    t=re.findall('window.__NUXT__=(.*?)\);',txt)[0]

    song_id=re.findall('\{id\:(.*?)\,',t)[1:]
    singer=re.findall('artist_name\:\"(.*?)\"',t)
    songs_list=re.findall('<div class="wordBody_title wordType" data-v-2519d9b3>(.*?)<\/div>',txt)
    title_name=re.findall(',name:"(.*?)"',t)[0]

    print("歌单名称:"+title_name)

    if len(song_id)>10:
        print("请不要把很多歌曲放置到歌单中，因为这会使控制台很混乱！")
        
    for i in range(len(song_id)):
        print("序号:{}\t{}\t{}".format(i+1,songs_list[i],singer[i]))


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
                url=kw.get_music_url(song_id[i])
                name=songs_list[i]+"-"+singer[i]
                download(url,name+".mp3")
                if pic or lrc:
                    print('此接口无法直接下载封面和歌词，您可以使用get-music '+songs_ls[i]+"，选择qq接口再做尝试！")
            except:
                print('\n\n\n——无法下载或解析歌曲！！！')
