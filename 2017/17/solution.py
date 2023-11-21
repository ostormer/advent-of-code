from tqdm import tqdm

buffer = [0]

current_loc = 0

steps = 344

# for i in tqdm(range(1, 50000001)):
#     current_loc = (current_loc + steps) % len(buffer) + 1
#     buffer.insert(current_loc, i)
#     i += 1

after_zero = 1
for i in tqdm(range(1, 50000001)):
    current_loc = (current_loc + steps) % i + 1  # len(buffer) = i
    if current_loc == 1:  # insert after 0
        after_zero = i
    # buffer.insert(current_loc, i)
    i += 1

print(after_zero)

