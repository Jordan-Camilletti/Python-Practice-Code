import re
import webbrowser
import urllib.request

header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
song1=""
song2=""
BPM=0
while(BPM==0):
	song1=input("Enter Song 1: ").lower()
	url1="https://songbpm.com/"+(song1.lower().replace(" ","-"))
	pageBytes=urllib.request.urlopen(urllib.request.Request(url1,headers=header))
	page=pageBytes.read().decode("utf8").split("\n")
	try:
		BPM=int(re.split('[<>]',page[101])[2])
		song1=page[88]+" by "+page[85]
	except ValueError:
		print("That song was not found.")
pageBytes.close()
print(song1)

url2="https://www.bpmdatabase.com/music/search/?artist=&title=&bpm="+str(BPM)+"&genre="
pageBytes=urllib.request.urlopen(urllib.request.Request(url2,headers=header))
page=pageBytes.read().decode("utf8").split("\n")
song2=re.split('[<>]',page[517])[2]
print(song2)
pageBytes.close()
