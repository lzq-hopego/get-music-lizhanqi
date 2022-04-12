import requests # 请求
import json


def qq(name):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/33',
    'cookie':'RK=LdWlHMsQ+b; ptcz=42785168e679b66b7913e09a4387fc94c5ad2d81419840eb33a502abc14ae6c6; pgv_pvid=4366402929; fqm_pvqid=ed1a5c76-5778-4d72-aa4f-389d94cd126e; ts_uid=886687551; fqm_sessionid=2b4a4a2f-b921-4e70-861d-54a608695f10; pgv_info=ssid=s5047316408; ts_refer=www.so.com/link; _qpsvr_localtk=0.49574447171587144; login_type=1; wxopenid=; tmeLoginType=2; psrf_qqaccess_token=D40E8A445E33FC38FB47291B44C03E96; qqmusic_key=Q_H_L_5Opuh_YbF8NbIlG-FqC_2ns2gXyWSTh_cplWyZPhEpyIWDVtQUGLwQQ; psrf_access_token_expiresAt=1656146941; psrf_qqunionid=93ABF9072A8734C330E108787CC182AE; uin=2363310076; wxunionid=; qm_keyst=Q_H_L_5Opuh_YbF8NbIlG-FqC_2ns2gXyWSTh_cplWyZPhEpyIWDVtQUGLwQQ; psrf_musickey_createtime=1648370941; qm_keyst=Q_H_L_5Opuh_YbF8NbIlG-FqC_2ns2gXyWSTh_cplWyZPhEpyIWDVtQUGLwQQ; psrf_qqopenid=900C2C2A46F36818FEB00C24A5EEC6B0; wxrefresh_token=; psrf_qqrefresh_token=8289BF671C8907272471F03D564F5A69; euin=owosoio5oenl7c**; ts_last=y.qq.com/n/ryqq/search',
    'referer':'https://y.qq.com/'
    }

    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w={}'
    resp = requests.get(url.format(name), headers=headers)

    json_str = resp.text
    json_str = json_str[9:-1]
    json_dict = json.loads(json_str)
    music_list = json_dict["data"]["song"]["list"]

    song_name=[]
    singer_name=[]
    song_url=[]

    for music in music_list:
            per_songmid = music["songmid"]  #歌曲的songmid
            per_songname = music["songname"]  #歌曲名称
            singer = music["singer"][0]["name_hilight"]  #歌手名称
            
            music_document_url_part = "https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D".format(per_songmid)
            music_document_html_json = requests.get(music_document_url_part).text
            music_document_html_dict = json.loads(music_document_html_json)  #将文件从json格式转化为字典格式
            music_url_part = music_document_html_dict["req_0"]["data"]["midurlinfo"][0]["purl"]
            if music_url_part != '':
                song_name.append(per_songname)
                singer_name.append(singer)
                song_url.append(music_document_html_dict['req_0']['data']['sip'][0]+music_url_part)
    return song_name,singer_name,song_url
    
