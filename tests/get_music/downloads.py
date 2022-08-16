from get_music import download
from get_music import kugou
from get_music import kuwo
from get_music import qq
from get_music import netease
from get_music import oneting
from get_music import baidu
from get_music import fivesing
from get_music import migu
from rich.console import Console
##from get_music import *
console=Console()
def downloads():
    d={1:kugou.kugou(),
       2:netease.netease(),
       3:qq.qq(),
       4:kuwo.kuwo(),
       5:migu.migu(),
       6:baidu.baidu(),
       7:oneting.oneting(),
       8:fivesing.fivesing('yc'),
       9:fivesing.fivesing('fc')}
    try:
        try:
            fo=open("get_music.txt",'r',encoding='utf-8')
            txt=fo.read().split("\n")
            fo.close()
        except:
            fo=open("get_music.txt",'r')
            txt=fo.read().split("\n")
            fo.close()
        ls=[]
        for i in txt:
            ls.append(i.split())

        console.print("[b green]正在搜索歌曲信息，注意该模式下我们不会返回任何数据进行交互") 
        for i in ls:
            try:
                
                songname,way=i[0],i[-1]
                songnum=int(i[1])
                if songnum>20:
                    console.print("[b red]第二列的序号出错啦")
                    sys.exit()
                if way=='kg':
                    api=d[1]
                    api.search(i[0])
                    songname=api.songname
                    singername=api.singername
                    songid=api.songs_url
                    
                    for i in range(songnum):
                        fname=songname[i]+"-"+singername[i]+".mp3"            
                        url=api.get_music_url(songid[i])
                        download.download(url,fname)
                if way=='wy':
                    api=d[2]
                    api.search(i[0])
                    songname=api.song_name
                    singername=api.songer_name
                    songid=api.song_id
                    for i in range(songnum):
                            fname=songname[i]+"-"+singername[i]+".mp3"  
                            download.download(songid[i],fname)
                if way=='qq':
                    api=d[3]
                    api.search(i[0])
                    songname=api.song_name
                    singername=api.singer_name
                    songid=api.song_url
                    for i in range(songnum):
                        fname=songname[i]+"-"+singername[i]+".mp3"            
                        url=api.get_music_url(songid[i])
                        download.download(url,fname)
                if way=='kw':
                    api=d[4]
                    api.search(i[0])
                    songname=api.musicNames
                    singername=api.singer
                    songid=api.song_url
                    for i in range(songnum):
                        fname=songname[i]+"-"+singername[i]+".mp3"         
                        url=api.get_music_url(songid[i])
                        download.download(url,fname)
                if way=='migu':
                    api=d[5]
                    api.search(i[0])
                    songname=api.songname
                    singername=api.singer
                    songid=api.songurl
                    for i in range(songnum):
                            fname=songname[i]+"-"+singername[i]+".mp3"
                            download.download(songid[i],fname)
                if way=='bd':
                    api=d[6]
                    api.search(i[0])
                    songname=api.sings
                    singername=api.song_name
                    songid=api.tsids
                    for i in range(songnum):
                        fname=songname[i]+"-"+singername[i]+".mp3"         
                        url=api.get_music_url(songid[i])
                        download.download(url,fname)
                if way=='1ting':
                    api=d[7]
                    api.search(i[0])
                    songname=api.song_name
                    singername=api.singer_name
                    songid=api.song_url
                    for i in range(songnum):
                        fname=songname[i]+"-"+singername[i]+".mp3"            
                        download.download(songid[i],fname)
                if way=='yc':
                    api=d[8]
                    api.search(i[0])
                    songname=api.song_name
                    singername=api.singer_name
                    songid=api.song_id
                    for i in range(songnum):
                        fname=songname[i]+"-"+singername[i]+".mp3"         
                        url=api.get_music_url(songid[i])
                        download.download(url,fname)
                if way=='fc':
                    api=d[9]
                    api.search(i[0])
                    songname=api.song_name
                    singername=api.singer_name
                    songid=api.song_id
                    for i in range(songnum):
                        fname=songname[i]+"-"+singername[i]+".mp3"         
                        url=api.get_music_url(songid[i])
                        download.download(url,fname)
                
            except:
                console.print("[b red]歌曲名称获取失败")
                break
    except FileNotFoundError:
        console.print("[b red]您未创建“get_music.txt”文件")
    except:
        console.print("[b red]未知错误，有可能是没有返回数据导致的，你可以使用get-music命令下载，或者联系维护者邮箱3101978435@qq.com")
