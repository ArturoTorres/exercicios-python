# this should: print( smaller( [1, 7, 2, 3, 0, 6], 4) )  # [1, 2, 3, 0]

def smaller(list,number):
	smallers = []
	for item in list: 
		if item < number: 
			smallers.append(item)
	return smallers

print(smaller( [1, 7, 2, 3, 0, 6], 4) )
	