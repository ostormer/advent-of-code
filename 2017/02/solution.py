from pathlib import Path

in_string = Path("2017/02/in.txt").read_text()

lines = [[int(num) for num in line.split("\t")] for line in in_string.split("\n")]




# del 1
checksum = 0
for line in lines:
    checksum += max(line) - min(line)

print(checksum)

# del 2
checksum = 0
for line in lines:
    for a in line:
        for b in line:
            if a == b:
                continue
            if a % b == 0:
                checksum +=  a / b


print(checksum)
