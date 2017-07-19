"""This script allows you to records multiple string values and the amount of times they've been entered. 
It logs the strings and amount values in a text file called 'times.txt'"""

def addTime(time,t):
	for n in range(len(t)):
		if(t[n][0]==time):
			t[n][1]+=1
			return t
	t.append([time,1])
	return t

times=[]
wrd=""
with open("times.txt",'r+') as f:
	for l in f.read():
		if(l!="~" and l!="\n"):
			wrd=wrd+l
		elif(l=="~"):
			num,amount=wrd.split("-")
			times.append([num,int(amount)])
			wrd=""
print("Add time? Y/N")
addMore=input()
while(addMore=="Y"):
	times=addTime(input(),times)
	print("Add more time? Y/N")
	addMore=input()
print(times)
with open("times.txt",'w') as f:
	for num,amount in times:
		f.write(num+"-"+str(amount)+"~\n")
