import os
import re

input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day3/input.txt")

def getNumberMatches(line):
    numberMatches = re.finditer(r'([0-9]+)', line)
    return numberMatches

def getSymbolMatches(line):
    symbolMatches = re.finditer(r'([\*])', line)
    return symbolMatches

def getMatchParams(match, line):
    matchParams = {}
    matchParams["matchStart"] = match.start()
    matchParams["matchEnd"] = match.end()
    matchParams["prevLine"] = 0 if line == 0 else line - 1
    matchParams["nextLine"] = len(inputObject)-1 if line == len(inputObject)-1 else line + 1
    matchParams["minStart"] = 0 if matchParams["matchStart"] == 0 else matchParams["matchStart"] - 1
    matchParams["maxEnd"] = len(inputObject[line]["lineString"])-1 if matchParams["matchEnd"] == len(inputObject[line]["lineString"])-1 else matchParams["matchEnd"] + 1
    return matchParams

def getInputData():
    global inputObject
    global totalSymbolMatches
    global totalNumberMatches
    totalSymbolMatches = 0
    totalNumberMatches = 0
    inputObject = {}
    lineNumber = 0
    for line in input.readlines():
        inputObject[lineNumber] = {}
        inputObject[lineNumber]["lineString"] = line
        inputObject[lineNumber]["numberMatches"] = getNumberMatches(line)
        inputObject[lineNumber]["symbolMatches"] = getSymbolMatches(line)
        totalSymbolMatches += len(list(getSymbolMatches(line)))
        lineNumber += 1

def resetInputDataMatches(lineNumbers):
    #print("Resetting Input Data")
    for lineNumber in lineNumbers:
        inputObject[lineNumber]["numberMatches"] = getNumberMatches(inputObject[lineNumber]["lineString"])
        inputObject[lineNumber]["symbolMatches"] = getSymbolMatches(inputObject[lineNumber]["lineString"])

def checkForAdjacentSymbols(match, line):
    matchParams = getMatchParams(match, line)
    #print(match)
    #print(matchParams)
    stringToSearch = inputObject[matchParams["prevLine"]]["lineString"][matchParams["minStart"]:matchParams["maxEnd"]] + inputObject[line]["lineString"][matchParams["minStart"]:matchParams["maxEnd"]] + inputObject[matchParams["nextLine"]]["lineString"][matchParams["minStart"]:matchParams["maxEnd"]]
    #print(stringToSearch)
    symbolsString = re.sub(r'\d+','',stringToSearch)
    symbolMatch = re.match(r'.*[^\.].*',symbolsString)
    if symbolMatch:
        return True
    return False

def checkForAdjacentNumbers(match, line):
    adjacentRatio = {}
    adjacentRatio["isGear"] = False
    adjacentRatio["gearRatio"] = 0
    matchParams = getMatchParams(match, line)
    adjacentPartNumbers = []
    #print(matchParams)
    #print(f"Checking for adjancency on : {line} at {matchParams['matchStart']} between {matchParams['minStart']} and {matchParams['matchEnd'] }")
    # check previous lines numbermatches to see if they start or end within our adjacency zone
    #print("Checking previous line for numberMatches")
    #print(matchParams["prevLine"])
    resetInputDataMatches([matchParams["prevLine"], line, matchParams["nextLine"]])
    for numberMatch in inputObject[matchParams["prevLine"]]["numberMatches"]:
        #print(numberMatch)
        if(matchParams["minStart"] <= numberMatch.start() <= matchParams["matchEnd"] or matchParams["minStart"] <= numberMatch.end() - 1 <= matchParams["matchEnd"] ):
            #print(f"Found adjancency on Previous Line: {matchParams['prevLine']} with number: {numberMatch[0]}")
            #print(numberMatch)
            adjacentPartNumbers.append(numberMatch[0])
            #print(adjacentPartNumbers)
        #print("Inside Previous Line")
    # check current lines numbermatches to see if they start or end within our adjacency zone
    #print("Checking current line for numberMatches")
    #print(line)
    for numberMatch in inputObject[line]["numberMatches"]:
        #print(numberMatch)
        if(matchParams["minStart"] <= numberMatch.start() <= matchParams["matchEnd"] or matchParams["minStart"] <= numberMatch.end() - 1 <= matchParams["matchEnd"] ):
            #print(f"Found adjancency on Current Line: {line}")
            #print(numberMatch)
            adjacentPartNumbers.append(numberMatch[0])
            #print(adjacentPartNumbers)
        #print("Inside Current Line")
    # check next lines numbermatches to see if they start or end within our adjacency zone
    #print("Checking next line for numberMatches")
    #print(matchParams["nextLine"])
    for numberMatch in inputObject[matchParams["nextLine"]]["numberMatches"]:
        #print(numberMatch)
        if(matchParams["minStart"] <= numberMatch.start() <= matchParams["matchEnd"] or matchParams["minStart"] <= numberMatch.end() - 1 <= matchParams["matchEnd"] ):
            #print(f"Found adjancency on Next Line: {matchParams['nextLine']}")
            #print(numberMatch)
            adjacentPartNumbers.append(numberMatch[0])
            #print(adjacentPartNumbers)
        #print("Inside Next Line")
    resetInputDataMatches([matchParams["prevLine"], line, matchParams["nextLine"]])
    if len(adjacentPartNumbers) == 2:
        #print(f"Adjacent Part Numbers: {adjacentPartNumbers}")
        adjacentRatio['isGear'] = True
        adjacentRatio['gearRatio'] = int(adjacentPartNumbers[0]) * int(adjacentPartNumbers[1])
    return adjacentRatio



def findNumbersAdjacentToSymbols():
    partNumberTotal = 0
    for line in inputObject:
        for numberMatch in inputObject[line]["numberMatches"]:
            #print(numberMatch)
            if checkForAdjacentSymbols(numberMatch, line):
                partNumberTotal += int(numberMatch[0])
    return partNumberTotal

def findSumOfGearRatios():
    adjacentGearRatioSum = 0
    for line in inputObject:
        for symbolMatch in inputObject[line]["symbolMatches"]:
            #print(f"Checking Symbol Match: {symbolMatch}")
            adjacentGearRatio = checkForAdjacentNumbers(symbolMatch, line)
            if adjacentGearRatio["isGear"]:
                adjacentGearRatioSum += adjacentGearRatio["gearRatio"]
    return adjacentGearRatioSum

def main():
    getInputData()
    partNumberSum = findNumbersAdjacentToSymbols()
    gearRatioSum = findSumOfGearRatios()
    print(f"Part Number Sum: {partNumberSum}")
    print(f"Gear Ratio Sum: {gearRatioSum}")
    print(f"Total Symbol Matches: {totalSymbolMatches}")

if __name__ == "__main__":
    main()