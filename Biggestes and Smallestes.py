#This takes a array of numbers, 'col', and returns a list of specified length, 'num', of the biggest or smallest numbers

from collections import deque
import heapq

def largest(num, col):
	newLst=deque(maxlen=num)
	for x in sorted(col):
		newLst.append(x)
	return(newLst)
	
def smallest(num, col):
	newLst=deque(maxlen=num)
	heap=list(col)
	heapq.heapify(heap)
	for x in range(num):
		newLst.append(heapq.heappop(heap))
	return(newLst)

col=[3,6,8,1,5,8,3,9,4,2]
print(largest(2,col))
print(smallest(2,col))
