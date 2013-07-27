import math
import json
import pprint

json_file = open("polys.json")

data = json.load(json_file)

def area(vertices):
	x = 0
	y = 1
	a = 0
	for i in range(len(vertices)-1):
		a += vertices[i][x]*vertices[i+1][y]-vertices[i][y]*vertices[i+1][x]
		print vertices[i][x]*vertices[i+1][y]-vertices[i][y]*vertices[i+1][x]

	print a

for item in data:
	for c in item["geometry"]["coordinates"]:
		area(c)
