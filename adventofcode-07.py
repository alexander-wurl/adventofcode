#!/usr/bin/env python3

def substitute(shinygoldrules, rules):
  for r in rules:  
    for g in shinygoldrules:  
      if (r[1].find(g[0][:-1])>-1):  
        temp = [str(r[0]), str(r[1].replace(g[0][:-1], g[1]))] 
        shinygoldrules.append(temp)
  return shinygoldrules

def finduniqe(rules):
  leftside = []
  leftside = [e[0] for e in rules]
  ret = []
  for e in leftside:
    if (e not in ret):
      ret.append(e)
  return ret

# main
fileid = open("input-07.txt")
data = fileid.read()

rules = []
rules = data.split("\n")[:-1] 

splittedrules = []
splittedrules = [x.split(" contain ") for x in rules] 

shinygoldrules = []
for e in splittedrules: 
  if (e[1].find("shiny gold bag")>-1): 
    shinygoldrules.append(e)

solution = 0

while True:
  shinygoldrules = substitute(shinygoldrules, splittedrules)
  l = len(finduniqe(shinygoldrules))
  if ( l > solution):
      solution = l
  else:
      break

print("final solution: " + str(solution) )
