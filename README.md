# get-music-lizhanqi ：Listen to what you want
多合一音乐下载，搜索，python，支持酷狗，网易，百度，一听，5sing原创及翻唱,酷我，咪咕和qq音乐平台的音乐下载，有些支持下载封面和歌词有些则不支持，requests和json占主要



**[get-music-lizhanqi](https://github.com/lzq-hopego/get-music-lizhanqi)** is a command line tool which helps you search and download music from multiple sources.

Support for QQ music, Netease music, guwo music, Kugou music and Baidu music. 

**Python3 Only. Python 3.7+ Recommended.**


**[get-music-lizhanqi](https://github.com/lzq-hopego/get-music-lizhanqi)
**是一个基于Python3的命令行工具，可以从多个网站搜索和下载音乐，方便寻找音乐，解决不知道哪个网站有版权的问题。工具的本意是**聚合搜索**，API
是从公开的网络中获得，**不是破解版**，也听不了付费歌曲。

**禁止将本工具用于商业用途**，如产生法律纠纷与本人无关，如有侵权，请联系我删除。


QQ邮箱：3101978435@qq.com

最近API封杀有点多，个人有点维护不过来,所以更新不及时不要怪我哦。

> 注意: 部分音乐源在一些国家和地区不可用。

## 功能
- 支持get-music -r 一次下载多个歌曲，具体使用方法get-music -help中会有，pypi地址：<https://pypi.org/project/get-music-lizhanqi/>
- 部分歌曲支持无损音乐
- 优先搜索高品质音乐（无损 -> 320K -> 128K）
-支持一次下载多个版本的歌曲
- 支持下载歌词和封面（部分）

> 注意：仅支持Python3，建议使用 **Python3.7 以上版本**

## 安装

使用pip安装：

```bash
$ pip install get-music-lizhanqi
```

## 更新至最新版本

使用pip更新（建议使用pip进行更新，因为最新版本一般会最先发布在pypi上，当然github也会同步）：

```
$ pip install --upgrade get-music-lizhanqi
```



在以下环境测试通过：
- 说明：不仅限测试环境，关于macos，由于作者还是个学生暂时无法提供macos的测试，不过只要python3.7版本能用，那么脚本也能使用


| 系统名称 | 系统版本       | Python版本  | 测试样片                              |
| -------- | -------------- | ---------- |  ------------------------------------- |
| Windows  | Windows 7 x64  | 3.7.0      | http://img.lizhanqi.xyz/win7.jpg      |
| Windows  | Windows 10 x64 | 3.7.0     | http://img.lizhanqi.xyz/win10.jpg     |
| Windows  | Windows 11 x64 | 3.7.0     | http://img.lizhanqi.xyz/win11.jpg     |
| Centos   | Centos 7.9 x64 | 3.7.0           | http://img.lizhanqi.xyz/centos.jpg    |
| Ubuntu   | Ubuntu 22.4 x64 | 3.7.0       | http://img.lizhanqi.xyz/ubuntu.jpg    |
| Kali     | Kali 20.4 x64  |  3.7.0    |   http://img.lizhanqi.xyz/kali.jpg      |
| Android  | Android 10 x64 | 3.6.6(qpython) | http://img.lizhanqi.xyz/phone.jpg  |
| Deepin  | Deepin 20 x64 | 3.7.0 | http://img.lizhanqi.xyz/deepin.jpg  |


## 使用方式

直接在命令行敲:

```
$ get-music
```
之后步骤按照程序提示进行下一步即可。


如果你是一个特别喜欢自定义的人，你可以这样做：
```
>>>import get_music
>>>dir(get_music)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'baidu', 'download', 'fivesing', 'kugou', 'kuwo', 'migu', 'netease', 'oneting', 'qq']
```
会返回以上内容，这时就得到了可用的模块是'baidu', 'download', 'fivesing', 'kugou', 'kuwo', 'migu', 'netease', 'oneting', 'qq',共九个可供调用的模块,下面我会介绍，每个模块的使用方法：

一、'download'模块

说明：此模块为下载时展示进度条的模块，是自己封装的，因为tqdm没有适配python3.6（总是安装失败）所以我直接自己写了一个，免得安装时出幺蛾子

get_music.download.download(url,filename)  #第一个参数是下载链接，第二个参数是保存为什么东西（需要加文件扩展名）
```
>>>get_music.download.download('https://webfs.ali.kugou.com/202206161239/72f11276df52e9182ace289d71092e83/KGTX/CLTX001/a2b996fc632a8f47a133ab6dc170c3d2.mp3','wake.mp3')
```

二、'netease','migu','oneting'属于一次性即可返回音乐的下载链接，不需要二次解析

```
>>>netease=get_music.netease.netease().search(songname)    #search(songname)中的songname是你要搜索的歌曲名字，然后程序会返回三个列表，第一个列表是歌曲名字，第二个列表是歌手，第三个列表是下载链接
>>>migu=get_music.migu.migu().search(songname)
>>>oneting=get_music.oneting.oneting().search(songname)
```

三、剩下的模块均需要二次数据解析

拿kugou举例，其余接口返回数据的方式都与kugou一致
```
>>>kugou=get_music.kugou.kugou()
>>>song_name,song_singers,song_id=kugou.search(songname)    #songname同样是歌名,search()会返回三个列表，歌曲名，歌手，歌曲id，分别赋值给前面的三个变量
>>>url=kugou.get_music_url(songid)   #songid,就是上一行代码的song_id里面的数据，通过get_music_url()可以获得真实的歌曲下载地址
```

四、fivesing，这个模块比较特殊，因为它封装了"原唱"和"翻唱"

其余的搜索、解析真实下载地址的流程就和kugou的一致
```
>>>原唱=get_music.fivesing.fivesing('ys')
>>>翻唱=get_music.fivesing.fivesing('fc')
```


## get-music -r


如果想要正确的使用-r命令，就必须创建一个名为get_music.txt的文档，里面的内容可以是以下内容，用逗号（中英都可）分隔的三个参数，每一行为一组，切不可多写，第一个是歌曲名，第二个是需要下载几首歌或者是一个歌手的名字，第三个参数就是下载的平台，由于技术原因作者写的代码很烂，所以暂时只能在kg（酷狗），kw（酷我），qq（qq音乐），wy（网易云），bd(百度),migu(咪咕)，1ting（一听），yc（5sing原唱），fc（5sing翻唱）十个接口中进行批量下载歌曲的操作
```
爱人错过,告五人,kg
爱人错过,1,qq
大田后生仔,1,wy
11,队长,kw
```

## get-music -l

下载歌曲和歌词，具体搜索歌曲的流程和get-music一致，不同的是最后多保存了个歌词
```
$get-music -l
```

## get-music -p

下载歌曲和封面，具体搜索歌曲的流程和get-music一致，不同的是最后多保存了个封面
```
$get-music -p
```

## get-music -lp

下载歌曲、封面和歌词，具体搜索歌曲的流程和get-music一致，不同的是最后多保存了封面和歌词
```
$get-music -lp  #get-music -pl也是一样，为了防止敲错，这两个都可用
```
## get-music -v

查看当前版本，并校验当前版本与pypi上的版本判断是否是最新版本，如果不是最新版本则会提示你让你更新
```
$get-music -v
```

## get-music -t

打开使用python的tkinter框架编写的可视化窗口程序，不用写一行代码即可下载到你喜欢的音乐。、
```
$get-music -t
```

## get-music -help

你的所有疑惑将在帮助中解答，当然没有本文档那么详细，建议直接阅览本md文档即可
```
$get-music -help
```
## get-music -hot
你可以查看qq，酷狗，网易云的热歌榜单的前六个。
```
$get-music -hot
```
## get-music -s
用于查看网络中关于该歌曲的网盘信息，如果有则返回网盘链接和提取码
```
$get-music -s
```

## 说明
- 在linux平台上尽量使用root用户进行pip安装，然后用root用户启动该程序，由于作者知识浅薄尚不能够对linux平台进行全平台适配，敬请理解！
- 九个搜索引擎任你挑`qq netease kugou baidu kuwo migu，1ting，5singfc，5singyc`，每个数量限制为10，保存目录为当前目录。
- 指定序号时可以使用`1 1,2(中间的逗号要用英文逗号哦，并且有的不支持，不支持这样会有提示)`的形式。
- 默认对搜索结果排序和去重，排序顺序按照歌手和歌名排序，当两者都相同时保留最大的文件。
- 无损音乐歌曲数量较少，如果没有无损会默认下载320K或128K。
-下载的歌曲的质量以最终保存的文件为准


## 示例：
- 
<http://img.lizhanqi.xyz/test.jpg>

## 支持的音乐源列表

| 音乐源     | 缩写    | 网址                      | 有效 | 无损 | 320K | 封面 | 歌词 | 单曲 |
| ---------- | ------- | ------------------------- | ---- | ---- | ---- | ---- | ---- | ---- |
| QQ音乐     | qq      | <https://y.qq.com/>       | ✓    | -    | -    | ✓     | ✓    |  ✓   |
| 酷狗音乐   | kugou   | <http://www.kugou.com/>   | ✓    | -    | -    | ✓     | ✓    | ✓    |
| 网易云音乐 | netease | <https://music.163.com/>  | ✓    | -    | ✓    | ✓     | ✓    |   ✓  |
| 咪咕音乐   | migu    | <http://www.migu.cn/>     | ✓    | -    |  -   |  ✓    |  ✓   |  ✓   |
| 百度音乐   | baidu   | <http://music.baidu.com/> | ✓    | -    | ✓    | ✓    | ✓     | ✓    |
| 酷我音乐   | kuwo   | <http://www.kuwo.cn/>      | ✓    | -    |  -   |  ✓   |  ✓    | ✓    |
| 1听   | 1ting   | <https://www.1ting.com/>       | ✓    | -    |  -   |  ✓   |  ✕    |  ✓   |
| 5sing   | 5sing   | <http://5sing.kugou.com/>    | ✓    | -    |  -   |  ✓   |  ✓    | ✓    |

> `-`表示不一定支持，`✓`表示部分或完全支持，`✕`表示尚未支持

欢迎提交支持更多音乐源！




## 更新记录
- 2022-11-02 完成v1.0.9版，修复网易云音乐无法下载歌词和封面的bug
- 2022-10-06 完成v1.0.7版，更新一些细节减小空间复杂度，更下载进度条显示总大小和下载速度
- 2022-09-25 完成v1.0.6版 修复v1.0.0版本遗留的问题，修改“get-music -r” 的文件内容格式，使用逗号分割，“歌曲，下载序号/歌手，接口”，增加下载时检测是否下载过，如果下载过，会提示是否重新下载，输入“y/Y/是”则会重新下载，不输入直接回车则不会重新下载
- 2022-9-9 完成v1.0.4版，新增get-music -s命令，用于查看网络中关于该歌曲的网盘信息，如果有则返回网盘链接和提取码
- 2022-8-17 完成v1.0.3版，修复酷我音乐的搜索不精准，支持查看酷我音乐的热歌榜，新增get-music -ip查看本机的公网地址
- 2022-8-15 完成v1.0.2版，修复qq音乐，更改在命令行的输出颜色和格式，以列表的方式打印在控制台，get-music -t的gui无任何影响，并支持get-music -hot查看qq音乐、酷狗音乐、网易云音乐的热歌榜单中的前六首，并支持直接下载试听，可能下载到的数据不太准确，后续会发布新版进行维护。
- 2022-06-11 完成v0.0.64版，修复酷狗音乐下载部分音乐时的错误
- 2022-06-11 完成v0.0.63版，开发权限开放！支持您在代码中调用该模块import get_music具体可以用多少个接口主要看dir(get_music)有什么，比如有kugou，那么可以这样用kugou=get_music.kugou()创建名为kugou的对象，然后dir(kugou)可以查看对象能进行的操作，kugou.search(songname),这是搜索，需要传递一个songname也就是歌曲名字，会返回三个列表类型的数据，包括歌曲名，歌手名，及歌曲在该平台的id号（url），如果是id号的话需要配合kugou.get_music_url(id)用这个方法会解析到真实的歌曲下载地址
- 2022-06-02 完成v0.0.62版，命令行支持向上翻页键入-1查看前一页的歌曲
- 2022-05-20 完成v0.0.59版，让您使用时更加稳定
- 2022-05-20 完成v0.0.58版，支持get-music -t 唤醒gui窗口进行下载，目前在win10上已经可以正常使用，但是没有为该gui添加下载进度条，使用的是python自带的tkinter框架
- 2022-05-13 22：55 完成v0.0.57版本，修复因python编码问题引起的报错导致get-music -r无反应等问题
- 2022-05-13 完成v0.0.56版,全面支持下载歌词和封面，get-music -l 既下载歌曲又下载歌词,get-music -p 既下载歌曲又下载封面，get-music -lp既下载歌曲又同时下载歌词和封面
- 2022-05-12 完成v0.0.55版，全新架构了一下程序，使用面向对象编程，并新增一听接口，5sing原唱，5sing翻唱，支持翻页操作输入0即可实现翻页，全部接口都同时支持多个同时下载，不支持断点续传（注意网络环境哦），同时get-music -r的接口支持kg,kw,qq,wy,migu,bd,1ting,fc,yc,不再支持qpython
- 2022-05-10 完成v0.0.54版，修复qpython中无法下载的问题，这个bug居然是file关键字的问题（qpython的关键字，至于是不是python3.6的那就不得而知喽），我把它拿来当变量了，sorry
- 2022-05-04 完成v0.0.53版，完善批量下载机制和操作手册，更新MD文档
- 2022-05-02 完成v0.0.52版，更新输出格式不再采用tqdm第三库，将适配python3.0全版本，输出将采用自己的算法，使效率更高，修复酷狗音乐数据返回慢的问题
- 2022-04-30 完成v0.0.47版,更新输出格式，不至于输出格式眼花缭乱
- 2022-04-28 完成v0.0.46版，更新进度条颜色为紫色，支持python3.7及以上
- 2022-04-27 完成v0.0.45版，修复咪咕音乐的错误
- 2022-04-27 完成v0.0.44版，修复v0.0.28的搜索bug，支持python2.9版本及以上
- 2022-04-27 完成v0.0.33版，修复返回数据一致的bug（调试时的bug，忘记改回了。{{{(>_<)}}}）
- 2022-04-26 完成v0.0.32版，完善MD文档，适配多个平台，支持get-music -r 批量下载（具体用法请get-music help程序会有详细说明）
- 2022-04-25 完成v0.0.28版，最后一版适配python2.9-python3.7以下的版本，无进度条，但是功能正常使用
- 2022-04-25 完成v0.0.27版,新增下载进度条，加快咪咕音乐的搜索效率,修改咪咕音乐的下载的错误，修复搜索结果为空的异常
- 2022-04-14 完成v0.0.21版，修复千千静听（百度音乐）无法下载封面和歌词的bug
- 2022-04-12 完成v0.0.20版，支持百度音乐(千千静听),支持-help（查看帮助），-v（查看当前版本）
- 2022-04-11 完成v0.0.11版，支持咪咕音乐
- 2022-04-10 完成v0.0.9版，更新算法，使时间复杂度更低,并支持酷我音乐
- 2022-04-09 完成v0.0.5版，支持QQ音乐
- 2022-04-09 完成v0.0.1版，支持酷狗和网易云

## 提Issues说明

- **检查是否是最新的代码，检查是否是Python3.7+，检查依赖有没有安装完整**。
- 说明使用的操作系统，例如Windows 10 x64
- 说明Python版本，以及是否使用了pyenv等虚拟环境
- 说明使用的命令参数、搜索关键字和出错的音乐源
- 如果有新的思路和建议也欢迎提交


## Credits 致谢

本项目受以下项目启发，参考了其中一部分思路，向这些开发者表示感谢。

- <https://github.com/requests/requests>

## THE END
- 本脚本仅支持学习使用，如有发现有任何商业用途，一经发现您将受到法律责任。
- 本程序使用的接口全部来源于网络，切不可有任何商业用途，或我程序中有涉及你公司利益的，你可以联系我，我会及时删除源代码，并不再更新。
- **禁止将本工具用于商业用途**，如产生法律纠纷与本人无关，如有侵权，请联系我删除。
- 如果你对界面设计感兴趣可以去看我的另一篇pyqt5对接的get-music-lizhanqi做的音乐下载播放ui，地址：https://github.com/lzq-hopego/get-music-lizhanqi-gui
- 项目创建者：李先生
- 项目维护者：李先生
- 维护者邮箱：3101978435@qq.com


## LICENSE

Copyright (c) 2022 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

