import csv

fuel = []

with open ("inputDay1.csv") as input:
	input_parsed = csv.reader(input)
	masses = []
	for row in input_parsed:
		masses.append(row[0])

for i in masses:
	i = int(i)
	i = int(i/3)-2
	fuel.append(i)

print (sum(fuel))