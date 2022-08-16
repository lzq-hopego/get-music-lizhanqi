
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import requests,time
from get_music import kugou
from get_music import netease
from get_music import kuwo
from get_music import fivesing
from get_music import qq
from get_music import kuwo
from get_music import oneting
from get_music import baidu
from get_music import migu

 

song_name=[]
singer_name=[]
song_url=[]
page=1
#选择文件路径的函数
def selectPath():
    path_ = askdirectory()
    path.set(path_)
##帮助文档
def help_info():
    tkinter.messagebox._show('get-music GUI帮助', 'get-music的gui界面介绍：\n输入下载的歌曲名.单曲搜索结果选中某行后再进行下载,重新搜索记得清空列表\n支持：\n歌曲搜索\n歌手搜索\n歌词搜索\n模糊搜索')
##清除text的内容
def cleartxt():
    text.delete(0,END)
##回车触发的事件
def enter(self):
    if entry.get()=='':
        tkinter.messagebox._show('警告信息','请输入搜索字段！')
        return
    global song_name
    global singer_name
    global song_url
    text.delete(0,END)
    song = entry.get()  #获得歌曲名
    d={1:kugou.kugou(),
       2:netease.netease(),
       3:qq.qq(),
       4:kuwo.kuwo(),
       5:migu.migu(),
       6:baidu.baidu(),
       7:oneting.oneting(),
       8:fivesing.fivesing('yc'),
       9:fivesing.fivesing('fc')}
    global api
    api=d[comboExample.current()+1]
    try:
        song_name,singer_name,song_url=api.search(song)
    except:
        tkinter.messagebox._show('警告信息',"无法返回数据或接口失效,或者您的网络未连接，如果还未解决可联系维护者邮箱：3101978435@qq.com")
        return
    for i in range(len(song_name)):
        text.insert(END, ">>>" +song_name[i]+"-"+singer_name[i] )
        text.see(END)
        text.update()
    global page
    page=1
##单击搜索的事件
def show():
    if entry.get()=='':
        tkinter.messagebox._show('警告信息','请输入搜索字段！')
        return
    global song_name
    global singer_name
    global song_url
    text.delete(0,END)
    song = entry.get()  #获得歌曲名
    d={1:kugou.kugou(),
       2:netease.netease(),
       3:qq.qq(),
       4:kuwo.kuwo(),
       5:migu.migu(),
       6:baidu.baidu(),
       7:oneting.oneting(),
       8:fivesing.fivesing('yc'),
       9:fivesing.fivesing('fc')}
    global api
    api=d[comboExample.current()+1]
    try:
        song_name,singer_name,song_url=api.search(song)
    except:
        tkinter.messagebox._show('警告信息',"无法返回数据或接口失效,或者您的网络未连接，如果还未解决可联系维护者邮箱：3101978435@qq.com")
        return
    for i in range(len(song_name)):
        text.insert(END, ">>>" +song_name[i]+"-"+singer_name[i] )
        text.see(END)
        text.update()
    global page
    page=1
##单击下一页的事件
def nexit():
    if entry.get()=='':
        tkinter.messagebox._show('警告信息','请输入搜索字段！')
        return
    global song_name
    global singer_name
    global song_url
    text.delete(0,END)
    song = entry.get()  #获得歌曲名
    d={1:kugou.kugou(),
       2:netease.netease(),
       3:qq.qq(),
       4:kuwo.kuwo(),
       5:migu.migu(),
       6:baidu.baidu(),
       7:oneting.oneting(),
       8:fivesing.fivesing('yc'),
       9:fivesing.fivesing('fc')}
    global api
    global page
    page=page+1
    api=d[comboExample.current()+1]
    try:
        song_name,singer_name,song_url=api.search(song,page)
    except:
        tkinter.messagebox._show('警告信息',"无法返回数据或接口失效,或者您的网络未连接，如果还未解决可联系维护者邮箱：3101978435@qq.com")
        return 
    for i in range(len(song_name)):
        text.insert(END, ">>>" +song_name[i]+"-"+singer_name[i] )
        text.see(END)
        text.update()
##单击上一页的事件
def updata():
    if entry.get()=='':
        tkinter.messagebox._show('警告信息','请输入搜索字段！')
        return
    global song_name
    global singer_name
    global song_url
    text.delete(0,END)
    song = entry.get()  #获得歌曲名
    d={1:kugou.kugou(),
       2:netease.netease(),
       3:qq.qq(),
       4:kuwo.kuwo(),
       5:migu.migu(),
       6:baidu.baidu(),
       7:oneting.oneting(),
       8:fivesing.fivesing('yc'),
       9:fivesing.fivesing('fc')}
    global api
    global page
    if page==1:
        tkinter.messagebox._show('警告信息','已经是第一页啦！')
        show()
        return 
    page=page-1
    api=d[comboExample.current()+1]
    try:
        song_name,singer_name,song_url=api.search(song,page)
    except:
        tkinter.messagebox._show('警告信息',"无法返回数据或接口失效,或者您的网络未连接，如果还未解决可联系维护者邮箱：3101978435@qq.com")
        return 
    for i in range(len(song_name)):
        text.insert(END, ">>>" +song_name[i]+"-"+singer_name[i] )
        text.see(END)
        text.update()
