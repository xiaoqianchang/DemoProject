from bs4 import BeautifulSoup
import requests


class WebSpider(object):
    def __init__(self):
        self.url = 'https://www.ted.com/talks'

    def get_talks_links(self):
        response = requests.get(self.url)
        htmlText = response.text
        return htmlText

    def write_file(self, path, text):
        with open(path, 'a', encoding='UTF-8') as file:
            file.writelines(text)


if __name__ == '__main__':
    webSpider = WebSpider()
    text = webSpider.get_talks_links()
    webSpider.write_file('talks.html', text)

