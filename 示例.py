'''
lzq-hopego   2023-8-12 示例基于get-music-lizhanqi v1.2.10
你可以使用本库对接你的pyqt tk等等，也可直接对接你的django and flask,也可在你的小程序中调用
'''
from get_music import kugou
from get_music import netease
from get_music import kuwo
from get_music import fivesing
from get_music import qq
from get_music import kuwo
from get_music import oneting
from get_music import baidu
from get_music import migu
from get_music import singbz

#初始化所有api
music_api={'kg':kugou.kugou(),
       'wy':netease.netease(),
       'qq':qq.qq(),
       'kw':kuwo.kuwo(),
       'mg':migu.migu(),
       'bd':baidu.baidu(),
       '1t':oneting.oneting(),
       'yc':fivesing.fivesing('yc'),
       'fc':fivesing.fivesing('fc'),
       'bz':singbz.singbz()}

# 每个api都有   search    get_music_url  get_music_pic get_music_lrc
'''
search   搜索，必须要先执行搜索，如果你有歌曲id可以直接get_music_url解析歌曲链接
    search(song_name,page_num=1) search接受两个参数，第一个关键字，第二个是页码

get_music_url 解析歌曲直链
    get_music_url(song_id) get_music_url接受一个参数，歌曲的id,此id可以通过search获取
    
get_music_pic 解析/下载  封面
    get_music_pic(num,return_url=False) get_music_pic接受两个参数，第一个是search返回的第几个
                                            假如需要返回的是第一个，就传1，第二个参数是否返回
                                            下载链接，默认不返回，如果返回则不自动下载
get_music_lrc 解析/下载  歌词
    get_music_lrc(num,return_url=False) get_music_lrc接受两个参数，第一个是search返回的第几个
                                            假如需要返回的是第一个，就传1，第二个参数是否返回
                                            下载链接，默认不返回，如果返回则不自动下载
'''
#现在实操利用字典中的api对象解析一首歌(无法解析收费或vip歌曲)


api=music_api['wy']
#使用search获取歌曲   search(song_name,page_num=1) 第一个参数必传,第二个参数缺省
songname,singername,songurl=api.search('大田后生仔')
print(songname,singername,songurl)
#search返回的三个列表，代表，歌曲名，歌手，歌曲id
#值得注意的是，这个歌曲id不管是不是下载链接，都不要直接使用，需要get_music_url解析一下
#songname ['大田後生仔', '大田後生仔',.....]
#singername ['林啟得', '丫蛋蛋',.....]
#songurl ['"http://m10.music.126.net/20230812095833/0a48dad120bf750982e5334fb6584d55/ymusic/0f0b/070b/020c/8a4dcf424e0a27fb4e085f58b242f2d2.mp3"',........]


#解析歌曲直链 我想解析丫蛋蛋的,而丫蛋蛋的是在列表的第二个，因此
song_url=api.get_music_url(songurl[1])
print(song_url)
#song_url='"http://m10.music.126.net/20230812095834/1ad1bdb711afea1a01f167a76020ed8f/ymusic/025d/060f/5552/57889b144f1e3beccb57b81709c72094.mp3"'


#现在解析歌词   此时需要传数字，数字是下标，将return_url=True，防止控制台输出
song_txt=api.get_music_lrc(1,return_url=True)
#此时返回的有可能是歌词，也有可能是歌词链接，此时你需要对歌词进行处理,如果不加return_url参数歌词将自动保存当前目录
#可以通过   'http' in song_txt  来处理是不是歌词链接
print(song_txt)
#和解析歌词一样，参数也保持一致
song_img=api.get_music_pic(1,return_url=True)
print(song_img)

#如何判断当前api是哪个平台的
print(api.api)   #网易云音乐
