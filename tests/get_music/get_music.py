from get_music import kugou
from get_music import kuwo
from get_music import qq
from get_music import netease
from get_music import oneting
from get_music import baidu
from get_music import fivesing
from get_music import migu
from rich.console import Console
import sys

console = Console()
def zhuti(songname = '',p = False,l = False):
    
    d={1:kugou.kugou(p,l),
       2:netease.netease(p,l),
       3:qq.qq(p,l),
       4:kuwo.kuwo(p,l),
       5:migu.migu(p,l),
       6:baidu.baidu(p,l),
       7:oneting.oneting(p,l),
       8:fivesing.fivesing('yc',p,l),
       9:fivesing.fivesing('fc',p,l)}
    
    if songname == '':
        songname = console.input('[b green]请输入您想听的歌曲，我来帮您下载\n[b red]>[/]')
    if songname == '':
        console.print("[b red]您没有输入歌曲，程序结束！")
        sys.exit()
    try:
            fs = eval(console.input('[b green]请选择下载渠道\n[b red]1，酷狗音乐\t2，网易云音乐\t3，QQ音乐\t4，酷我音乐\t\n5,咪咕音乐\t6,百度音乐(千千静听)\t7,一听\t8,5sing原唱\n9,5sing翻唱\n[/]输入下载渠道的序号就可以，想在酷狗端口下载就输入“[blue]1[/]”就可以，依次类推\n请输入下载序号\n[b red]>[/]'))
    except:
            console.print("[b red]您输入的接口有误！")
    try:
        api=d[fs]
    except:
        console.print("[b red]您输入的内容有些不合程序请检查后重试")
        return
    try:
        with console.status("[b green]搜索中..."):
            api.search(songname)
    except:
        console.print("[b red]无法返回数据或接口失效,或者您的网络未连接，如果还未解决可联系维护者邮箱：3101978435@qq.com")
        return
    try:
        api.prints()
    except:
        console.print("[b red]出现未知错误,有可能是您一直在下载导致的强制断开连接，或接口无返回值，请及时联系维护者3101978435@qq.com")
        return

def main_help():    
    txt='''
    关于本脚本的使用：\n
    \t\t1.1,“[b red]get-music -v[/]”查看当前版本，同时程序也会检查一下新版本的版本号是否更新看您个人\n
    \t\t1.2,“[b red]get-music -l[/]”下载歌曲的同时也下载歌曲的歌词，直接敲就行了后面的搜索步骤和“get-music”的操作基本一致\n
    \t\t1.3,“[b red]get-music -p[/]”下载歌曲的同时也下载歌曲的封面，这九个接口中只有“1ting”不支持下载歌词，其他的功能都能正常使用\n
    \t\t1.4,“[b red]get-music -lp[/]”或者“get-music -pl”它俩都是同一个意思，下载歌曲的同时也下载封面和歌词\n
    \t\t1.5,“[b red]get-music -t[/]”打开本脚本的GUI界面，相比命令行对小白更友好\n
    \t\t1.6，“[b red]get-music -help[/]”查看帮助文档\n
    \t\t1.7，“[b red]get-music -hot[/]”查看热歌榜单\n
    \t\t1.8，“[b red]get-music -r[/]”批量下载\n
    \t\t1.9，“[b red]get-music -s[/]”在网络中查找歌曲的网盘链接\n
    \t\t1.10“[b red]get-music -ip[/]”查找本程序的最新版本，并返回当前网络的公网地址\n
    get-music -r [b green]批量下载[/](注意该功能可能会不稳定，但是不会给您的计算机照成危害)在创建名为get_music.txt的文件，\n
    文件内容的格式为“[b red]歌曲名,下载序号/歌手,下载渠道[/]”歌曲名的地方也可以是歌手，
    \n\t\t下载序号其实是下载几首歌3的话就会下载3个不同版本的，如果填写的是歌手则下载含有您输入的歌手相匹配的歌曲
    \n\t\t下载渠道目前全支持，他们的缩写为：kg，kw,wy,qq,migu,bd,1ting,fc,yc\n文件内容示范:
    \n\n\t\t[b red]爱人错过，告五人，kg\n\t\t[b red]11，1，kg\n\n
    每一行为一组歌曲信息，想下载多个歌曲就换行,按照示范的再写一组\n\n
   

'''
    console.print(txt,style = 'b green')
    console.print("[b red]本程序仅用作学习用途，禁止将本脚本用于商业用途，如产生法律纠纷与本人无关，如有侵权，请联系我删除。")
    console.print("[b red]作者邮箱：3101978435@qq.com")
    console.print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！',style = 'b green')

def main():
    try:
            if len(sys.argv[:])==1:
                zhuti()
                sys.exit()
            if sys.argv[1][0]=="-":
                if sys.argv[1] in ['-h','-help']:
                    main_help()
                elif sys.argv[1] in ['-version','-v','-V']:
                    from get_music import ver
                    ver.ver(ip=False)
                    
                elif sys.argv[1] in ['-read','-r','-R']:
                    pass
                    from get_music import downloads
                    downloads.downloads()
                elif sys.argv[1]=='-ip':
                    from get_music import ver
                    ver.ver()
                elif sys.argv[1] =='-l':
                    zhuti(l=True)
                elif sys.argv[1] =='-p':
                    zhuti(p=True)
                elif sys.argv[1] in ['-lp','-pl']:
                    zhuti(l=True,p=True)
                elif sys.argv[1] in ['-hot','-hotmusic','-top']:
                    from get_music import top
                elif sys.argv[1] in ['-t','-T']:
                    try:
                        from get_music import gui
                    except:
                        console.print('[b red]您的设备暂不支持该命令！')
                elif sys.argv[1] in ['-s','-S']:
                    try:
                        from get_music.zhidao import search
                        search()
                    except:
                        console.print('[b red]很抱歉运行失败，您可以尝试升级新版本！')
                else:
                    main_help()
            elif sys.argv[1]=="help":
                main_help()
            else:
                q=sys.argv[1]
                zhuti(q)
                sys.exit()
    except:
            pass


