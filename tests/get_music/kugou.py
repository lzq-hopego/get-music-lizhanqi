import requests,json
from get_music import download

headers={
        'UserAgent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
        'Referer' : 'http://m.kugou.com/rank/info/8888',
        'Cookie' : 'UM_distinctid=161d629254c6fd-0b48b34076df63-6b1b1279-1fa400-161d629255b64c; kg_mid=cb9402e79b3c2b7d4fc13cbc85423190; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1523818922; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1523819865; Hm_lvt_c0eb0e71efad9184bda4158ff5385e91=1523819798; Hm_lpvt_c0eb0e71efad9184bda4158ff5385e91=1523820047; musicwo17=kugou'
        }

def get_songs(url):
    res=requests.get(url,headers=headers,timeout=1)
    return json.loads(res.text)


def get_songs_url(d):
    songs_list=d['data']['info']
    songs_url=[]
    songname=[]
    singername=[]
    for i in songs_list:
        l=[]
        songname.append(i['songname'])
        singername.append(i['singername'])
        l.append(i["hash"])
        l.append(i["album_id"])
        songs_url.append(l)
    return songs_url,songname,singername
def get_songs_urls(ls):
        song_list=[]
        for i in ls:
            url="https://www.kugou.com/yy/index.php?r=play/getdata&hash="+i[0]+"&album_id="+str(i[1]) 
            d=get_songs(url)
            l=[]
            l.append(d['data']['song_name'])
            l.append(d['data']['author_name'])
            l.append(d["data"]["play_url"])
            song_list.append(l)
        return song_list
def printf(songs_url,songname,singername):
    for i in range(len(songs_url)):
        print("序号:"+str(i+1)+'\t'+songname[i]+"——"+singername[i])
    a=input("请选择需要下载的歌曲序号(不支持多个同时下载)：")
    try:
        a=int(a)-1
        
        ls=[]
        ls.append(songs_url[a])
##        print(ls)
        lt=get_songs_urls(ls)
        
        return lt
    except:
        print("序号输入错误——程序出错啦")

def kugou(keyword):
##    keyword='爱人错过'
    if keyword:
        try:
            url="http://mobilecdngz.kugou.com/api/v3/search/song?tag=1&tagtype=%E5%85%A8%E9%83%A8&area_code=1&plat=0&sver=5&api_ver=1&showtype=20&version=8969&keyword="+keyword
            d=get_songs(url)
            songs_url,songname,singername=get_songs_url(d)
            songurl=printf(songs_url,songname,singername)
            name=songurl[0][1]+"唱的"+songurl[0][0]
            fname=songurl[0][0]+"-"+songurl[0][1]+".mp3"
            url=songurl[0][-1]
            download.download(url,fname,ouput=True)
            print("\n"+name+"已保存至当前目录下")
            print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
        except:
            print("未知错误，有可能是没有返回数据导致的，你可以使用get-music命令下载，或者联系维护者邮箱3101978435@qq.com")



        
