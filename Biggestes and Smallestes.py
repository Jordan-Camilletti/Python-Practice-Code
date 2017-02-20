from collections import deque

def largest(num, list):
	newLst=deque(maxlen=num)
	for x in range(num):
		newLst.append(list[0])
	return newLst

def smallest(num, list):
	newLst=deque(maxlen=num)
	for x in range(num):
		newLst.append(list[0])
	return newLst
		
list=[0,1,2,3,4,5,6,7,8,9]
print(largest(2,list))
print(smallest(2,list))
