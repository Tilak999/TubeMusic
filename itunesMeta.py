from urllib.request import urlopen
from urllib.request import pathname2url
from metadata_modal import metadata
import json

class itunesMeta(object):
   url = 'https://itunes.apple.com/search?term=$q&limit=5&media=music&entity=song'

   def searchSong(self,title):
      query = title.replace(" ","+")
      request_url = self.url.replace("$q",query)
      print(request_url)
      bStream = urlopen(request_url)
      return bStream.read().decode('utf-8')
   
   def getAllMatching(self,title,artist):
      data = self.searchSong(title)
      parsed = json.loads(data)
      #print(json.dumps(parsed,indent=4))
      meta_list = list()
      for m in parsed['results']:
         meta = metadata()
         meta.track_name = m['trackName']
         meta.track_num = m['trackNumber']
         meta.album = m['collectionName']
         meta.artists = m['artistName']
         meta.track_genre = m['primaryGenreName']
         artworkUrl = m['artworkUrl100'].replace('100x100bb','400x400bb')
         #print(artworkUrl)
         meta.album_art = artworkUrl
         meta_list.append(meta)
      
      if(len(meta_list) == 0):
         meta = metadata()
         meta.track_name = title
         meta.artists = artist
         meta_list.append(meta)
     
      return meta_list

   def __init__(self,title,artist):
      self.bestmatch = self.getAllMatching(title, artist)[0]
   
   def getBestMatch(self):
      return self.bestmatch