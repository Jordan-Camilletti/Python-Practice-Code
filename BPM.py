import webbrowser
import urllib.request

header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
song1=input("Enter Song 1: ").lower()
song2=""
BPM=0
#url="https://songbpm.com/space-oddity?q=Space%20Oddity%20"#Using this URL to test for now
url="https://songbpm.com/"+(song1.lower().replace(" ","-"))
pageBytes=urllib.request.urlopen(urllib.request.Request(url,headers=header))
page=pageBytes.read().decode("utf8").split("\n")
pageBytes.close()
print(page[101])
