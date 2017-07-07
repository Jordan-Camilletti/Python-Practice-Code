"""I guess this could be classified as a very basic virus
DO NOT run this on anything unless you want your search history ruined
Finding all of this content probably put me on so many watchlists."""

import webbrowser
import time
from random import randint
imgurUrls=["0CUFPuU.gifv","4JeXPYL.jpg","OUnesDL.jpg","Iq2CH.jpg","dD7yNfY.jpg","a/GRqUA","pKZCq.jpg","EaZSYU1.gifv","LdRVqSL.jpg","tbB9ktj.jpg","GRd85Vc.jpg"]
redditUrls=["84yqig40xm7z.png"]
youtubeUrls=["watch?v=19eFnrSf41A&feature=youtu.be&t=5m39s"]
liveleakUrls=["view?i=461_1360105026&safe_mode=off","view?i=bb4_1283184704&safe_mode=off","view?i=5e8_1425739036&safe_mode=off"]
otherUrls=["http://33.media.tumblr.com/5743e899731d3604cfbc1871ef64f9dc/tumblr_njk3p6hCUh1unvl7to1_500.gif","https://streamable.com/o3mic"]
browsers=['firefox','chrome']
def start(slep):
	while(True):
		page=randint(0,4)
		if(page==0):#https://i.imgur.com/
			link=imgurUrls[randint(0,len(imgurUrls)-1)]
			webbrowser.get('firefox').open("https://i.imgur.com/"+link)
		elif(page==1):#https://i.redd.it/
			link=redditUrls[randint(0,len(redditUrls)-1)]
			webbrowser.get('firefox').open("https://i.redd.it/"+link)
		elif(page==2):#https://www.youtube.com/
			link=youtubeUrls[randint(0,len(youtubeUrls)-1)]
			webbrowser.get('firefox').open("https://www.youtube.com/"+link)
		elif(page==3):#https://www.liveleak.com/
			link=liveleakUrls[randint(0,len(liveleakUrls)-1)]
			webbrowser.get('firefox').open("https://www.liveleak.com/"+link)
		elif(page==4):#other, no link header
			link=otherUrls[randint(0,len(otherUrls)-1)]
			webbrowser.get('firefox').open(link)
		time.sleep(slep)
