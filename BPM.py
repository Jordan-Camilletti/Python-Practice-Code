import webbrowser
import urllib
from urllib.request import urlopen

url="https://tunebat.com/Search?q=Space+Oddity+"
page=urllib.request.urlopen(url)
while(page.readline()):
	lne=page.readline()
	print(lne)
#f=urllib.request.urlopen(url)
#print(f.read())
