import requests,re
from get_music.qq import qq
from get_music.download import download



def qq_playerlist(url,pic=False,lrc=False):
    q=qq()
    '''8629968090'''

    s=requests.session()

    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
             }
    page_url='https://y.qq.com/n/ryqq/playlist/'
    if 'y.qq.com' in url:
        page_url=url
    else:
        page_url+=url
    html=s.get(page_url,headers=headers,timeout=1)

    txt=html.text
    user_name=re.findall('<a title="(.*?)" class="data__singer_txt" href=".*">',txt)[0]

    ul=re.findall('<ul class="songlist__list">(.*?)<\/ul>',txt)[0]

    li=re.findall('<li>(.*?)<\/li>',ul)
    songs_ls=[]
    singer=[]
    songid=[]

    for i in li:
        lt=re.findall('<a title="(.*?)" href="/n/ryqq/songDetail/(.*?)">.*<\/a>.*<a class="playlist__author" title=".*" href="/n/ryqq/singer/.*">(.*?)<\/a>',i)
        songs_ls.append(lt[0][0])
        singer.append(lt[0][2])
        songid.append(lt[0][1])


    print('本歌单由“'+user_name+"”创建。")
    print("平台限制，只能打印出10首哦")

    for i in range(len(songid)):
            print("序号:{}\t{}\t{}".format(i+1,songs_ls[i],singer[i]))
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
            url=q.get_music_url(songid[i])
            name=songs_ls[i]+"-"+singer[i]
            download(url,name+".mp3")
            if pic or lrc:
                print('此接口无法直接下载封面和歌词，您可以使用get-music '+songs_ls[i]+"，选择qq接口再做尝试！")
        except:
            print('\n\n\n——无法下载或解析歌曲！！！')
