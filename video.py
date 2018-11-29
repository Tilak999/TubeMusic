from bs4 import BeautifulSoup
from urllib.request import urlopen

class Video(object):

    def __init__(self,url):
        html = urlopen(url)
        soup = BeautifulSoup(html,"html.parser")
        self.name = soup.title.string.replace("- YouTube","")
        self.title = self.name.split('-')[1].strip(' ')
        self.artist = self.name.split('-')[0].strip(' ')
        self.title = self.title.split('(')[0].strip(' ')
        self.title = self.title.split('[')[0].strip(' ')
        self.title = self.title.split('ft.')[0].strip(' ')