def check_for_repeats(number):
	number = str(number)
	count = {}
	for i in range(len(number)):
		
	return False

def check_for_increasing(number):
	number = str(number)
	for i in range(1,len(number)):
		if any(number[i] < x for x in number[:i]):
			return False
	return True

rangeLower = 372037
rangeUpper = 905157
listofnumbers = []

for j in range(rangeLower,rangeUpper):
	if check_for_repeats(j) == True:
		if check_for_increasing(j) == True: listofnumbers.append(j)

print(len(listofnumbers))