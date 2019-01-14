import webbrowser
#import urllib
from urllib.request import urlopen, Request

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url="https://tunebat.com/Search?q=Space+Oddity+"
page=Request(url, headers)
print(urlopen(page).read())
"""while(page.readline()):
	lne=page.readline()
	print(lne)"""
#f=urllib.request.urlopen(url)
#print(f.read())
