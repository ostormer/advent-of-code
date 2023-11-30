from pathlib import Path

in_string = Path("2017/01/in.txt").read_text()

numbers = [int(c) for c in in_string]

sum = 0


for i in range(len(numbers)):
    if numbers[i] == numbers[(i + len(numbers)//2) % len(numbers)]:
        sum += numbers[i]

print(sum)