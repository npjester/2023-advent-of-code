import os
import re


input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day1/input.txt")


def getDigit(digitMatch) -> str:
    digit = digitMatch
    print(digit)
    if digit == "one":
        return "1"
    elif digit == "two":
        return "2"
    elif digit == "three":
        return "3"
    elif digit == "four":
        return "4"
    elif digit == "five":
        return "5"
    elif digit == "six":
        return "6"
    elif digit == "seven":
        return "7"
    elif digit == "eight":
        return "8"
    elif digit == "nine":
        return "9"    
    else:
        return digit


def main():
    totalValue = 0

    for line in input.readlines():
        digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        while '' in digits:
            digits.remove('')
        if digits:
            print("Next Digits: ",format(digits))
            if len(digits) > 1:
                firstDigit = getDigit(digits[0])
                print(firstDigit)
                lastDigit = getDigit(digits[len(digits)-1])
                print(lastDigit)
                value = firstDigit + lastDigit
                print(value)
            elif len(digits) == 1:
                firstDigit = getDigit(digits[0])
                print(firstDigit)
                value = firstDigit + firstDigit
                print(value)
            totalValue = totalValue + int(value)
    print(totalValue)

if __name__ == "__main__":
    main()