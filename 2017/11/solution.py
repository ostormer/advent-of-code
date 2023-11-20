from pathlib import Path
from collections import Counter
from tqdm import tqdm

in_string = Path("2017/11/in.txt").read_text()
trail = in_string.split(",")


# Straighten path
def straighten(a, b, c):
    if a * b > 0:  # samme fortegn
        if a > 0:
            pos = 1
        else:
            pos = -1
        shorten = min(abs(a), abs(b)) * pos
        a -= shorten
        b -= shorten
        c -= shorten

    return a, b, c


def shortest_distance(trail):
    c = Counter(trail)

    nw = c["nw"] - c["se"]
    ne = c["ne"] - c["sw"]
    s = c["s"] - c["n"]
    while True:
        count = {"nw": nw, "ne": ne, "s": s}
        n_zero, n_pos, n_neg = 0, 0, 0
        for n_direction in count.values():
            if n_direction > 0:
                n_pos += 1
            elif n_direction < 0:
                n_neg += 1
            elif n_direction == 0:
                n_zero += 1
        if n_zero == 1 and n_pos == 1 and n_neg == 1:
            break
        if n_zero > 1:
            break

        nw, ne, s = straighten(nw, ne, s)
        nw, s, ne = straighten(nw, s, ne)
        s, ne, nw = straighten(s, ne, nw)
    return abs(nw) + abs(ne) + abs(s)


distance_from_start = []

for i in tqdm(range(len(trail))):
    distance_from_start.append(shortest_distance(trail[: i + 1]))
print(max(distance_from_start))
