import webbrowser
#import urllib
from urllib.request import urlopen, Request

headers = {‘User-Agent’: ‘Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3’}
url="https://tunebat.com/Search?q=Space+Oddity+"
page=Request(url=url, headers=headers)
print(urlopen(page).read())
"""while(page.readline()):
	lne=page.readline()
	print(lne)"""
#f=urllib.request.urlopen(url)
#print(f.read())
