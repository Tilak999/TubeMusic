import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
from urllib.request import urlopen
from metadata_modal import metadata

class mp3Tags(object):
    def __init__(self,meta,path):
        
        try:
            audio = EasyID3(path)
        except mutagen.id3.ID3NoHeaderError:
            audio = mutagen.File(path, easy=True)
            audio.add_tags()

        audio['title'] = meta.track_name
        audio['artist'] = meta.artists
        audio['album'] = meta.album
        audio['tracknumber'] = str(meta.track_num)
        audio['encodedby'] = 'TubeMusic'
        audio['website'] = 'https://tubemusic.herokuapp.com'
        audio['genre'] = meta.track_genre
        audio.save(path, v2_version=3, v1=2)

        audio = ID3(path,translate=True,v2_version=3)
        #audio.tags.delete(path, delete_v1=True, delete_v2=True)
        audio.add(
            APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,
                desc=u'Cover',
                data=urlopen(meta.album_art).read()
            )
        )

        audio.update_to_v23()
        audio.save(path, v2_version=3, v1=2)

if __name__ == '__main__':
    mp3Tags(metadata(),'./static/sam.mp3')