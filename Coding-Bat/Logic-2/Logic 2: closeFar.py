"""Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1)
, while the other is "far", differing from both other values by 2 or more"""

def close_far(a, b, c):
  if(abs(b-a)<=1 and abs(c-b)>=2 and abs(c-a)>=2):#b is close, c is far
    return True
  if(abs(c-a)<=1 and abs(b-c)>=2 and abs(b-a)>=2):#c is close, b is far
    return True
  return False
