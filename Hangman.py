"""This uses a randomly selected word or a user input word and plays hangman with it."""

from random import randint

wordBank=["test1","test2","test3"]
word=(wordBank[randint(0,len(wordBank)-1)])
tries=6
while(tries!=0):
	tries-=1
	str=""
	for x in range(len(word)):
		str+="_"
	print(str)
