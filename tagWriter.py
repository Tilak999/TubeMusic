from mutagen.mp4 import MP4
from mutagen.mp4 import MP4Tags
from mutagen.mp4 import MP4Cover
from urllib.request import urlopen

class tagWriter(object):
	def __init__(self,meta,path):
		
		try:
			fd = urlopen(meta.album_art)
			audio = MP4(path)
			
			#clear previous meta tags
			audio.delete()
			
			covr = MP4Cover(fd.read(),MP4Cover.FORMAT_JPEG)

			fd.close()

			audio['covr'] = [covr] # make sure it's a list
			audio['\xa9nam'] = meta.title
			audio['\xa9alb'] = meta.album
			audio['\xa9ART'] = meta.artists
			audio['aART'] = meta.artists
			audio['trkn'] = [(meta.track_num,0)] #it should be int tuple
			audio['\xa9cmt'] = 'compiled using tubeMusic'
			audio['\xa9too'] = 'compiled using tubeMusic'

			audio.save()

		except:
			print("no meta to write")