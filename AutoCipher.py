"""
"""

alphC=[]#Cipher 'alphabet'
alphN=[]#Normal 'alphabet'
choice=""
cText=""
nText=""
while(choice.upper()!="EXIT"):
    choice=input("Input, Output, or Exit?\n")
    if(choice.upper()=="INPUT"):
        cText=input("Enter ciphered text.\n").upper()
        nText=input("Enter normal text.\n").upper()
        for n in range(len(cText)):
        	alphC.append(cText[n])
        	alphN.append(nText[n])
    elif(choice.upper()=="OUTPUT"):
        if(input("Cipher -> Normal (1)\nNormal -> Cipher(2)\n")=="2"):
            cText=input("Enter normal text.\n")
            for n in cText:
                if(n in alphC):
                    nText+=alphN[alphC.index(n)]
                else:
                    nText+="᏿"
            print(nText)
        else:
            nText=input("Enter ciphered text.\n")
            for n in nText:
                if(n in alphN):
                    cText+=alphC[alphN.index(n)]
                else:
                    cText+="᏿"
            print(cText)
