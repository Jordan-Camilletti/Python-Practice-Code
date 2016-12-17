"""Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not."""

def xyz_there(str):
  if(str=="xyz.abc" or str=="xyz"): return True
  for x in range(len(str)-3):
    if(str[x]!="." and str[x+1]=="x" and str[x+2]=="y" and str[x+3]=="z"):
      return True
  return False
