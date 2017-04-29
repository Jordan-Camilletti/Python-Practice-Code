"""this is an upside down pascal triangle done using recursion only"""

def tri(topLevel, currLevel, triangle):
	triangle=triangle+"*"
	if(topLevel==1):
		triangle=triangle+"\n"
		return triangle
	if(currLevel==1):
		triangle=triangle+"\n"
		return tri(topLevel-1,topLevel-1,triangle)
	return tri(topLevel,currLevel-1,triangle)

print(tri(5, 5,""))
