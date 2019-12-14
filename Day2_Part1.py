file = open("inputDay2.txt","r")
inputString = file.read()
inputString = inputString.strip().split(',')
instructions = [int(val) for val in inputString]
#instructions = [2,4,4,5,99,0]

print (instructions)

i = 0

instructions[1] = 12
instructions[2] = 2

while True:
	command = instructions[i]
	ref_1 = instructions[i+1]
	ref_2 = instructions[i+2]
	ref_3 = instructions[i+3]
	#print (command)
	if command == 1:
		instructions[ref_3] = instructions[ref_1] + instructions[ref_2]
	elif command == 2:
		instructions[ref_3] = instructions[ref_1] * instructions[ref_2]
	i = i+4
	print (instructions[i])
	if instructions[i] == 99: break

print (instructions)