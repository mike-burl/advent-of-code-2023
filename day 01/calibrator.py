import re

print('Opening input file...')
with open('test.txt') as file:
    lines = file.readlines()

totalSum = 0

for line in lines:
    numbers = re.findall(r'\d', line)
    firstNum = int(numbers[0])
    lastNum = int(numbers[-1])
    totalSum += (firstNum * 10) + lastNum

print(totalSum)