"""This is a basic replace letter cipher("A"~>"X", "B"~>"E", etc)
It works on cipher words and their normal counterparts supplied by the user
If given enough data, it can translate ciphered and normal messages"""

alphC=[]#Cipher 'alphabet'
alphN=[]#Normal 'alphabet'
choice=""
cText=""
nText=""
while(choice.upper()!="EXIT"):
	print("\nNormal:",alphN,"\nCipher:",alphC)
	choice=input("Input, Output, or Exit?\n")
	if(choice.upper()=="INPUT"):
		cText=input("Enter ciphered text.\n").upper()
		nText=input("Enter normal text.\n").upper()
		for n in range(len(cText)):
			if(cText[n] not in alphC):
				alphC.append(cText[n])
				alphN.append(nText[n])
	elif(choice.upper()=="OUTPUT"):
		if(input("Cipher -> Normal (1)\nNormal -> Cipher(2)\n")=="1"):
			cText=input("Enter ciphered text.\n").upper()
			nText=""
			for n in cText:
				if(n in alphC):
					nText+=alphN[alphC.index(n)]
				else:
					nText+="᏿"#Best thing I could find for 'unknown'
			print(nText)
		else:
			nText=input("Enter normal text.\n").upper()
			cText=""
			for n in nText:
				if(n in alphN):
					cText+=alphC[alphN.index(n)]
				else:
					cText+="᏿"
			print(cText)
