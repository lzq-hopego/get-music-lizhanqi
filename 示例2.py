#如何通过get-music-lizhanqi获取各个平台的热歌榜单

#需要导入top模块

#top模块提供了四个平台
#kg
#kw     不建议使用，因为他的数据总是出问题,必须使用的话就像kg一样，就是获取歌曲id在调用对应的模块进行解析,如果无法解析可以重新构建一个搜索(search方法)重新解析
#wy
#qq
#直接调用,返回的参数分别为    歌名,歌手,id    其中kuwo 只返回  歌名,歌手

from get_music import top


#获取酷狗的热歌榜单,只能获取到榜单的前22个
kg_song,kg_singer,kg_id=top.kg()
#由于是kg的因此我们需要导入kugou模块进行解析下载直链
from get_music.kugou import kugou
#初始化对象
kg=kugou()
#获取第一首歌的直链
kg_url=kg.get_music_url(kg_id[0])


#获取网易云音乐的热歌榜单
wy_song,wy_singer,wy_id=top.wy()
from get_music.netease import netease
wy=netease()
#获取第一首歌的直链
wy_url=wy.get_music_url(wy_id[0])

#获取qq音乐的热歌榜单
qq_song,qq_singer,qq_id=top.qq()
from get_music.qq import qq
qq=qq()
qq_url=qq.get_music_url(qq_id[5])  #解析第6首，因为前五首需要vip无法解析


