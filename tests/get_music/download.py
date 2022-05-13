import requests,time,sys




def download(url, filepath='./必须加上扩展名',ouput=False):
    if ouput==True:
        print()
    start = time.time()  # 下载开始时间
    response = requests.get(url, stream=True,timeout=3)  # stream=True必须写上
    size = 0  # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    try:
        if response.status_code == 200:  # 判断是否响应成功
            name=filepath
            print('开始下载'+name+','+'[文件格式]:'+filepath.split('.')[-1]+',[文件大小]:{size:.2f} MB,'.format(
                size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
            # filepath = '下载/222.mp4'  #注：必须加上扩展名
            with open(filepath, 'wb') as file:  # 显示进度条
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    s=float(size / content_size * 100)
                    if s==100:
                        sys.stdout.write('\r' + '[下载进度]:%s%.2f%%' % ('=' * int(size * 50 / content_size)+">", s))
                    else:
                        sys.stdout.write('\r' + '[下载进度]:%s%.2f%%' % ('=' * int(size * 50 / content_size), s))
        end = time.time()  # 下载结束时间
        print('完成！用时: %.2f秒' % (end - start))  # 输出下载用时时间
    except Exception:
        pass


