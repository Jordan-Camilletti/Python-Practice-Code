"""most likely getting data from wiki script"""

import webbrowser
import urllib

#Starting year is 1792
#The voter turnout percentage is always the first number on line 52
year=1792
percents=[]

url="https://en.wikipedia.org/wiki/United_States_presidential_election,_"+str(year)
webbrowser.open(url)