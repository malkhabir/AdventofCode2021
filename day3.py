theInput = []
myInput = []
verticalView = []
temP = ""
output0 = ""
output1 = ""

#Read file in a list
with open("day3_input.txt", "r") as adventofcodeInput:
    theInput = adventofcodeInput.readlines()
    for line in theInput:
        myInput.append(line.strip('\n'))

#Test of a smaller input
#with open("small3.txt", "r") as adventofcodeInput:
#     theInput = adventofcodeInput.readlines()
#     for line in theInput:
#         myInput.append(line.strip('\n'))

#loop on chr per lines
#verticalview is literally vertical view of the bits.
#eg: 010
#    011
#the vertical view is 00, 11, 01.
for chr in range(len(myInput[0])):
    for line in myInput:
        temP += line[chr]
    verticalView.append(temP)
    temP = ''



#functions to return the chr with the most or least appearance in a given strinf "lines"
def get_thebit_max(lines):
    #Takes a string of bit as input and will return the most freq element as
    #per AOC conditions.

    chrFreq = {'0' : 0, '1' : 0}

    for chr in lines:
        if chr in lines:
            chrFreq[chr] += 1
        else:
            chrFreq[chr] += 1

    maxi = max(chrFreq, key = chrFreq.get)
    mini = min(chrFreq, key = chrFreq.get)

    return maxi

def get_thebit_mini(lines):
        #Takes a string of bit as input and will return the least freq element as
        #per AOC conditions.

        chrFreq = {'0' : 0, '1' : 0}

        for chr in lines:
            if chr in lines:
                chrFreq[chr] += 1
            else:
                chrFreq[chr] += 1

        mini = min(chrFreq, key = chrFreq.get)

        return mini

def binary_to_decimal(binary):
    decimal = 0
    theLength = len(binary) - 1
    for i in binary:
        decimal += int(i) * ((2) ** (theLength))
        theLength -= 1
        if theLength < 0:
            break
    return decimal

#Use of function on my verticalviews.
for elements in verticalView:
    output0 += get_thebit_max(elements)

for elementia in verticalView:
    output1 += get_thebit_mini(elementia)


gammaRate = output0
epsilonRate = output1

print(gammaRate, epsilonRate, binary_to_decimal(gammaRate),  binary_to_decimal(epsilonRate))
print("The power consumption of the submarine is {0}".format(binary_to_decimal(gammaRate)*binary_to_decimal(epsilonRate)))
