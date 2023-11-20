from pathlib import Path

in_string = Path("2017/06/in.txt").read_text()
blocks = [int(i) for i in in_string.split("\t")]


seen_distributions = [blocks[:]]
n_blocks = len(blocks)
while True:
    max_index = blocks.index(max(blocks))  # Index of first occurence of max elem

    distribution_pot = blocks[max_index]
    blocks[max_index] = 0

    # Distribute
    distribute_to = (max_index + 1) % n_blocks
    while distribution_pot > 0:
        blocks[distribute_to] += 1
        distribution_pot -= 1
        distribute_to += 1
        distribute_to %= n_blocks  # Wrap around

    if blocks in seen_distributions:
        seen_distributions.append(blocks[:])
        break

    seen_distributions.append(blocks[:])  # save a copy of blocks


print(len(seen_distributions) - 1)
# print(seen_distributions)

print(len(seen_distributions) - seen_distributions.index(seen_distributions[-1]) - 1)
