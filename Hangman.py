"""This uses a randomly selected word or a user input word and plays hangman with it."""

from random import randint

def maymay(letter, word, arr):
	for x in range(len(word)):
		if(letter==word[x]):
			arr[x]=letter
	return arr

wordBank=["test1","test2","test3"]
if(input('Do you want to use your own word? Y/N\n')=="Y"):
	wrd=input('Enter your word\n')
else:
	wrd=(wordBank[randint(0,len(wordBank)-1)])
arr=["_"]*(len(wrd))
tries=5
while(tries!=0):#Break if they guess word
	choice=input("Enter a letter\n")
	tries-=1
	arr=maymay(choice,wrd,arr)
	for x in arr:
		if x==choice:
			tries+=1
			break
	print(arr," tries left:", tries)
#Create a win/loss message
