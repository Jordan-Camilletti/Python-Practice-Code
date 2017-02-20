from collections import deque
import heapq

def smallest(num, col):
	newLst=deque(maxlen=num)
	heap=list(col)
	heapq.heapify(heap)
	for x in range(num):
		newLst.append(heapq.heappop(heap))
	return(newLst)
	

col=[3,6,8,1,5,8,3,9,4,2]
#print(largest(2,list))
print(smallest(2,col))
