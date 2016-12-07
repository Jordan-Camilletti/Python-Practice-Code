"""Given an array length 1 or more of ints,
return the difference between the largest and smallest values in the array."""

def big_diff(nums):
  bigs=-1
  small=100
  for x in nums:
    if x>bigs:
      bigs=x
    if x<small:
      small=x
  return bigs-small
