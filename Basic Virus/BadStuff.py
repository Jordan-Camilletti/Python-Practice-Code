"""I guess this could be classified as a very basic virus
DO NOT run this on anything unless you want your search history ruined
Finding all of this content probably put me on so many watchlists."""

import webbrowser
import time
from random import randint
imgurUrls=["0CUFPuU.gifv","4JeXPYL.jpg","OUnesDL.jpg","Iq2CH.jpg","dD7yNfY.jpg","a/GRqUA","pKZCq.jpg","EaZSYU1.gifv","LdRVqSL.jpg","tbB9ktj.jpg","GRd85Vc.jpg"]
redditUrls=["84yqig40xm7z.png"]
youtubeUrls=["watch?v=19eFnrSf41A&feature=youtu.be&t=5m39s","watch?v=y1B8vXlH5l4?t=52s","watch?v=pP6jf9aovjM?t=9s","watch?v=vLEe9iHf-FA?t=41s","watch?v=fbngCt4BavU?t=29s","watch?v=ICUluUi6aTc?t=6s","watch?v=KjVLZLsW0do?t=3s"]
liveleakUrls=["view?i=461_1360105026&safe_mode=off","view?i=bb4_1283184704&safe_mode=off","view?i=5e8_1425739036&safe_mode=off"]
otherUrls=["http://33.media.tumblr.com/5743e899731d3604cfbc1871ef64f9dc/tumblr_njk3p6hCUh1unvl7to1_500.gif","https://streamable.com/o3mic"]
def start(slep):
	while(True):
		page=randint(0,4)
		if(page==0): webbrowser.open("https://i.imgur.com/"+imgurUrls[randint(0,len(imgurUrls)-1)])
		elif(page==1): webbrowser.open("https://i.redd.it/"+redditUrls[randint(0,len(redditUrls)-1)])
		elif(page==2): webbrowser.open("https://www.youtube.com/"+youtubeUrls[randint(0,len(youtubeUrls)-1)])
		elif(page==3): webbrowser.open("https://www.liveleak.com/"+liveleakUrls[randint(0,len(liveleakUrls)-1)])
		elif(page==4): webbrowser.open(otherUrls[randint(0,len(otherUrls)-1)]
		time.sleep(slep)
