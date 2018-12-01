import subprocess
from bs4 import BeautifulSoup
from urllib.request import urlopen

def download(url, filepath): 
  devnull = open('/dev/null', 'w')
  args = ['youtube-dl','--output',filepath+'.%(ext)s','--extract-audio','--audio-format','mp3',url]
  process = subprocess.Popen(args, stdout=devnull)
  retcode1 = process.wait()

def getInfo(url):
  html = urlopen(url)
  soup = BeautifulSoup(html,"html.parser")
  name = soup.title.string.replace("- YouTube","")
  title = name.strip()
  artist = ""
  try:
    title = name.split('-')[1].strip(' ')
    artist = name.split('-')[0].strip(' ')
    title = title.split('(')[0].strip(' ')
    title = title.split('[')[0].strip(' ')
    title = title.split('ft.')[0].strip(' ')
  except:
    print("Error parsing youtube video name")
  return {"title":title, "artist":artist}