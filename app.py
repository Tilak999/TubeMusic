from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from mp3Tags import mp3Tags
from itunesMeta import itunesMeta

import urllib.parse
import re
import youtube

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/getMusic',methods=['GET'])
def getMusic():
	try:
		#get url parameter + parse url to readable form
		url = urllib.parse.unquote(request.args.get('url'))
		info = youtube.getInfo(url)
		meta = itunesMeta(info['title'],info['artist'])
		return render_template('getMusic.html', meta=meta.getBestMatch(), url=url)
	except:
		print('error')
		return redirect('/')

@app.route('/saveToDisk',methods=['GET'])
def saveToDisk():
		url = urllib.parse.unquote(request.args.get('url'))

		info = youtube.getInfo(url)
		meta = itunesMeta(info['title'],info['artist'])
		name = info['title']+"-"+info['artist']
		name = re.sub(r'([^\s\w_-])+','',name).replace(" ","_")

		download_dir = './static/'
		filepath = download_dir + name
		youtube.download(url,filepath)
		
		mp3Tags(meta.getBestMatch(),filepath + ".mp3")

		return redirect(filepath + ".mp3")

if __name__ == '__main__':
    app.run()