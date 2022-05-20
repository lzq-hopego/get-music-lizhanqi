import requests # 请求
import json
from get_music import download
# import download

class qq:
    def __init__(self,p=False,l=False):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/33',
            'cookie':'RK=LdWlHMsQ+b; ptcz=42785168e679b66b7913e09a4387fc94c5ad2d81419840eb33a502abc14ae6c6; pgv_pvid=4366402929; fqm_pvqid=ed1a5c76-5778-4d72-aa4f-389d94cd126e; ts_uid=886687551; fqm_sessionid=2b4a4a2f-b921-4e70-861d-54a608695f10; pgv_info=ssid=s5047316408; ts_refer=www.so.com/link; _qpsvr_localtk=0.49574447171587144; login_type=1; wxopenid=; tmeLoginType=2; psrf_qqaccess_token=D40E8A445E33FC38FB47291B44C03E96; qqmusic_key=Q_H_L_5Opuh_YbF8NbIlG-FqC_2ns2gXyWSTh_cplWyZPhEpyIWDVtQUGLwQQ; psrf_access_token_expiresAt=1656146941; psrf_qqunionid=93ABF9072A8734C330E108787CC182AE; uin=2363310076; wxunionid=; qm_keyst=Q_H_L_5Opuh_YbF8NbIlG-FqC_2ns2gXyWSTh_cplWyZPhEpyIWDVtQUGLwQQ; psrf_musickey_createtime=1648370941; qm_keyst=Q_H_L_5Opuh_YbF8NbIlG-FqC_2ns2gXyWSTh_cplWyZPhEpyIWDVtQUGLwQQ; psrf_qqopenid=900C2C2A46F36818FEB00C24A5EEC6B0; wxrefresh_token=; psrf_qqrefresh_token=8289BF671C8907272471F03D564F5A69; euin=owosoio5oenl7c**; ts_last=y.qq.com/n/ryqq/search',
            'referer':'https://y.qq.com/'
            }
        self.l=l
        self.p=p
    def search(self,songname,page=1):
        self.page = page
        self.songname = songname
        self.url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p='+str(self.page)+'&n=20&w='+self.songname
        resp = requests.get(self.url, headers=self.headers)
        json_str = resp.text
        json_str = json_str[9:-1]
        json_dict = json.loads(json_str)
        music_list = json_dict["data"]["song"]["list"]
        
        self.song_name=[]
        self.singer_name=[]
        self.song_url=[]
##        print(json_dict)
        self.mid=[]
        for music in music_list:
            self.mid.append(music["albummid"])
            self.song_url.append(music["songmid"])  #歌曲的songmid
            self.song_name.append(music["songname"])  #歌曲名称
            self.singer_name.append(music["singer"][0]["name_hilight"])  #歌手名称
        return self.song_name,self.singer_name,self.song_url
    def prints(self):
        name=self.song_name
        singer=self.singer_name
        song_url=self.song_url
        for i in range(0,len(name)):
            print("序号{}\t\t{}————{}".format(i+1,name[i],singer[i]))
        songs=input('请选择您要下载哪一首歌，直接输入序号就行\n如需下载多个请用逗号分割即可，例如1,2\n输入0可以继续搜索下一页\n如果不需要下载多个，请直接输入序号就行：')
        if songs=='':
            print('\n\n\n——您未做出选择！程序即将自动退出！！！')
            return
        elif songs=='0':
            self.search(self.songname,page=self.page+1)
            self.prints()
            return 
        song_list=songs.split(",")
        for i in song_list:
            try:
                i=int(i)-1
            except ValueError:
                print("您输入的序号有问题，请用英文逗号分割谢谢！")
                return
            try:
                fname=name[i]+"-"+singer[i]+".mp3"
                songid=song_url[i]
                songurl=self.get_music_url(songid)
##                print(get_music_url)
                if songurl==None:
                    print("很抱歉由于某种原因无法为您下载"+singer[i]+'唱的'+name[i]+'的歌')
                    return
                if self.l==True:
                    self.get_music_lrc(num=i)
                if self.p==True:
                    self.get_music_pic(num=i)
                download.download(songurl,fname,ouput=True)
                print(singer[i]+'唱的'+name[i]+'下载完成啦！')
                print("已保存至当前目录下")
            except IndexError:
                print("您输入的序号不在程序给出的序号范围！")
                return
        print('\n≧∀≦\t感谢您对本程序的使用，祝您生活愉快！')
    def get_music_url(self,songid):
        url_part = "https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D".format(songid)
        music_document_html_json = requests.get(url_part).text
        music_document_html_dict = json.loads(music_document_html_json)  #将文件从json格式转化为字典格式
        music_url_part = music_document_html_dict["req_0"]["data"]["midurlinfo"][0]["purl"]
        if music_url_part != '':
            return music_document_html_dict['req_0']['data']['sip'][0]+music_url_part

    def get_music_pic(self,num):
        try:
            url='https://y.gtimg.cn/music/photo_new/T002R300x300M000'+self.mid[num]+'.jpg'
            name=self.song_name[num]+"-"+self.singer_name[num]+'-'+"封面.jpg"
            download.download(url,name)
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的封面！")
    def get_music_lrc(self,num):
        try:
            name=self.song_name[num]+"-"+self.singer_name[num]+'-'+"歌词.txt"
            headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
             'referer' : 'https://m.y.qq.com'}
            url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg?songmid={}&format=json&nobase64=1&songtype=0&callback=c'.format(self.song_url[num])
            html=requests.get(url,headers=headers)
            d=json.loads(html.text[2:-1])['lyric']
            with open(name,'w') as f:
                f.write(d)
            print("\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            print("未找到该歌曲的歌词！")

##a=qq(p=True,l=True)
##a.search('11')
##a.prints()
##input()
