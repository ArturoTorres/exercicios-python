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


# another option
import json
file_name = "feature_collection.geojson"
f = open(file_name, "r") # r = read, w = write
document = f.read()

as_dict = json.loads(document)

level = ""
def print_keys(obj, level):
		if(type(obj) == type({})):
			lev = level + "."
			for k, v in obj.iteritems():
				print lev, k, v
				#print k, v
				print_keys(v, lev)
		elif (type(obj)== type([])):
			lev = level + "."
			for item in obj:
				print_keys(item, lev)

print_keys(as_dict, level)
