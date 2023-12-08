import os
import re

input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day4/input.txt")
global numberOfWinningCards
numberOfWinningCards = 0

def getInput():
    global allScratchCards
    allScratchCards = {}
    for line in input.readlines():
        scratchCardDetails = re.search(r'Card\s+(?P<cardNumber>\d+):\s+(?P<winningNumbers>.*)\s+\|\s+(?P<gameNumbers>.*)$', line) # lets use named matches to get all the data in one go....
        scratchCardNumber = int(scratchCardDetails.group('cardNumber'))
        winningNumbers = list(map(int,scratchCardDetails.group('winningNumbers').split()))
        gameNumbers = list(map(int,scratchCardDetails.group('gameNumbers').split()))
        matchingNumbers = set(winningNumbers) & set(gameNumbers)
        allScratchCards[scratchCardNumber] = {}
        allScratchCards[scratchCardNumber]['scratchCardNumber'] = scratchCardNumber
        allScratchCards[scratchCardNumber]['winningNumbers'] = winningNumbers
        allScratchCards[scratchCardNumber]['gameNumbers'] = gameNumbers
        allScratchCards[scratchCardNumber]['matchingNumbers'] = matchingNumbers
        allScratchCards[scratchCardNumber]['numberOfMatches'] = len(matchingNumbers)
        allScratchCards[scratchCardNumber]['cardScore'] = ( 2 ** ( allScratchCards[scratchCardNumber]['numberOfMatches'] - 1 )) if allScratchCards[scratchCardNumber]['numberOfMatches'] >= 1 else 0
        allScratchCards[scratchCardNumber]['isWinner'] = True if allScratchCards[scratchCardNumber]['numberOfMatches'] >= 1 else False

        
def getTotalSumOfScores():
    runningTotalSum = 0
    for card in allScratchCards:
        #print(f"Matches: {allScratchCards[card]['numberOfMatches']} Score: {allScratchCards[card]['cardScore']}")
        runningTotalSum += allScratchCards[card]['cardScore']
    return runningTotalSum


def getScoreFromCard(parentCardNumber, cardsWon, i = 1, depth = 0):
    global numberOfWinningCards
    depth = depth + 1
    padding = str(parentCardNumber) +" L" + "-" * depth
    while i <= cardsWon:
        cardNumber = parentCardNumber + i
        i = i + 1
        if allScratchCards[cardNumber]['isWinner']:
            #print(padding+f"-Card {cardNumber} Matches: {allScratchCards[cardNumber]['numberOfMatches']} i: {i - 1}")
            numberOfWinningCards += allScratchCards[cardNumber]['numberOfMatches']
            #print(padding+f'-Number of cards won: {numberOfWinningCards}')
            getScoreFromCard(cardNumber, allScratchCards[cardNumber]['numberOfMatches'], 1, depth)
        #else:
            #print(padding+f'Card {cardNumber} is not a winner.')


def getTotalSumOfScoresFullRules():
    global numberOfWinningCards
    for card in allScratchCards:
        #print(f"Matches: {allScratchCards[card]['numberOfMatches']} Score: {allScratchCards[card]['cardScore']}")
        #print(f'Number of cards won: {numberOfWinningCards}')
        if allScratchCards[card]['isWinner']:
            #print(f'Checking Card {card} with Matches: {allScratchCards[card]["numberOfMatches"]}')
            numberOfWinningCards += allScratchCards[card]["numberOfMatches"]
            #print(f'{card} Number of cards won: {numberOfWinningCards}')
            getScoreFromCard(card,allScratchCards[card]["numberOfMatches"])
        #else:
            #print(f'Card {card} is not a winner, no cards won.')
    numberOfWinningCards += len(allScratchCards)
    return numberOfWinningCards

def main():
    getInput()
    totalSumOfScores = getTotalSumOfScores()
    totalSumOfScoresFullRules = getTotalSumOfScoresFullRules()
    print(f'Total Sum of Scores: {totalSumOfScores}')
    print(f'Total Sum of Scores Full Rules: {totalSumOfScoresFullRules}')
    return totalSumOfScores

if __name__ == "__main__":
    main()