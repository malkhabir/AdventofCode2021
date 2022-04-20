LIST = []
INPUT = []
increasesCounter = 0
decreasesCounter = 0

with open("input.txt", "r") as input:
    LIST = input.readlines()
    for ele in LIST:
        INPUT.append(int(ele.strip("\n")))

for ele in range(len(INPUT)):
    if ele - (len(INPUT)-1) == 0:
        break
    else:
        if INPUT[ele + 1] - INPUT[ele] > 0:
            increasesCounter = increasesCounter + 1
        else:
            decreasesCounter = decreasesCounter + 1

print(increasesCounter)
print(decreasesCounter)
