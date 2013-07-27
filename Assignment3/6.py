import math
import json
import pprint

def area(vertices):
	x = 0
	y = 1
	a = 0
	for i in range(len(vertices)-1):
		a += (vertices[i][x]*vertices[i+1][y])-(vertices[i][y]*vertices[i+1][x])
	a += (vertices[-1][x]*vertices[0][y] - vertices[-1][y]*vertices[0][x])
	a = a/2
	return abs(a)

def polygonarea(json_polygons):
	for item in json_polygons:
		for c in item["geometry"]["coordinates"]:
			print "polygon area:",area(c)

us_mall = open("7_usa_nationalmall.geojson")

us_mall_json = json.load(us_mall)

print "us mall polys"
polygonarea(us_mall_json)

us_mall.close()

gilberto_polys = open("polys.json")

gilberto_polys_json = json.load(gilberto_polys)

print "given polygon areas:"
polygonarea(gilberto_polys_json)

gilberto_polys.close()



	

