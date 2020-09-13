import csv

list1 = []

with open("data.csv", 'r', newline='') as csvfile:
    read = csv.reader(csvfile)
    for i in read:
        list1.append(i)

# list[row][column]
for rows in list1:
    print(rows[10])
