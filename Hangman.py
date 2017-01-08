"""This uses a randomly selected word or a user input word and plays hangman with it."""
from random import randint

wordBank=["test1","test2","test3"]
print(wordBank[randint(0,len(wordBank)-1)])
