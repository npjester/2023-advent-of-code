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

def getPowerSum(gamesDictMax):
    totalPower = 0
    for game in gamesDictMax:
        gamePower = 0
        gamePower = gamesDictMax[game]['redMax'] * gamesDictMax[game]['blueMax'] * gamesDictMax[game]['greenMax']
        totalPower += gamePower
    return totalPower
    
def main():
    gamesDictMax = getGamesMax()
    powerSum = getPowerSum(gamesDictMax)
    print(powerSum)


if __name__ == "__main__":
    main()