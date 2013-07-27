import math
import json
import pprint

json_file = open("usa_nationalmall.geojson")

data = json.load(json_file)

def area(vertices):
	x = 0
	y = 1
	a = 0
	for i in range(len(vertices)-1):
		a += (vertices[i][x]*vertices[i+1][y])-(vertices[i][y]*vertices[i+1][x])
	a += (vertices[-1][x]*vertices[0][y] - vertices[-1][y]*vertices[0][x])
	a = a/2
	return abs(a)

for item in data:
	for c in item["geometry"]["coordinates"]:
		print "polygon area:",area(c)


