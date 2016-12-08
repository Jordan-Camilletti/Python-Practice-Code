"""Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
So for example, if a is 13, then a, b, and c do not count."""
def lucky_sum(a, b, c):
  tot=a+b+c
  if(a==13):
    tot=tot-(a+b+c)
  elif(b==13):
    tot=tot-(b+c)
  elif(c==13):
    tot=tot-c
  return tot
