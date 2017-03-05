"""For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,so 15 rounds up to 20.
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5,
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values."""

def round10(num):
  fNum=num/float(10)
  if(float(str(fNum)[len(str(fNum))-1])>=5):
    return(int(fNum)+1)*10
  else:
    return(int(fNum))*10
  
def round_sum(a, b, c):
  return(round10(a)+round10(b)+round10(c))
