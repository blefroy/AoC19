def run_program(instructions, x, y):
	i = 0
	instructions[1] = x
	instructions[2] = y
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
		#print (instructions[i])
		if instructions[i] == 99: return instructions[0]

def loop_program(instructions):
	for x in range(0,100):
		for y in range (0,100):
			#print(x,y)
			try:
				result = run_program(instructions[:],x,y)
				print (result)
				if result == 19690720: return (x,y)
			except: 
				next

file = open("inputDay2.txt","r")
inputString = file.read()
inputString = inputString.strip().split(',')
instructions = [int(val) for val in inputString]
#instructions = [2,4,4,5,99,0]

#print (instructions)


(noun, verb) = loop_program(instructions)
print("Result:", 100 * noun + verb)

	

