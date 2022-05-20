from get_music import kugou
from get_music import kuwo
from get_music import qq
from get_music import netease
from get_music import oneting
from get_music import baidu
from get_music import fivesing
from get_music import migu
import sys

def zhuti(songname='',p=False,l=False):
    if songname=='':
        songname=input('请输入您想听的歌曲，我来帮您下载：\n')
    if songname=='':
        print("您没有输入歌曲，程序结束！")
        sys.exit()
    try:
            fs=eval(input('请选择下载渠道\n1，酷狗音乐\t2，网易云音乐\t3，QQ音乐\t4，酷我音乐\t\n5,咪咕音乐\t6,百度音乐(千千静听)\t7,一听\t8,5sing原唱\n9,5sing翻唱\n输入下载渠道的序号就可以，想在酷狗端口下载就输入“1”就可以，依次类推\n请输入下载序号:'))
    except:
            print("您输入的接口有误！")

    d={1:kugou.kugou(p,l),
       2:netease.netease(p,l),
       3:qq.qq(p,l),
       4:kuwo.kuwo(p,l),
       5:migu.migu(p,l),
       6:baidu.baidu(p,l),
       7:oneting.oneting(p,l),
       8:fivesing.fivesing('yc'),
       9:fivesing.fivesing('fc')}
    try:
        api=d[fs]
    except:
        print("您输入的内容有些不合程序请检查后重试")
    try:
        api.search(songname)
    except:
        print("无法返回数据或接口失效，可联系维护者，邮箱：3101978435@qq.com")
    try:
        api.prints()
    except:
        print("出现未知错误,有可能是您一直在下载导致的强制断开连接，或接口无返回值，请及时联系维护者3101978435@qq.com")

def main_help():    
    txt='''
    -help\t查看帮助文档\n
    -version\t查看当前版本\n
    -t\t打开gui窗口下载,使用的框架是python自带的tkinter\n
    -r\t(注意该功能可能会不稳定，但是不会给您的计算机照成危害)在
    创建名为get_music.txt的文件，文件内容的格式为"歌曲名 下载序号 下载渠
    道"歌曲名的地方也可以是歌手，下载序号其实是下载几首歌3的话就会下载3
    个不同版本的，下载渠道目前全支持，他们的缩写为：kg，kw,wy,qq,migu,bd,1ting,fc,yc\n文件内容示范:
    \n\n爱人错过 1 kg\n11 1 kg\n\n
    每一行为一组歌曲信息，想下载多个歌曲就换行
    按照示范的再写一组\n\n关于该脚本的使用：\n
    1.在dos命令行（或其他系统的命令行）的随意目录下，敲击“get-music”进入该脚本的启动页面\n
    \t\t1.1,“get-music -v”查看当前版本，同时程序也会检查一下新版本的版本号是否更新看您个人\n
    \t\t1.2,“get-music -l”下载歌曲的同时也下载歌曲的歌词，直接敲就行了后面的搜索步骤和“get-music”的操作基本一致\n
    \t\t1.3,“get-music -p”下载歌曲的同时也下载歌曲的封面，这九个接口中只有“1ting”不支持下载歌词，其他的功能都能正常使用\n
    \t\t1.4,“get-music -lp”或者“get-music -pl”它俩都是同一个意思，下载歌曲的同时也下载封面和歌词\n
    \t\t1.5，“get-music -h”查看帮助文档\n
    2.一般的第一个步骤会提醒你要下载什么歌曲，这是至于要输入歌曲的就行了
    3.这个步骤程序会让你选择一个搜索歌曲的接口（平台），直接输入接口的序号即可，
    关于接口（平台）说明，只有咪咕音乐的部分歌曲支持flac格式的，
    并且在酷狗等音乐接口（平台）可能会下载到试听的部分（这说明该音乐只有vip
    才能下载，本脚本暂不支持下载vip歌曲和携带vip账号）——如果用酷狗那就直接输入
    “1”并按下回车
    4.这个时候程序就该返回数据了，会有20条（不出意外的情况下，
    当然也跟接口（平台）的返回的数据有关），同样的输入序号即可下载，可以直接输
    入“1”进行下载
    5.执行下载中会有进度条提示，文件越大音质越好\n
    关于本程序：\n
    \t禁止将本脚本用于商业用途，如产生法律纠纷与本人无关，
    \t如有侵权，请联系我删除。
    作者兼维护者邮箱：3101978435@qq.com'

'''
    print(txt)
    print("本程序仅用作学习用途，禁止将本脚本用于商业用途，如产生法律纠纷与本人无关，如有侵权，请联系我删除。")
    print("作者邮箱：3101978435@qq.com")
    print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')

def main():
    try:
            if len(sys.argv[:])==1:
                zhuti()
                sys.exit()
            if sys.argv[1][0]=="-":
                if sys.argv[1] in ['-h','-help']:
                    main_help()
                elif sys.argv[1] in ['-version','-v','-V']:
                    print("\n当前版本为v0.0.58\n")
                    try:
                        from get_music import ver
                        ver.ver()
                    except:
                        print("获取最新版本信息失败！")
                elif sys.argv[1] in ['-read','-r','-R']:
                    pass
                    from get_music import downloads
                    downloads.downloads()
                elif sys.argv[1] =='-l':
                    zhuti(l=True)
                elif sys.argv[1] =='-p':
                    zhuti(p=True)
                elif sys.argv[1] in ['-lp','-pl']:
                    zhuti(l=True,p=True)
                elif sys.argv[1] in ['-t','-T']:
                    try:
                        from get_music import gui
                    except:
                        print('您的设备暂不支持该命令！')
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


