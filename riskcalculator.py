import csv

list1 = []
newlist = []
newlist1 = []

with open("data.csv", 'r', newline='') as csvfile:
    read = csv.reader(csvfile)
    for i in read:
        list1.append(i)


def calculate(scene, mask, talk, distance):
    count = 0
    while count < 3:
        newlist.append(list1[(scene*3)+count-1])
        count += 1
    # print(newlist)
    # print(newlist[mask-1][3])
    talking = (talk*3)
    risk = newlist[mask-1][talking+distance-3]
    print("Risk of getting CoVID-19 is", risk, "in a million")


#calculate(4, 3, 2, 2)
# list[row][column]
