"""This is just a simple script I wrote to get the data of US election turnouts """

import webbrowser
import urllib
from urllib.request import urlopen

#Starting year is 1792
#The voter turnout percentage is always the first number on line 52
year=1792
percents=[]

for year in range(1792,2020,4):
  url="https://en.wikipedia.org/wiki/United_States_presidential_election,_"+str(year)
  #webbrowser.open(url)
  print(list(enumerate(urllib.request.urlopen(url)))[51])#Gets the specific line
