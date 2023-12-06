import re

with open('input.txt') as file:
    lines = file.readlines()

numberMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

totalSum = 0

def stringToInt(input):
    if input.isdigit():
        return int(input)
    else:
        return numberMap[input]

for line in lines:
    pattern = r"""(?x)
			(
			  \d|
			  (?:
			      one|two|three|four|five|six|seven|eight|nine
			  )
)"""
    numbers = re.findall(pattern, line)
    firstNum = stringToInt(numbers[0])
    reversedLine = line[::-1]
    reversePattern = r"""(?x)
			(
			  \d|
			  (?:
			      eno|owt|eerht|ruof|evif|xis|neves|thgie|enin
			  )
)"""
    numbers = re.findall(reversePattern, reversedLine)
    lastNum = stringToInt(numbers[0][::-1])
    totalSum += (firstNum * 10) + lastNum

print(totalSum)