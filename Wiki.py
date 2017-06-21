"""This plays a game based on the notion that all 1st links on wikipedia lead to https://en.wikipedia.org/wiki/Philosophy
https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy this is a page better explaining the game"""

import webbrowser
import urllib.request
print("Enter starting prompt")
prompt=input()
route=[]
while(prompt!="Philosophy" and prompt!="Philosophical"):
	route.append(prompt)
	url="https://en.wikipedia.org/wiki/"+prompt
	prompt=""
	lnk_found=False
	webbrowser.open(url)
	page=urllib.request.urlopen(url)
	while(page.readline() or lnk_found==False):
		lne=page.readline()
		if(b'<p>' in lne and b'<a href="/wiki/' in lne):
			lnk_found=True
			break
	lnk_found=False
	par=False
	line=lne.decode("utf-8")
	for x in range(len(line)):
		if(line[x]=="("):
			par=True
		if(line[x]==")"):
			par=False
		if(not par):
			if(line[x-15:x]=='<a href="/wiki/'):
				newWrd=line[x:]
				for n in range(len(newWrd)):
					try:
						if(newWrd[n]!='"'):
							prompt+=newWrd[n]
						else:
							newWrd=""
					except IndexError:
						lnk_found=True
						break
		if(lnk_found):
			break
	print(prompt)
	if(prompt in route):
		print("Endless loop encountered!")
		break
print(route)
