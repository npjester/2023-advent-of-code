import os
import re
from functools import reduce

input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day2/input.txt")

def getGamesMax():
    gamesDict = {}
    for line in input.readlines():
        gameNum = re.findall('Game (\d+):.*', line)
        redMax = max(map(int,re.findall('(\d+) red', line)))
        blueMax = max(map(int,re.findall('(\d+) blue', line)))
        greenMax = max(map(int,re.findall('(\d+) green', line)))
        if gameNum:
            gamesDict[gameNum[0]] = {}
            gamesDict[gameNum[0]]["redMax"] = redMax
            gamesDict[gameNum[0]]["greenMax"] = greenMax
            gamesDict[gameNum[0]]["blueMax"] = blueMax
    return gamesDict

def getGamesThatMatch():
    gameMatchDict = {"redMax" : 12, "greenMax" : 13, "blueMax" : 14}
    gamesDictMax = getGamesMax()
    totalSum = 0
    for game in gamesDictMax:
        if gamesDictMax[game]['redMax'] <= gameMatchDict['redMax'] and gamesDictMax[game]['greenMax'] <= gameMatchDict['greenMax'] and gamesDictMax[game]['blueMax'] <= gameMatchDict['blueMax']:
           totalSum += int(game)
    #print(totalSum)
    return totalSum

def main():
    matchingGamesTotal = getGamesThatMatch()
    print(matchingGamesTotal)
    ## do the things with the numbers and seeing which meet criteria....


if __name__ == "__main__":
    main()