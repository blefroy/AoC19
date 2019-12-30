def check_for_repeats(number):
	number = str(number)
	count = [0]*10
	toggle = 0
	for i in range(0,len(number)):
		count[int(number[i])] += 1

	#print(count)
	return bool([x for x in count if x == 2])

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

#print(listofnumbers)
print(len(listofnumbers))