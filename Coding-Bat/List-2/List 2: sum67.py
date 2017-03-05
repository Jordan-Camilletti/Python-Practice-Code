"""Return the sum of the numbers in the array,
except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7).
Return 0 for no numbers."""

def sum67(nums):
  tot=0
  current=False
  for x in nums:
    if(x==6):
      current=True
    if(x==7):
      if(current):
        tot=tot-7
      current=False
    if(current==False):
      tot=tot+x
  return(tot)
