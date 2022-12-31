import requests,re
from get_music.kugou import kugou
from get_music.download import download
import ast

def kg_playerlist(url,pic=False,lrc=False):
    kg=kugou()
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
             }

    page_url='https://t1.kugou.com/'
    if ('t1.kugou.com' in url) or ('wwwapi.kugou.com' in url):
        page_url=url
    else:
        page_url+=url
    
    s=requests.session()

    html=s.get(page_url,headers=headers,timeout=1)
    txt=html.text
    ls_d=re.findall('var dataFromSmarty = \[(.*?)\]',txt)[0]
    ls_d='['+ls_d+"]"
    lt=ast.literal_eval(ls_d)

    hashlist=[]
    album_id=[]
    song_name=[]
    singer=[]
    for i in lt:
        hashlist.append(i['hash'])
        album_id.append(i['album_id'])
        song_name.append(i['song_name'])
        singer.append(i['author_name'])
    if len(hashlist)>10:
        print("请不要把很多歌曲放置到歌单中，因为这会使控制台很混乱！")
    for i in range(len(hashlist)):
        print("序号:{}\t{}\t{}\t".format(i+1,song_name[i],singer[i]))
    songs=input('请选择您要下载哪一首歌，直接输入序号就行\n如需下载多个不连续的请用英文逗号分割即可，例如1,2\n如需下载多个连续的请用-分割即可，例如1-3\n如需全部下载，请输入all\n如果不需要下载多个，请直接输入序号就行:')
    if songs=='':
        print('\n\n\n——您未做出选择！程序即将自动退出！！！')
        return
    if songs=='all':
        song_list=range(len(song_name))
    elif '-' in songs:
        song_list=range(int(songs.split('-')[0]),int(songs.split('-')[-1])+1)
    else:
        song_list=songs.split(",")
        if len(song_list)==1:
            song_list=songs.split("，")

    for i in song_list:
        i=int(i)-1
        try:
            url=kg.get_music_url([hashlist[i],album_id[i]])
            name=song_name[i]+"-"+singer[i]
            download(url,name+".mp3")
            if pic or lrc:
                print('此接口无法直接下载封面和歌词，您可以使用get-music '+songs_ls[i]+"，选择qq接口再做尝试！")
        except:
            print('\n\n\n——无法下载或解析歌曲！！！')
