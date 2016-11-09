"""Given 3 int values, a b c, return their sum.
However, if any of the values are in the range 13..19 inclusive then that value counts as 0, except 15 and 16 do not count as a teens."""

def no_teen_sum(a, b, c):
  if(a>12 and a<15)or(a>16 and a<20):
    a=0
  if(b>12 and b<15)or(b>16 and b<20):
    b=0
  if(c>12 and c<15)or(c>16 and c<20):
    c=0
  return a+b+c
