from get_music import kugou
from get_music import kuwo
from get_music import qq
from get_music import netease
from get_music import oneting
from get_music import baidu
from get_music import fivesing
from get_music import migu
import sys

def zhuti(songname=''):
    if songname=='':
        songname=input('请输入您想听的歌曲，我来帮您下载：\n')
    if songname=='':
        print("您没有输入歌曲，程序结束！")
        sys.exit()
    try:
            fs=eval(input('请选择下载渠道\n1，酷狗音乐\t2，网易云音乐\t3，QQ音乐\t4，酷我音乐\t\n5,咪咕音乐\t6,百度音乐(千千静听)\t7,一听\t8,5sing原唱\n9,5sing翻唱\n输入下载渠道的序号就可以，想在酷狗端口下载就输入“1”就可以，依次类推\n请输入下载序号:'))
    except:
            print("您输入的接口有误！")

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
        api=d[fs]
        api.search(songname)
        api.prints()
    except:
        print("出现未知错误,有可能是您一直在下载导致的强制断开连接，或接口无返回值，请及时联系维护者3101978435@qq.com")

def main_help():
    print()
    print("本程序直接在命令行运行“get-music”即可开启程序的下载入口")
    print("支持快捷下载get-music [songname],例如：get-music 爱人错过")
    print("本程序暂不支持 ‘import get_music’ 呢")
    print("本程序支持六个音乐平台，后续会持续更新和维护")
    txt='-help\t查看帮助文档\n-version\t查看当前版本\n-r\t(注意该功能可能会不稳定，但是不会给您的计算机照成危害)在创建名为get_music.txt的文件，文件内容的格式为"歌曲名 下载序号 下载渠道"歌曲名的地方也可以是歌手，下载序号其实是下载几首歌3的话就会下载3个不同版本的，下载渠道目前只支持kg，kw,wy,qq\n文件内容示范:\n爱人错过 1 kg\n11 1 kg\n每一行为一组歌曲信息，想下载多个歌曲就换行按照示范的再写一组n\n关于该脚本的使用：\n 1.在dos命令行（或其他系统的命令行）的随意目录下，敲击“get-music”进入该脚本的启动页面\n 2.一般的第一个步骤会提醒你要下载什么歌曲，这是至于要输入歌曲的就行了\n 3.这个步骤程序会让你选择一个搜索歌曲的接口（平台），直接输入接口的序号即可，关于接口（平台）说明，只有咪咕音乐的部分歌曲支持flac格式的，并且在酷狗等音乐接口（平台）可能会下载到试听的部分（这说明该音乐只有vip才能下载，本脚本暂不支持下载vip歌曲和携带vip账号）——如果用酷狗那就直接输入“1”并按下回车\n 4.这个时候程序就该返回数据了，会有19条（不出意外的情况下，当然也跟接口（平台）的返回的数据有关），同样的输入序号即可下载，可以直接输入“1”进行下载\n 5.1在百度音乐接口（平台）会出现让你确定yes或no的提示，这个提示表示是否下载歌词和封面，目前六个接口中仅有百度接口支持，如何不想下载直接回车（或者输入no）\n 5.2执行下载中会有进度条提示，文件越大音质越好\n关于本程序：\n禁止将本脚本用于商业用途，如产生法律纠纷与本人无关，如有侵权，请联系我删除。\n作者兼维护者邮箱：3101978435@qq.com'
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
                    print("\n当前版本为v0.0.55\n")
                    try:
                        from get_music import ver
                        ver.ver()
                    except:
                        print("获取最新版本失败！")
                elif sys.argv[1] in ['-read','-r','-R']:
                    pass
                    from get_music import downloads
                    downloads.downloads()
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


