import os
import re


input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day1/input.txt")
totalValue = 0

for line in input.readlines():
    digits = re.findall(r'\d', line)
    if digits:
        if len(digits) > 1:
            value = digits[0] + digits[len(digits)-1]
        elif len(digits) == 1:
            value = digits[0] + digits[0]
        totalValue = totalValue + int(value)
print(totalValue)