#!/usr/bin/env python3

import os

def substitute(shinygoldrules, rules):
  for r in rules:  
    for g in shinygoldrules:  
      if (r[1].find(g[0][:-1])>-1):  
        shinygoldrules.append([str(r[0]), str(r[1].replace(g[0][:-1], g[1]))])
  return shinygoldrules

def findunique(rules):
  leftside = [e[0] for e in rules]
  ret = []
  for e in leftside:
    if (e not in ret):
      ret.append(e)
  return ret

# main
fileid = open(os.path.dirname(__file__) + "/input-07.txt")
data = fileid.read()

rules = data.split("\n")[:-1] 

splittedrules = [x.split(" contain ") for x in rules] 

shinygoldrules = []
for e in splittedrules: 
  if (e[1].find("shiny gold bag")>-1): 
    shinygoldrules.append(e)

solution = 0

while True:
  shinygoldrules = substitute(shinygoldrules, splittedrules)
  l = len(findunique(shinygoldrules))
  if ( l > solution):
      solution = l
  else:
      break

print("solution: " + str(solution) )
