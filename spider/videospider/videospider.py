"""
流媒体视频下载：
1. 先下载视频片段（片段是不能播放的）
2. 再合并片段成视频（可播放但可能是没有声音的）
3. 下载音频的方式同上（视频）
4. 再通过某些工具把视频音频合并
"""
import requests
import threading
import datetime
import os

count = 0


def downloader(start, end, url, resources):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    for resource in resources[start: end]:
        global count

        request = requests.get(resource.replace("\n", ""),
                         headers=headers,
                         stream=True)
        bytes = resource.split('=')[-1]
        with open("/spider/ted/videos/" + bytes.replace("\n", ""), "wb") as code:
            code.write(request.content)
        count = count + 1
        print("In Progress：%.2f" % (count / len(resources)))


def download_vedio(url, num_thread=100):
    cwd = os.getcwd()
    file = open('index.m3u8', 'r', encoding='UTF-8')
    text_list = file.readlines()
    resource_list = []
    for text in text_list:
        if text.find('#EX') == -1:
            resource_list.append(text)

    file.close()
    file_size = len(resource_list)

    part = file_size // num_thread
    for n in range(num_thread):
        start = part * n
        if n == num_thread - 1:
            end = file_size
        else:
            end = start + part

        thread = threading.Thread(target=downloader, kwargs={'start': start, 'end': end, 'url': url, 'resources': resource_list})
        thread.setDaemon(True)
        thread.start()

    currentThread = threading.current_thread()
    for t in threading.enumerate():
        if t is currentThread:
            continue
        t.join()


def build_merge_cmd():
    cwd = os.getcwd()
    f = open('index.m3u8', 'r', encoding='UTF-8')
    text_list = f.readlines()
    files = []
    for i in text_list:
        if i.find('#EX') == -1:
            files.append(i)
    f.close()
    tmp = []
    for file in files[0:1024]:
        bytes = file.split('=')[-1]
        tmp.append(bytes.replace("\n", ""))

    shell_str = '+'.join(tmp)
    shell_str = 'copy /b ' + shell_str + ' ted.mp4' + '\n' + 'del *.ts'
    return shell_str


def generate_merge_cmd(cmdString):
    cwd = os.getcwd()
    f = open("merge.bat", 'w')
    f.write(cmdString)
    f.close()


if __name__ == '__main__':
    url = "https://pb.tedcdn.com/talk/hls/video/"
    start = datetime.datetime.now().replace(microsecond=0)
    download_vedio(url)
    end = datetime.datetime.now().replace(microsecond=0)
    print(end - start)
    cmd = build_merge_cmd()
    generate_merge_cmd(cmd)

