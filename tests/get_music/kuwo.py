from urllib.request import urlretrieve
from urllib.parse import quote
import requests

import json






def kuwo(musicName):
    encodName=quote(musicName)
    url='https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(encodName)
    referer='https://www.kuwo.cn/search/list?key={}'.format(encodName)
    # 请求头
    headers = {
        "Cookie": "_ga=GA1.2.2021007609.1602479334; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1602479334,1602673632; _gid=GA1.2.168402150.1602673633; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1602673824; kw_token=5LER5W4ZD1C",
        "csrf": "5LER5W4ZD1C",
        "Referer": "{}".format(referer),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    }
    response=requests.get(url=url,headers=headers)
    dict2=json.loads(response.text)
    misicInfo=dict2['data']['list']  # 歌曲信息的列表
    musicNames=list()   # 歌曲名称的列表
    singer=[]
    song_url=[]   # 存储歌曲下载链接的列表
    for i in range(len(misicInfo)):


        songurl=get_url(misicInfo[i]['rid'])
        if songurl != '' :
            singer.append(misicInfo[i]['artist'])
            musicNames.append(misicInfo[i]['name'])
            song_url.append(songurl)
        
    return musicNames,singer,song_url



def get_url(i):
    url2='http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=9e58f6a0-b88e-11ec-a21e-535a6948e2ff'.format(i)
    headers2={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    response2=requests.get(url=url2,headers=headers2)
    dict3=json.loads(response2.text)
    try:
        url=dict3['data']['url']
    except:
        return ''
    return url


