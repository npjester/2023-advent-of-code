import os
import re

input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day3/input.txt")

def findNumbersAdjacentToSymbols():
    inputObject = {}
    lineNumber = 0
    partNumberTotal = 0
    ## Must be a better way to do this lines to array thing...
    for line in input.readlines():
        inputObject[lineNumber] = line
        lineNumber += 1
    for line in inputObject:
        numberMatches = re.finditer(r'([0-9]+)', inputObject[line])
        #print(line)
        for match in numberMatches:
            matchStart = match.start()
            matchEnd = match.end() # rework this to not need to check if we are on first or last line maybe inputObject length? inputObject Count so it's any size object
            prevLine = 0 if line == 0 else line - 1
            nextLine = len(inputObject)-1 if line == len(inputObject)-1 else line + 1
            minStart = 0 if matchStart == 0 else matchStart - 1
            maxEnd = len(inputObject[line])-1 if matchEnd == len(inputObject[line])-1 else matchEnd + 1
            stringToSearch = inputObject[prevLine][minStart:maxEnd] + inputObject[line][minStart:maxEnd] + inputObject[nextLine][minStart:maxEnd]
            print(stringToSearch)
            symbolsString = re.sub(r'\d+','',stringToSearch)
            print(symbolsString)
            symbolMatch = re.match(r'.*[^\.].*',symbolsString)
            if symbolMatch:
                print("Symbol")
                partNumberTotal += int(match[0])
            else:
                print("No Symbol")
    return partNumberTotal

def main():
    partNumberSum = findNumbersAdjacentToSymbols()
    print(partNumberSum)

if __name__ == "__main__":
    main()