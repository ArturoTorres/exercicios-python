def get_odd(list):
	odds = []
	for item in list:
		number = item
		if number%2 != 0:
			odds.append(number)
	return odds

print( get_odd( [1, 7, 2, 3, 0, 6]) ) # [1, 7, 3]

