import math
import json
import pprint
from operator import itemgetter

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
			linerelations.append([line1_vertex,line2_vertex,distance(line1_vertex,line2_vertex)])

linerelations.sort(key=itemgetter(2))

pprint.pprint(linerelations)

print "closest vertices:"
print "line 1:", linerelations[0][0]
print "line 2:", linerelations[0][1]