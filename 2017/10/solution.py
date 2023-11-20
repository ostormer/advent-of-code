from pathlib import Path

in_string = Path("2017/10/in.txt").read_text()
length_list = [int(i) for i in in_string.split(",")]

c = 0
skip_size = 0


def knot_hash_round(lengths, init_hash_list, c, skip_size):
    p = 256
    hash_list = list(init_hash_list)
    c = c % p
    skip_size = skip_size % p
    for length in lengths:
        double_list = hash_list + hash_list
        double_list[c : c + length] = reversed(double_list[c : c + length])
        hash_list[c:p] = double_list[c:p]
        hash_list[0:c] = double_list[p : p + c]
        c += length + skip_size
        skip_size += 1
        c = c % p
        skip_size = skip_size % p

    return hash_list, c, skip_size


def knot_hash(string):
    p = 256
    lengths = [ord(char) for char in string]
    lengths += [17, 31, 73, 47, 23]
    hash_list = range(p)
    c = 0
    skip_size = 0
    for _r in range(64):
        hash_list, c, skip_size = knot_hash_round(lengths, hash_list, c, skip_size)

    # Sparse to dense hash
    dense = []
    dense_string = ""
    for block in range(int(p / 16)):
        d = 0
        for i in range(block * 16, (block + 1) * 16):
            d = d ^ hash_list[i]
        dense.append(d)
        dense_string += hex(d)[2:]

    return dense_string


print(knot_hash("70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41"))
