from get_music import kugou
from get_music import netease
from get_music import qq
from get_music import kuwo
from get_music import migu
from get_music import baidu
from get_music import oneting
from get_music import fivesing
from get_music import singbz
from get_music import download
from rich.console import Console
from rich.table import Table
import sys

console = Console()
txt='''
                __                                  __        
   ____   _____/  |_            _____  __ __  _____|__| ____  
  / ___\_/ __ \   __\  ______  /     \|  |  \/  ___/  |/ ___\ 
 / /_/  >  ___/|  |   /_____/ |  Y Y  \  |  /\___ \|  \  \___ 
 \___  / \___  >__|           |__|_|  /____//____  >__|\___  >
/_____/      \/                     \/           \/        \/

'''
console=Console()
console.print(txt,style='bold green')

def zhuti(songname = '',p = False,l = False):
    d={1:kugou.kugou(p,l),
       2:netease.netease(p,l),
       3:qq.qq(p,l),
       4:kuwo.kuwo(p,l),
       5:migu.migu(p,l),
       6:baidu.baidu(p,l),
       7:oneting.oneting(p,l),
       8:fivesing.fivesing('yc',p,l),
       9:fivesing.fivesing('fc',p,l),
       10:singbz.singbz(p,l)}
    if songname == '':
        songname = console.input('[b green]请输入您想听的歌曲，我来帮您下载\n[b red]>[/]')
    if songname == '':
        console.print("[b red]您没有输入歌曲，程序结束！")
        sys.exit()
    try:
            fs = eval(console.input('[b green]请选择下载渠道\n[b red]1，酷狗音乐\t2，网易云音乐\t3，QQ音乐\t4，酷我音乐\t\n5,咪咕音乐\t6,百度音乐(千千静听)\t7,一听\t8,5sing原唱\n9,5sing翻唱\t10,5sing伴奏\n[/]输入下载渠道的序号就可以，想在酷狗端口下载就输入“[blue]1[/]”就可以，依次类推\n请输入下载序号\n[b red]>[/]'))
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
    prints(api)


def main_help():    
    txt='''
    关于本脚本的使用：\n
    \t\t1.1,“[b red]get-music -v[/]”查看当前版本，同时程序也会检查一下新版本的版本号是否更新看您个人\n
    \t\t1.2,“[b red]get-music -l[/]”下载歌曲的同时也下载歌曲的歌词，直接敲就行了后面的搜索步骤和“get-music”的操作基本一致\n
    \t\t1.3,“[b red]get-music -p[/]”下载歌曲的同时也下载歌曲的封面，这十个接口中只有“1ting”不支持下载歌词，其他的功能都能正常使用\n
    \t\t1.4,“[b red]get-music -lp[/]”或者“get-music -pl”它俩都是同一个意思，下载歌曲的同时也下载封面和歌词\n
    \t\t1.5,“[b red]get-music -t[/]”打开本脚本的GUI界面，相比命令行对小白更友好\n
    \t\t1.6，“[b red]get-music -help[/]”查看帮助文档\n
    \t\t1.7，“[b red]get-music -hot[/]”查看热歌榜单\n
    \t\t1.8，“[b red]get-music -r[/]”批量下载\n
    \t\t1.9，“[b red]get-music -s[/]”在网络中查找歌曲的网盘链接\n
    \t\t1.10, “[b red]get-music -playerlist[/]”下载歌单中的歌曲,只支持,酷狗,网易云,QQ,酷我,四个平台\n
    \t\t1.11“[b red]get-music -ip[/]”查找本程序的最新版本，并返回当前网络的公网地址\n
    get-music -r [b green]批量下载[/](注意该功能可能会不稳定，但是不会给您的计算机照成危害)在创建名为get_music.txt的文件，\n
    文件内容的格式为“[b red]歌曲名,下载序号/歌手,下载渠道[/]”歌曲名的地方也可以是歌手，
    \n\t\t下载序号其实是下载几首歌3的话就会下载3个不同版本的，如果填写的是歌手则下载含有您输入的歌手相匹配的歌曲
    \n\t\t下载渠道目前全支持，他们的缩写为：kg，kw,wy,qq,migu,bd,1ting,fc,yc,bz\n文件内容示范:
    \n\n\t\t[b red]爱人错过，告五人，kg\n\t\t[b red]11，1，kg\n\n
    每一行为一组歌曲信息，想下载多个歌曲就换行,按照示范的再写一组，其中fc,yc,bz的数据来自5sing接口\n\n
   

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
                    try:
                        top.prints()
                    except:
                        console.print('[b red]接口无反应您可重试！')
                elif sys.argv[1] == '-playerlist':
                    try:
                        from get_music.playerlist import player_list
                        player_list(sys.argv[2:])
                    except:
                        sys.exit()
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



def prints(self):
        name=self.songname
        singer=self.singername
        song_url=self.songs_url
        table = Table(style='purple',title='[b green]get-music-lizhanqi')
        table.add_column('[red]序号',justify='center')
        table.add_column('[yellow]歌曲名',justify='center',overflow=True)
        table.add_column('[blue]歌手',justify='center',overflow=True)
        table.add_column('[green]平台',justify='center',overflow=True)
        for i in range(0,len(name)):
            table.add_row('[b red]'+str(i+1),'[yellow]'+name[i],'[blue]'+singer[i],'[b green]'+self.api,end_section=True)
        console.print(table)
        songs=console.input('[b green]请选择您要下载哪一首歌，直接输入[b red]序号[/]就行\n如需下载多个不连续的请用[b red]英文逗号[/]分割即可，[b blue]例如1,2[/]\n如需下载多个连续的请用[b red]-[/]分割即可，[b blue]例如1-3[/]\n如需全部下载，请输入[b blue]all[/]\n输入[b red]0[/]可以继续搜索[b red]下一页[/]\n输入[b red]-1[/]可以继续搜索[b red]上一页[/]\n如果不需要下载多个，请直接输入序号就行:')
        if songs=='':
            console.print('[b red]\n\n\n——您未做出选择！程序即将自动退出！！！')
            return
        elif songs=='0':
            self.search(self.song_name,page=self.page+1)
            
            return prints(self)
        elif songs=='-1':
            if self.api != '网易云音乐' or self.page-1==-1:
                if self.page-1<=0:
                    console.print("[b red]\n已经是第一页啦！")
                    return
            
            self.search(self.song_name,page=self.page-1)
            return prints(self)
        if songs=='all':
            song_list=range(len(self.songname))
        elif '-' in songs:
            song_list=range(int(songs.split('-')[0]),int(songs.split('-')[-1])+1)
        else:
            song_list=songs.split(",")
            if len(song_list)==1:
                song_list=songs.split("，")
        for i in song_list:
            try:
                i=int(i)-1
            except ValueError:
                console.print("[b red]您输入的序号有问题，请用仔细检查谢谢！")
                continue
            try:
                singername=singer[i]
                if self.api=='5Sing伴奏':
                    singername=singer[i].split('-')[0]
                fname=name[i]+"-"+singername+".mp3"
                url=song_url[i]
                songurl=self.get_music_url(url)
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
                download.download(songurl,fname,ouput=True)
                console.print('[b red]'+singer[i]+'唱的'+name[i]+'下载完成啦！')
                console.print("[b red]已保存至当前目录下")
            except IndexError:
                console.print("[b red]您输入的序号不在程序给出的序号范围！")
                continue
        console.print('[b green]\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
