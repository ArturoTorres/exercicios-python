import math
import json
import pprint

json_file = open("my_lines.json")

data = json.load(json_file)

def distance(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	dx2 = (x2-x1)**2
	dy2 = (y2-y1)**2

	return math.sqrt(dx2+dy2)

linerelations = []

for index in range(len(data)-1):
	for line1_vertex in data[index]["coordinates"]:
		for line2_vertex in data[index+1]["coordinates"]:
			linerelations.append({"line1_vertex":line1_vertex,"line2_vertex":line2_vertex,"distance":distance(line1_vertex,line2_vertex)})

pprint.pprint(linerelations)