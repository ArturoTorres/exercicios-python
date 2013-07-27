import math
import json
import pprint

json_file = open("lines.json")

data = json.load(json_file)


def distance(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	dx2 = (x2-x1)**2
	dy2 = (y2-y1)**2

	return math.sqrt(dx2+dy2)

for index, item in enumerate(data):
	d = 0
	for c in item["coordinates"]:
		if 'c_one' in locals():
			d += distance(c_one,c)
		else:
			c_one = c
	print "length of line #",index+1,":",d	

