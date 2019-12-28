def update_location(instruction, x,y):
	direction = instruction[:1]
	distance = re.findall(r"\d+", instruction)

	for i in range(0,int(distance[0])):
		x_update = 0
		y_update = 0
		if direction == "R": x_update = 1
		elif direction == "L": x_update = -1
		elif direction == "U": y_update = 1
		elif direction == "D": y_update = -1

		x.append(x[-1]+x_update)
		y.append(y[-1]+y_update)

	#print (direction)
	#print (distance)

def shortest_path(matches,path_1,path_2):
	listofpaths = []
	for x in matches:
		pathlength = path_1.index(x) + path_2.index(x) + 2
		listofpaths.append(pathlength)
	return(min(listofpaths))

filename = "inputDay3.txt"

file = open(filename,"r")
input1 = file.readline()
input2 = file.readline()
input1 = input1.strip().split(',')
input2 = input2.strip().split(',')

def concatenate_coordinates(x,y):
	concatenated = []
	seperator = ','
	for i in range(1,len(x)):
		concatenated.append(seperator.join([str(x[i]),str(y[i])]))
	return concatenated

#instructions = [int(val) for val in inputString]

import re

#inputString = "R75,D30,R83,U83,L12,D49,R71,U7,L72,U62,R66,U55,R34,D71,R55,D58,R83"
#inputString = inputString.strip().split(',')

x_1 = [0]
y_1 = [0]
x_2 = [0]
y_2 = [0]

# input1 = "R8,U5,L5,D3"
# input2 = "U7,R6,D4,L4"
# input1 = input1.strip().split(',')
# input2 = input2.strip().split(',')
# print(input1)
# print(input2)

for next_instruction in input1:
	update_location(next_instruction,x_1,y_1)

for next_instruction in input2:
	update_location(next_instruction,x_2,y_2)

print(len(x_1)+len(x_2)-2)

distance = []

combined_1 = concatenate_coordinates(x_1,y_1)
print("Combined 1")
combined_2 = concatenate_coordinates(x_2,y_2)
print("Combined 2")

matches = set(combined_1).intersection(set(combined_2))
print(shortest_path(matches,combined_1,combined_2))
#print(calc_distance(matches))


# for i in range(1,len(combined_1)):
# 	if combined_1[i] in combined_2:
# 		distance.append(calc_distance(x_1[i],y_1[i]))
# 		print("Match")
# 	if i%100 == 0:
# 		print(i)


#Compare X1 to X2 in list
#If there's a match, look at Y1 and Y2
