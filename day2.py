theInput = []
myInput = []
myKeys = []
myValues = []
sumForwards = 0
sumUps = 0
sumDowns = 0

with open("day2_input.txt", "r") as adventofcodeInput:
        theInput = adventofcodeInput.readlines()
        for line in theInput:
            myInput.append(line.strip('\n'))

for ele in myInput:
    myValues.append(int(ele.split(" ")[1]))

for ele in myInput:
    myKeys.append(ele.split(" ")[0])


sumOfMoves = list(zip(myKeys, myValues))

for ele in range(len(sumOfMoves)):
    if sumOfMoves[ele][0] == 'forward':
        sumForwards = sumOfMoves[ele][1] + sumForwards

    elif sumOfMoves[ele][0] == 'up':
        sumUps = sumOfMoves[ele][1] + sumUps

    elif sumOfMoves[ele][0] == 'down':
        sumDowns = sumOfMoves[ele][1] + sumDowns


# print(myInput)
# print(myKeys)
# print(myValues)
# print(sumOfMoves[0][1])
print(sumForwards, sumDowns, sumUps)
print("We have a horizontal position of {0} and a depth of {1} (Multiplying these together produces {2}.)".format(sumForwards,sumDowns-sumUps,(sumForwards*(sumDowns-sumUps))))
