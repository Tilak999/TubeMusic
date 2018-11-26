from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

import urllib.parse
import re

from video import Video
#from tagWriter import tagWriter
from mp3Tags import mp3Tags
from SpotifyMeta import SpotifyMeta

import subprocess

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/getMusic',methods=['GET'])
def getMusic():

	try:
		#get url parameter + parse url to readable form
		url = urllib.parse.unquote(request.args.get('url'))

		v = Video(url)
		meta = SpotifyMeta(v.title,v.artist)

		return render_template('getMusic.html', meta=meta, url=url)
	
	except:
		print('error');
		return redirect('/')

@app.route('/saveToDisk',methods=['GET'])
def saveToDisk():
	
	try:
		url = urllib.parse.unquote(request.args.get('url'))

		v = Video(url)
		meta = SpotifyMeta(v.title,v.artist)
		name = v.title+"-"+v.artist
		name = re.sub(r'([^\s\w_-])+','',name).replace(" ","_")

		download_dir = '/static/'
		#download_dir = '/Users/Tilak/Documents/tubemusic/wsgi/static/songs/'
		temp_file = download_dir+name+'.temp'
		final_file = download_dir+name+'.mp3'

		devnull = open('/dev/null', 'w')
		
		args = ['youtube-dl','--restrict-filenames','-o',final_file,'--extract-audio','--audio-format','mp3','--audio-quality','0',url]
		process = subprocess.Popen(args, stdout=devnull)
		retcode1 = process.wait()

		if(meta.isEmpty == 'false'):
			mp3Tags(meta,final_file)

		return redirect('/static/'+name+'.mp3')

	except:
		return "sorry some server side error occured, try with another song link."

if __name__ == '__main__':
    app.run()