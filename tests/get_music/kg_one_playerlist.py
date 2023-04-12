import requests,json
import urllib.parse
from get_music.kugou import kugou
from get_music.download import download

def kg_one_playerlist(url,pic=False,lrc=False):
    kg=kugou()
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
                 }

    s=requests.session()

    html=s.get(url,headers=headers,timeout=1)
    txt=html.text
    d=txt.split('var nData=')[-1].split('\n')[0][:-1]

    dd=json.loads(d)


    hashlist=[]
    album_id=[]
    song_name=[]
    singer=[]
    size=[]
    user_name=''
    music_sheet_name=''


    for i in dd['songs']:
        hashlist.append(i['hash'])
        album_id.append(i['audio_id'])
        song_name.append(urllib.parse.unquote(i['name'].split('-')[-1].strip()))
        singer.append(urllib.parse.unquote(i['singerinfo'][0]['name']))
        size.append(str(round(i['size']/1024/1024,2))+'MB')
    if len(hashlist)>10:
            print("请不要把很多歌曲放置到歌单中，因为这会使控制台很混乱！")
    print('歌单创建者:{}\t歌单名称:{}'.format(dd['listinfo']['list_create_username'],dd['listinfo']['name']))
    print('序号\t歌名\t歌手\t歌曲大小')
    for i in range(len(hashlist)):
        print("序号:{}\t{}\t{}\t{}".format(i+1,song_name[i],singer[i],size[i]))
    songs=input('请选择您要下载哪一首歌，直接输入序号就行\n如需下载多个不连续的请用英文逗号分割即可，例如1,2\n如需下载多个连续的请用-分割即可，例如1-3\n如需全部下载，请输入all\n如果不需要下载多个，请直接输入序号就行:')
    if songs=='':
        print('\n\n\n——您未做出选择！程序即将自动退出！！！')

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
            url=kg.get_music_url([hashlist[i],album_id[i]])
            name=song_name[i]+"-"+singer[i]
            download(url,name+".mp3")
            if pic or lrc:
                print('此接口无法直接下载封面和歌词，您可以使用get-music '+songs_ls[i]+"，选择qq接口再做尝试！")
        except:
            print('\n\n\n——无法下载或解析歌曲！！！')
