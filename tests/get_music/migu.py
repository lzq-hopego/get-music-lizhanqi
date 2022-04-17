import requests,json,sys

##q="爱人错过"
def migu(q):
    url="http://pd.musicapp.migu.cn/MIGUM2.0/v1.0/content/search_all.do"
    head={"referer": "http://music.migu.cn/",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/33",
          
        }
    params = {
            "ua": "Android_migu",
            "version": "5.0.1",
            "text": q,
            "pageNo": "1",
            "pageSize": "1",
            "searchSwitch": '{"song":1,"album":0,"singer":0,"tagSong":0,"mvSong":0,"songlist":0,"bestShow":1}',
        }

    html=requests.get(url,headers=head,params=params,timeout=1)

    res_data=json.loads(html.text)['songResultData']["result"]
    singers=[]
    song_name=[]
    song_url=[]
    print("——正在分析数据，请耐心等待——\n")

    for i in res_data:
        singers.append(i['singers'][0]['name'])
        song_id=i["contentId"]
        song_name.append(i['name'])
        rate_list=sorted(i["rateFormats"],key=lambda x:int(x["size"]),reverse=True)
        Songurl='https://freetyst.nf.migu.cn/'
    ##        print(rate_list)
        for i in rate_list:
            if "androidUrl" in list(i.keys()):
                ftp=i['androidUrl'].strip("ftp://").strip("218.200.160.122:21/")
                break
            if 'url' in list(i.keys()):
                ftp=i['url'].strip("url://").strip("218.200.160.122:21/")
                break
    ##        try:
    ##            ftp=rate_list[0]['androidUrl'].strip("ftp://").strip("218.200.160.122:21/")
    ##        except:
    ##            ftp=rate_list[1]['url'].strip("ftp://").strip("218.200.160.122:21/")
        song_url.append(Songurl+ftp)

    for i in range(0,len(singers)-1):
        print("序号：{} \t{}——{}".format(i+1,song_name[i],singers[i]))
    try:
        a=int(input("请输入您需要下载的歌曲序号(不支持多个同时下载):"))-1
    except:
        print('\n\n\n——您未做出选择！程序即将自动退出！！！')
        sys.exit()

    print("由于歌曲品质过高，所以会占用很长的下载时间，请保持网络畅通，谢谢")
    rep=requests.get(song_url[a])
    geshi=song_url[a].split(".")[-1]

    with open("./音乐/"+song_name[a]+"-"+singers[a]+"."+geshi,'wb')as f:
        f.write(rep.content)

    print("\n\n"+singers[a]+'唱的'+song_name[a]+'下载完成啦！')
    print("\n\n已保存至当前目录的音乐文件夹下")
    print('\n≧∀≦\n感谢您对本程序的使用，祝您生活愉快！')
