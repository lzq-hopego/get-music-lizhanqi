import requests
import re
from rich.progress import Progress
import rich
from rich.console import Console
import os


def download(url,name,ouput=False):
    console=Console()
    if ouput==True:
        print()
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    name = re.sub(rstr, "_", name)  # 替换为下划线
    if os.path.exists(r"./"+name):
        yorn=console.input('[b green]“[b red]{}[/]”已下载是否重新下载(Y/N):'.format(name))
        if yorn not in ['y','Y','是']:
            return
    response = requests.get(url, stream = True,timeout = 1)  # stream=True必须写上
    size = 0  # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小


    with Progress(rich.progress.TextColumn("[progress.description]{task.description}")
                  ,rich.progress.BarColumn()
                  ,rich.progress.TaskProgressColumn()
                  ,rich.progress.TimeRemainingColumn()
                  ,rich.progress.TotalFileSizeColumn()
                  ) as progress:
        task1 = progress.add_task("[b red]正在下载:" + name, total=100)
        while not progress.finished:
            try:
                
                with open(name, 'wb') as file:
                    for data in response.iter_content(chunk_size = 1024):
                        file.write(data)
                        size += len(data)
                        n = int(size * 100 / content_size)
                        progress.update(task1, completed = n)

            except Exception:
                pass
    


