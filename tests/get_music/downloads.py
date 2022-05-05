from get_music import download
from get_music import kuwo
from get_music import getkugou as kugou
from get_music import netease
from get_music import qq

def downloads():
    try:
        fo=open("get_music.txt",'r',encoding='utf-8')
        txt=fo.read().split("\n")
        fo.close()
        ls=[]
        for i in txt:
            ls.append(i.split())

        print("正在搜索歌曲信息，注意该模式下我们不会返回任何数据进行交互") 
        for i in ls:
            try:
                songname,way=i[0],i[-1]
                songnum=int(i[1])
                if way=='kw':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=kuwo.kuwo(songname)
                    print("搜索完成，开始下载...")
                    for i in range(0,songnum):
                        fname=song_name[i]+"-"+singers[i]+".mp3"
                        url=song_url[i]
                        download.download(url,fname)
                if way=='kg':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=kugou.kugou(songname)
                    print("搜索完成，开始下载...")
                    for i in range(0,songnum):
                        fname=song_name[i]+"-"+singers[i]+".mp3"
                        url=song_url[i]
                        download.download(url,fname)
                if way=='qq':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=qq.qq(songname)
                    print("搜索完成，开始下载...")
                    for i in range(0,songnum):
                        fname=song_name[i]+"-"+singers[i]+".mp3"
                        url=song_url[i]
                        download.download(url,fname)
                if way=='wy':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=netease.netease(songname)
                    print("搜索完成，开始下载...")
                    for i in range(0,songnum):
                        fname=song_name[i]+"-"+singers[i]+".mp3"
                        url=song_url[i]
                        download.download(url,fname)
            except ValueError:
                songnum=i[1]
                if way=='kw':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=kuwo.kuwo(songname)
                    print("搜索完成，开始下载...")
                    for i,j in enumerate(singers):
                        if songnum in j:
                            fname=song_name[i]+"-"+singers[i]+".mp3"
                            url=song_url[i]
                            download.download(url,fname)
                if way=='kg':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=kugou.kugou(songname)
                    print("搜索完成，开始下载...")
                    for i,j in enumerate(singers):
                        if songnum in j:
                            fname=song_name[i]+"-"+singers[i]+".mp3"
                            url=song_url[i]
                            download.download(url,fname)
                if way=='qq':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=qq.qq(songname)
                    print("搜索完成，开始下载...")
                    for i,j in enumerate(singers):
                        if songnum in j:
                            fname=song_name[i]+"-"+singers[i]+".mp3"
                            url=song_url[i]
                            download.download(url,fname)
                if way=='wy':
                    print("正在搜索："+songname)
                    song_name,singers,song_url=netease.netease(songname)
                    print("搜索完成，开始下载...")
                    for i,j in enumerate(singers):
                        if songnum in j:
                            fname=song_name[i]+"-"+singers[i]+".mp3"
                            url=song_url[i]
                            download.download(url,fname)

            except:
                print("歌曲名称获取失败")
                break
    except FileNotFoundError:
        print("您未创建“get_music.txt”文件")
    except:
        print("未知错误，有可能是没有返回数据导致的，你可以使用get-music命令下载，或者联系维护者邮箱3101978435@qq.com")
