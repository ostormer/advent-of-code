from pathlib import Path

data = Path("2023/01/in.txt").read_text()

data = data.split("\n")

numbers_dict = {
    # "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
s = 0

for line in data:
    l = line[:]
    for word, number in numbers_dict.items():
        l = l.replace(word, word[0] + str(number) + word[-1])

    numbers = [int(letter) for letter in l if letter.isnumeric()]

    s += numbers[0] * 10 + numbers[-1]

print(s)
