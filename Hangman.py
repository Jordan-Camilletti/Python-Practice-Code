"""This uses a randomly selected word or a user input word and plays hangman with it."""

from random import randint

def maymay(letter, word, arr):
	for x in range(len(word)):
		if(letter==word[x]):
			arr[x]=letter
	return arr

wordBank=["test1","test2","test3"]#Add an option to allow user to use word bank or use own word
wrd=(wordBank[randint(0,len(wordBank)-1)])
arr=["_"]*(len(wrd))
tries=5
while(tries!=0):#Break if they guess word
	choice=input('Enter a letter')
	tries-=1
	arr=maymay(choice,wrd,arr)
	print(arr)
#Create win/loss message
