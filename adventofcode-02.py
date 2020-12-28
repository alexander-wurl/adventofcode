#!/usr/bin/env python3

import helper

f = helper.getData("02")

solution = 0

for line in f:
	w = line.split(" ")
	mm = w[0].split("-")
	min = mm[0]
	max = mm[1]
	c = w[1][0]
	count = w[2].count(c)

	if (count >= int(min)) and (count <= int(max)):
		solution += 1
		print("OK " + str(solution))

print("FINAL SOLUTION:" + str(solution))
