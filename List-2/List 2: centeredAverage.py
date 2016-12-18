"""Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value."""

def centered_average(nums):
  large=nums[0]
  small=nums[0]
  tot=0
  for x in nums:
    tot=tot+x
    if(x>large):
      large=x
    if(x<small):
      small=x
  tot=tot-large-small
  return(tot/(len(nums)-2))
