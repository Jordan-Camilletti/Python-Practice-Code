"""Given two strings, 
return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences"""

def end_other(ab, ba):
  a=ab.lower();
  b=ba.lower();
  if(len(a)>len(b)):
    return(b==a[len(a)-len(b):]);
  else:
    return(a==b[len(b)-len(a):]);
