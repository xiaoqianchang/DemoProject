from bs4 import BeautifulSoup
import requests
from contextlib import closing
import os
import sys


class WebSpider(object):
    def __init__(self):
        self.url = 'https://www.ted.com/talks'
        self.talks = []
        self.links = []
        self.image_links = []

    def createBeautifulSoup(self):
        """
        创建 BeautifulSoup
        :return:
        """
        response = requests.get(self.url)
        html_text = response.text
        # BeautifulSoup(html_text, 'html.parser')
        # bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
        # 没有安装 lxml 会报如上错误 使用 pip install lxml 安装就行就行
        # 或者使用 BeautifulSoup(html_text, 'html.parser')
        bs = BeautifulSoup(html_text, 'lxml')
        return bs

    def get_talks_links(self):
        """
        1. 针对网页标签 使用 find 方法，获取某标签里面的属性用 get 方法
        2. 获取某标签的列表 使用 find_all 方法
        :return:
        """
        bs = WebSpider.createBeautifulSoup(self)
        results_div = bs.find('div', id='browse-results')
        results_div_h4 = results_div.find_all('h4', class_='f-w:700 h9 m5')
        # print(results_div_h4)
        for item in results_div_h4:
            self.talks.append(item.find('a').string)
            self.links.append(item.find('a').get('href') + '\n')

    def get_talks_image_links(self):
        """
        获取图片 img src 资源
        :return:
        """
        bs = WebSpider.createBeautifulSoup(self)
        results_div = bs.find('div', id='browse-results')
        results_div_img = results_div.find_all('img')
        for item in results_div_img:
            self.image_links.append(item.get('src') + '\n')

    def write_file(self, path, text):
        """
        写文件方法
        :param path:
        :param text:
        :return:
        """
        with open(path, 'a', encoding='UTF-8') as file:
            file.writelines(text)

    def download_image(self, path, image_url, filename):
        """
        下载图片
        :param path: 本地保存的路径
        :param image_url: 图片连接
        :param filename: 本地保存的文件名
        :return:
        """
        image_path = os.path.join(path, filename)
        request_headers = {'Accept': '*/*',
                           'Accept-Encoding': 'gzip, deflate, br',
                           'Accept-Language': 'zh-CN,zh;q=0.9',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        size = 0
        with closing(requests.get(image_url, headers=request_headers, stream=True)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                sys.stdout.write(filename + ' downloading...\n')
                sys.stdout.write('File Size: %0.2f MB\n' % (content_size / chunk_size / 1024))

                with open(image_path, 'wb') as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        file.flush()
                        sys.stdout.write('In Progress: %.2f%%' % float(size / content_size * 100) + '\r')
                        sys.stdout.flush()

    def start_download(self, links):
        for link in links:
            temp = link.split('/')[-1]
            image_name = temp.split('?')[0]
            self.download_image('/spider/ted/image/', link, image_name)


if __name__ == '__main__':
    webSpider = WebSpider()
    # 获取连接
    # webSpider.get_talks_links()
    # webSpider.write_file('talks.txt', webSpider.talks)
    # webSpider.write_file('links.txt', webSpider.links)
    webSpider.get_talks_image_links()
    # webSpider.write_file('imgs.txt', webSpider.imgs)
    # 下载图片
    webSpider.start_download(webSpider.image_links)

