"""Given a string, return a string where for every char in the original, there are two chars."""

def double_char(str):
  wrd=""
  for x in range(len(str)):
    wrd=wrd+str[x]+str[x]
  return wrd
