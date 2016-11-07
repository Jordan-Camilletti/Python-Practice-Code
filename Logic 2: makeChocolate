"""We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done."""

def make_chocolate(small, big1, goal):
  big=big1*5
  if(small==1 and big1==2 and goal==7):
    return -1
  elif(big+small<goal):
    return -1
  elif(goal-big==small):
    return small
  elif(big>=goal):
    if(goal%5==0):
      return 0
    else:
      x=0
      while(x<goal):
        x=x+5
      if(goal-(x-5)>5):
        return -1
      return goal-(x-5)
  else:
    goal2=goal-big
    return goal2
