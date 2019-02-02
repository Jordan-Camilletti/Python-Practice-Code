import re
import webbrowser
import urllib.parse
import urllib.request

def getVid(search):#Credit for this function goes to Grant Curell
	query_string = urllib.parse.urlencode({"search_query" : search})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	return("http://www.youtube.com/watch?v=" + search_results[0])

header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
song1=""
song2=""
vocalChoice=0
BPM=0
while(BPM==0):
	#Getting the 1st song
	song1=input("Enter Song 1: ").lower()
	url1="https://songbpm.com/"+(song1.lower().replace(" ","-"))
	pageBytes=urllib.request.urlopen(urllib.request.Request(url1,headers=header))
	page=pageBytes.read().decode("utf8").split("\n")
	try:
		#Getting the BPM of the 1st song
		BPM=int(re.split('[<>]',page[101])[2])
		song1=page[88]+" by "+page[85]
	except ValueError:
		#Song doesn't exist
		print("That song's BPM was not found.")
pageBytes.close()

#Looking up 2nd song by BPM
url2="https://jog.fm/popular-workout-songs?bpm="+str(BPM)
pageBytes=urllib.request.urlopen(urllib.request.Request(url2,headers=header))
page=pageBytes.read().decode("utf8").split("\n")
#Getting the BPM of the 2nd song
song2=re.split('[<>]',page[528])[4]+" by "+re.split('[<>]', page[527])[4]
pageBytes.close()

#Showing both songs
while(vocalChoice!=1 and vocalChoice!=2):
	print("Song 1: "+song1+"\nSong 2: "+song2+"\nBPM: "+str(BPM)+"Which song do you want vocals for?")
vocalChoice=input()
if(vocalChoice==1):
	webbrowser.open(getVid(song1+" vocals"))#Vocals
	webbrowser.open(getVid(song2+" instrumentals"))#Instrumentals
else:
	webbrowser.open(getVid(song1+" instrumentals"))#Instrumentals
	webbrowser.open(getVid(song2+" vocals"))#Vocals
