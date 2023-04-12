import getopt
from rich.console import Console

con = Console()
def player_list(argv):
    opts=getopt.getopt(argv,"i:-l-p",["api="])[0]
##    print(opts)
    api=''
    url=''
    lrc=False
    pic=False
    for i in opts:
        if ('-i' in i) and (i[-1] !=''):
            url=i[-1]
        elif ('--api' in i) and (i[-1] !=''):
            api=i[-1]
        elif '-l' in i:
            lrc=True
        elif '-p' in i:
            pic=True
    ##print(url,api,lrc,pic)
    
    if api=='' and url=='':
        y_help()
    if url=='':
        url=con.input('\n\n[b green]请输入歌单链接或歌单id >>>')
        if url=='':
            con.print("[b green]您未输入歌单链接,程序自动退出")
            return
    if 'http' in url:
        if 'kugou.com' in url:
            api='kugou'
        elif '163.com' in url:
            api='netease'
        elif 'qq.com' in url:
            api='qq'
        elif 'kuwo.cn' in url:
            api='kuwo'
    if api=='' or (api not in ['kugou','netease','kuwo','qq']):
        api=con.input('[b green]请输入歌单的平台(kugou,kuwo,netease,qq) >>>')
        if api=='' or (api not in ['kugou','netease','kuwo','qq']):
            con.print("[b green]您未选择歌单平台,程序自动退出")
            return

    if api=='kugou':
        from get_music.kg_playerlist import kg_playerlist
        kg_playerlist(url,lrc=lrc,pic=pic)
    elif api=='netease':
        from get_music.wy_playerlist import wy_playerlist
        wy_playerlist(url,lrc=lrc,pic=pic)
    elif api=='qq':
        from get_music.qq_playerlist import qq_playerlist
        qq_playerlist(url,lrc=lrc,pic=pic)
    elif api=='kuwo':
        from get_music.kw_playerlist import kw_playerlist
        kw_playerlist(url,lrc=lrc,pic=pic)

def y_help():
        con.print('[b green]这是一个下载歌单列表歌曲的页面，以下是帮助文档')
        con.print('[yellow]你可以使用链接或输入id的方式来下载')
        con.print('[b green]酷狗的分享链接:[yellow]https://t1.kugou.com/[b red]97fwCebzGV3[/]')
        con.print('[b green]网易云的分享链接:[yellow]https://y.music.163.com/m/playlist?id=[b red]7101557391[/]&userid=1915127969&creatorId=1915127969')
        con.print('[b green]QQ音乐的分享链接:[yellow]https://y.qq.com/n/ryqq/playlist/[b red]7277950710[/]')
        con.print('[b green]酷我的分享链接:[yellow]http://m.kuwo.cn/newh5app/playlist_detail/[b red]3432572921[/]?t=plantform&from=ar')
        con.print('[b red]注意如果你使用id的方式进行的，请一定要指定api的名字,下面是示例：')
        con.print('[b red]使用链接则不需要跟api的,使用id下载则必要api,api的取值:kugou,kuwo,netease,qq')
        con.print('[b green][b yellow]使用分享链接下载歌单的命令:[/]get-music -playerlist -i https://y.qq.com/n/ryqq/playlist/7277950710')
        con.print('[b green][b yellow]使用id下载歌单的命令:[/]get-music -playerlist -i 7277950710 --api=qq')
        con.print('[b yellow][b red]-playlist[/]是打开下载歌单程序,第一个参数必须是它,[b red]-i[/]后要有一个空格,空格后要输入链接或id，如果是id后面就必须要跟api参数')
        
