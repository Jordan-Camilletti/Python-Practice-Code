"""Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count."""

def sum13(nums):
  tot=0
  for x in range(len(nums)):
    if(x==0):
      if(nums[x]!=13):
        tot=tot+nums[x]
    else:
      if(nums[x]!=13 and nums[x-1]!=13):
        tot=tot+nums[x]
  return tot
