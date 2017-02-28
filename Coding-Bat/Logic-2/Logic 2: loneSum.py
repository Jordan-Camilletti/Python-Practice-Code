"""Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values, it does not count towards the sum."""

def lone_sum(a, b, c):
  if(a==b and a==c):
    return 0
  elif(a==c):
    return b
  elif(b==c):
    return a
  elif(a==b):
    return c
  return a+b+c