##为程序更加人性化的小变量
cishu=1
##one是一次返回数据的接口，由于接口多且复杂所以有很多接口不是一次性返回的数据需要二次解密
one=[1,4,6]
##单击下载的事件
def download():
    try:
        if entry_path.get() =='':
            tkinter.messagebox._show('警告信息',"您未选择路径！")
        
        else:
            if comboExample.current() in one:
                # 一次就可以返回数据的接口
                path=entry_path.get()
                try:
                    song_index=text.curselection()[0]
                except IndexError:
                    tkinter.messagebox._show('警告信息',"您未选择歌曲！")
                    return 
                song=song_url[song_index]
                fname=song_name[song_index]+'-'+singer_name[song_index]+".mp3"
                fname=fname.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
                create(song,path+"/"+fname)
            else:
                # 需要另外解析音乐下载地址的接口
                path=entry_path.get()
                try:
                    song_index=text.curselection()[0]
                except IndexError:
                    tkinter.messagebox._show('警告信息',"您未选择歌曲！")
                    return 
                song=api.get_music_url(song_url[song_index])
                fname=song_name[song_index]+'-'+singer_name[song_index]+".mp3"
                fname=fname.replace(':','_').replace('?','_').replace('|','_').replace('"','_').replace('<','_').replace('>','_')
                create(song,path+"/"+fname)
    except:
        tkinter.messagebox._show('警告信息',"无法返回数据或接口失效,或者您的网络未连接,当然也有因为因为路径的问题导致的无法下载，如果还未解决可联系维护者邮箱：3101978435@qq.com")
        return


def create(url,filepath):
    top = Toplevel()
    top.geometry('300x50+{}+{}'.format(int((sw-770)/2),int((sh-460)/2)))
    top.title('下载进度')
    pb = ttk.Progressbar(top, length=200, mode="determinate", orient=HORIZONTAL)
    pb.pack(padx=10, pady=20)
    pb["maximum"] = 100
    pb["value"] = 0  
    start = time.time()  # 下载开始时间
    try:
        response = requests.get(url, stream=True,timeout=1)  # stream=True必须写上
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(response.headers['content-length'])  # 下载文件总大小
        try:
            if response.status_code == 200:  # 判断是否响应成功
                name=filepath
                print('开始下载'+name+','+'[文件格式]:'+filepath.split('.')[-1]+',[文件大小]:{size:.2f} MB,'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                with open(filepath, 'wb') as file:  # 显示进度条
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        s=float(size / content_size * 100)
                        vlue=int(size * 100 / content_size)
                        pb["value"] = vlue      
                        root.update()            # 更新画面                    
            end = time.time()  # 下载结束时间
            print('完成！用时: %.2f秒' % (end - start))  # 输出下载用时时间
        except:
            top.destroy()
            pass
    except:
        tkinter.messagebox._show('警告信息',"无法返回数据或接口失效,或者您的网络未连接,当然也有因为因为路径的问题导致的无法下载，如果还未解决可联系维护者邮箱：3101978435@qq.com")
        top.destroy()
    top.destroy()



root = Tk()
##禁止拉伸窗体
root.resizable(False,False)
##调整窗口的透明度
root.attributes('-alpha', 0.9)
path = StringVar()

##初始化窗口至屏幕中央
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
root.geometry('770x460+{}+{}'.format(int((sw-770)/2),int((sh-460)/2)))

root.title("get-music GUI")


##下拉列表控件
comboExample = ttk.Combobox(root, 
                            values=[
                                    "酷狗音乐", 
                                    "网易云音乐",
                                    "QQ音乐",
                                    "酷我音乐",
                                    "咪咕音乐",
                                    "千千静听",
                                    "一听音乐",
                                    "5sing原唱",
                                    "5sing翻唱"],font=("Consolas", 15),state="readonly")
comboExample.grid(row=0, column=0)
comboExample.current(0)

 

Button(root, text="搜索", relief = 'ridge',font=("Consolas", 15), command=show).grid(row=0, column=2)
 
entry = Entry(root, font=('Consolas', 15))
entry.grid(row=0, column=1)
##绑定在输入框的回车事件
entry.bind("<Return>", enter)
 
Label(root, text="文件存放路径", font=('Consolas', 15)).grid(row=2, column=0)
#存放路径的输入栏
entry_path = Entry(root, textvariable = path,font=('Consolas', 15))
entry_path.grid(row=2, column=1)
 
Button(root, text="选择路径", relief = 'ridge',font=("Consolas", 15), command=selectPath).grid(row=2, column=2)#,sticky=E)
 
text = Listbox(root,selectmode = BROWSE,font=("Consolas", 15), width=45, height=10)
text.grid(row=3, columnspan=2)



Button(root, text="清空列表", relief = 'ridge',font=("Consolas", 15), command=cleartxt).grid(row=3, column=2,sticky=S)
 
#下载和退出按钮

Button(root, text="下一页",font=("Consolas", 15),command=nexit).grid(row=4, column=1)
Button(root, text="上一页",font=("Consolas", 15),command=updata).grid(row=4, column=1,sticky=W)
btn_down=Button(root, text="开始下载",relief = 'ridge',font=("Consolas", 15), command=download).grid(row=4, column=0, sticky=W)

Button(root, text="退出", relief = 'ridge',font=("Consolas", 15), command=root.destroy).grid(row=4, column=1, sticky=E)
Button(root, text="帮助", relief = 'ridge',font=("Consolas", 15), command=help_info).grid(row=4, column=2, sticky=E)
root.mainloop()
