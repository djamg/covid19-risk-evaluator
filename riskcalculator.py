import csv
import time

list1 = []


def createlist():
    with open("./data.csv", 'r', newline='') as csvfile:
        read = csv.reader(csvfile)
        for i in read:
            list1.append(i)


createlist()
time.sleep(1)


def calculate(scene, mask, talk, distance):
    newlist = []
    count = 0
    while count < 3:
        newlist.append(list1[(scene*3)+count-1])
        count += 1
    # print(newlist)
    # print(newlist[mask-1][3])
    talking = (talk*3)
    risk = newlist[mask-1][talking+distance-3]
    risk_percentage = float(risk)/10000
    return [risk, risk_percentage]
    # return[("Risk of getting COVID-19 is", risk,
    #        "in a million that is", risk_percentage, "percent")]


# calculate(1, 3, 3, 3)
# calculate(6, 3, 3, 3)
# calculate(2, 3, 3, 3)

# list[row][column]
