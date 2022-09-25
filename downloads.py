from get_music import *
import sys
import os
from rich.console import Console
console=Console()
# kg，kw,wy,qq,migu,bd,1ting,fc,yc
def downloads():
    d={'kg':kugou.kugou(),
       'wy':netease.netease(),
       'qq':qq.qq(),
       'kw':kuwo.kuwo(),
       'migu':migu.migu(),
       'bd':baidu.baidu(),
       '1ting':oneting.oneting(),
       'yc':fivesing.fivesing('yc'),
       'fc':fivesing.fivesing('fc')}
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
            ln=i.split(',')
            if len(ln)==1:
                ln=i.split('，')
            else:
                console.print('[b green]请按照规范填写！在[b red]get-music -help[/]中查看规范！')
                sys.exit()
            ls.append(ln)

        console.print("[b green]正在搜索歌曲信息，注意该模式下我们不会返回任何数据进行交互") 
        for i in ls:
            try:
                api=d[i[-1]]
                with console.status("[b green]正在搜索:{}".format(i[0])):
                    name,singer,songid=api.search(i[0])
                if 'get_music_url' in dir(api):
                   get_url=True
                else:
                    get_url=False
                    
                if int(i[1]) > len(songid):
                    console.print('[b green]超出单次下载的最大范围或无法批量下载，可采用[b red]get-music[/]命令进行下载')
                    continue
                
                for j in range(int(i[1])):
                    fname=name[j]+"-"+singer[j]+".mp3"
                    if get_url==True:
                        url=api.get_music_url(songid[j])
                    else:
                        url=songid[j]
                    download.download(url,fname)
               
                    
            except:
                if name != None:
                    for k,l in enumerate(singer):
                        if i[1] in l:
                            fname=name[k]+"-"+singer[k]+".mp3"
                            if get_url==True:
                                url=api.get_music_url(songid[k])
                            else:
                                url=songid[k]
                            download.download(url,fname)
                else:
                        console.print("[b red]歌曲名称获取失败")
                continue
    except FileNotFoundError:
        console.print("[b green]您未创建“[b red]get_music.txt[/]”文件")
    except:
        console.print("[b green]未知错误，有可能是没有返回数据导致的，你可以使用get-music命令下载，或者联系维护者邮箱3101978435@qq.com")


