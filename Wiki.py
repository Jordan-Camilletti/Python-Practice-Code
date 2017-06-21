"""
"""

import webbrowser
import urllib.request
print("Enter starting prompt")
prompt=input()
route=[]
while(prompt not "Philosophy"):
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
	line=lne.decode("utf-8")
	for x in range(len(line)):
		if(line[x-15:x]=='<a href="/wiki/'):
			newWrd=line[x:]
			for n in range(len(newWrd)):
				try:
					if(newWrd[n]!='"'):
						prompt+=newWrd[n]
					else:
						newWrd=""
				except IndexError:
					print(prompt)
					lnk_found=True
					break
		if(lnk_found):
			break
	print(prompt)
print(route)
