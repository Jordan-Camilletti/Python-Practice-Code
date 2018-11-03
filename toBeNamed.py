"""most likely getting data from wiki script"""

import webbrowser
import urllib
from urllib.request import urlopen

#Starting year is 1792
#The voter turnout percentage is always the first number on line 52
year=1792
percents=[]

url="https://en.wikipedia.org/wiki/United_States_presidential_election,_"+str(year)
#webbrowser.open(url)
print(list(enumerate(urllib.request.urlopen(url)))[51])#Gets the specific line