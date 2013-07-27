import json
import pprint

json_file = open("feature_collection.geojson")

data = json.load(json_file)

for feature in data["features"]:
	for key,value in feature.iteritems():
		print "key:", key
		if type(value) == dict:
			print "value:" 
			pprint.pprint(value)
		else:
			print "value:", value
		print " "

json_file.close
