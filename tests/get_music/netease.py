import requests,json

def netease(songname,page=1):
    headers={'referer':'http://music.163.com/',
        'proxy':"false",
        'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

    data={'s':songname,
        'type':1,
        'offset':page*10-10,
        'limit':10}

    url='http://music.163.com/api/cloudsearch/pc'

    txt=requests.post(url,headers=headers,data=data,timeout=1)

    d=json.loads(txt.text)

    song_url=['http://music.163.com/song/media/outer/url?id=','.mp3']

    songs=d["result"]['songs']
    song_name=[]
    song_id=[]
    songer_name=[]
    for i in songs:
            song_id.append(str(i['id']).join(song_url))
            song_name.append(i["name"])
            songer_name.append(i['ar'][0]["name"])

##    for i in range(0,len(song_id)-1):
    return song_name,songer_name,song_id
