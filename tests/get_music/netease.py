from get_music import download
from rich.console import Console
import base64
import binascii
import json
import random
import string
from urllib import parse
import requests
from Crypto.Cipher import AES
console=Console()

class netease:
    def __init__(self,p=False,l=False):
        
        self.l=l
        self.p=p
        self.api='网易云音乐'
    def search(self,songname,page=0):
        headers = {
        'authority': 'music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://music.163.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://music.163.com/search/',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
        url='https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        d = {"hlpretag": "<span class=\"s-fc7\">", "hlposttag": "</span>", "s": songname, "type": "1", "offset": str(page),
         "total": "true", "limit": "20", "csrf_token": ""}
        d = json.dumps(d)
        random_param = get_random()
        param = get_final_param(d, random_param)
        data='params=' + parse.quote(param['params']) + '&encSecKey=' + parse.quote(param['encSecKey'])
        
        self.page=page
        self.song_name=songname
        req=requests.post(url,headers=headers,data=data,timeout=1)
        d=json.loads(req.text)

        
        songs=d["result"]['songs']
        self.songname=[]
        self.songs_url=[]
        self.singername=[]

        self.id=[]
        self.pic=[]
        self.songs=songs
        for i in songs:
                self.songname.append(i["name"])
                self.singername.append(i['ar'][0]["name"])
                self.id.append(i['id'])
                self.pic.append(i['al']['picUrl'])
                d = {"ids": "[" + str(i['id'])+ "]", "level": "standard", "encodeType": "",
                 "csrf_token": ""}
                d = json.dumps(d)
                param = get_final_param(d, random_param)
                song_info = get_reply(param['params'], param['encSecKey'])
                if len(song_info) > 0:
                    song_info = json.loads(song_info)
                    song_url = json.dumps(song_info['data'][0]['url'], ensure_ascii=False)
                    if song_url=='null':
                        self.songs_url.append("")
                    else:
                        self.songs_url.append(song_url)
                else:
                    self.songs_url.append("")
        return self.songname,self.singername,self.songs_url
    def prints(self):
        pass
    def get_music_url(self,url):
        return url
        
    def get_music_lrc(self,num,return_url=False):
        headers = {
                "user-agent" : "Mozilla/5.0",
                "Referer" : "http://music.163.com",
                "Host" : "music.163.com"
            }
        try:
            song_id=self.id[num]
            if not isinstance(song_id, str):
                song_id = str(song_id)
            url = "http://music.163.com/api/song/lyric?id={}+&lv=1".format(song_id)
            r = requests.get(url, headers=headers,timeout=1)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            json_obj = json.loads(r.text)
            if return_url:
                return json_obj["lrc"]["lyric"]
            name=self.songname[num]+"-"+self.singername[num]+'-'+"歌词.txt"
            name=name.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
            with open(name,'w') as f:
                f.write(json_obj["lrc"]["lyric"])
            console.print("[b red]\n\n歌词已下载完成,文件名称为:"+name+"\n")
        except:
            if type(num)==str:
                url = f"http://music.163.com/api/song/lyric?id={num}+&lv=1&tv=-1"
                r = requests.get(url, headers=headers,timeout=1)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                json_obj = json.loads(r.text)
                return json_obj["lrc"]["lyric"]

            else:
                console.print("[b red]未找到该歌曲的歌词！")
    def get_music_pic(self,num,return_url=False):
        try:
            url=self.pic[num]
            if return_url:
                return url
            name=self.songname[num]+"-"+self.singername[num]+'-'+"封面.jpg"
            download.download(url,name)
            console.print("[b red]\n歌曲封面下载完成，文件名称为:"+name)
        except:

            console.print("[b red]未找到该歌曲的封面！")
# 从a-z,A-Z,0-9中随机获取16位字符
def get_random():
    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return random_str


# AES加密要求加密的文本长度必须是16的倍数，密钥的长度固定只能为16,24或32位，因此我们采取统一转换为16位的方法
def len_change(text):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    text = text.encode("utf-8")
    return text


# AES加密方法
def aes(text, key):
    # 首先对加密的内容进行位数补全，然后使用 CBC 模式进行加密
    iv = b'0102030405060708'
    text = len_change(text)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(text)
    encrypt = base64.b64encode(encrypted).decode()
    return encrypt


# js中的 b 函数，调用两次 AES 加密
# text 为需要加密的文本， str 为生成的16位随机数
def b(text, str):
    first_data = aes(text, '0CoJUm6Qyw8W8jud')
    second_data = aes(first_data, str)
    return second_data


# 这就是那个巨坑的 c 函数
def c(text):
    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    text = text[::-1]
    result = pow(int(binascii.hexlify(text.encode()), 16), int(e, 16), int(f, 16))
    return format(result, 'x').zfill(131)


# 获取最终的参数 params 和 encSecKey 的方法
def get_final_param(text, str):
    params = b(text, str)
    encSecKey = c(str)
    return {'params': params, 'encSecKey': encSecKey}





# 通过歌曲的id获取播放链接
def get_reply(params, encSecKey):
    url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
    payload = 'params=' + parse.quote(params) + '&encSecKey=' + parse.quote(encSecKey)
    headers = {
        'authority': 'music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://music.163.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://music.163.com/',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

##测试代码
##a=netease(l=True,p=True)
##d=a.search("微微")
##a.get_music_url(a.songs_url[0])
##input()
