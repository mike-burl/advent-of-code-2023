import re

print('Opening input file...')
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
			      one|two|three|four|five|six|seven|eight|nine|ten| 
			      eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| 
			      eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| 
			      ninety|hundred|thousand
			  )
              \b
)"""
    numbers = re.findall(pattern, line)
    firstNum = stringToInt(numbers[0])
    lastNum = stringToInt(numbers[-1])
    totalSum += (firstNum * 10) + lastNum

print(totalSum)