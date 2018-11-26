from urllib.request import urlopen
from urllib.request import pathname2url
import json

class SpotifyMeta(object):

  def __init__(self,title,artist):
     '''
     query = pathname2url(title)
     url = 'https://api.spotify.com/v1/search?q='+query+'&type=track'

     bStream = urlopen(url)
     txt = bStream.read().decode('utf-8')
     meta = json.loads(txt)
     '''
     self.isEmpty = 'false'
     self.title = title
     self.track_num = 0
     self.album = ''
     self.artists = artist
     self.album_art = ''
     
     if(True):
        print('info: Meta empty')
        self.isEmpty = 'true'

     else:

        music = meta['tracks']['items'][0]

        self.album = music['album']['name']
        self.album_art = music['album']['images'][1]['url']
        self.title = music['name']
        self.track_num = music['track_number']
        self.artists = '';

        for artist in music['artists']:
          self.artists = self.artists + artist['name']+', '
        
        self.artists = self.artists.strip(', ')
        
        print('Song name :'+self.title)
        print('Album name :'+self.album)
        print('Artists: '+self.artists)
