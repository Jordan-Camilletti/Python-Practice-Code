"""
"""

import webbrowser
import urllib.request
print("Enter starting prompt")
prompt=input()
route=[]
route.append(prompt)
url="https://en.wikipedia.org/wiki/"+prompt
lnk=""
#webbrowser.open(url)
page=urllib.request.urlopen(url)
while(page.readline()):
	lne=page.readline()
	if(b'<p>' in line and b'<a href="/wiki/' in lne):
		line=lne.decode("utf-8")
		for x in range(len(line)):
			if(line[x-15:x]=='<a href="/wiki/'):
			newWrd=line[x:]
			for n in range(len(newWrd)):
				if(newWrd[n]!='"'):
					lnk+=newWrd[n]
				else:
					print(lnk)
					break

print(route)

"""lne=b'<p><b>Water</b> is a transparent and nearly colorless <a href="/wiki/Chemical_substance" title="Chemical substance">chemi'
line=lne.decode("utf-8")
for x in range(len(line)):
	if(line[x-15:x]=='<a href="/wiki/'):
		newWrd=line[x:]
		for n in range(len(newWrd)):
			if(newWrd[n]!='"'):
				lnk+=newWrd[n]
			else:
				print(lnk)
				break"""
