import csv

fuel = []

with open('day1_input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for row in csv_reader:
        fuel.append (int(int(row[0])/3)-2)
        while True:
            remaining = int(fuel[-1]/3)-2
            if remaining > 0: fuel.append(remaining)
            else: break
print(sum(fuel))