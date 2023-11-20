import math

what = 312051


def radius(x):
    return math.ceil(math.sqrt(x) / 2 - 0.5 - 1e-6)  # Add eps


def dist_from_center(x):
    r = radius(x)
    size_of_outer_circle = 8 * r
    if size_of_outer_circle == 0:
        return 0

    num_in_circle = x - (r * 2 - 1) ** 2

    side_length = int(size_of_outer_circle / 4)
    dist_after_corner = num_in_circle % side_length
    dist_to_middle = int(abs((side_length / 2) - dist_after_corner))

    return dist_to_middle + r


print(dist_from_center(what))

grid = {}

for x in range(-50, 51):
    for y in range(-50, 51):
        grid[(x, y)] = 0


grid[(0, 0)] = 1

coords_by_index = [(0, 0)]
sums = [1]
i = 2
r = 1
size_of_outer_circle = 8 * r
bottom_right = (r * 2 + 1) ** 2

x, y = 1, 0
while i < 1000:
    insert = sum(
        (grid[(x - 1, y - 1)],
        grid[(x - 1, y)],
        grid[(x - 1, y + 1)],
        grid[(x, y - 1)],
        grid[(x, y + 1)],
        grid[(x + 1, y - 1)],
        grid[(x + 1, y)],
        grid[(x + 1, y + 1)])
    )

    grid[(x, y)] = insert
    sums.append(insert)
    i += 1
    if insert > what:
        print(insert)
        break

    if x == r:  # right
        if y == r:  # top right
            x -= 1
        elif y == -r:  # bottom right
            r += 1
            x += 1
        else:
            y += 1
    elif y == r:  # top
        if x == -r:  # top left
            y -= 1
        else:
            x -= 1
    elif x == -r:  # left
        if y == -r:  # bottom left
            x += 1
        else:
            y -= 1
    elif y == -r:  # bottom
        if x == r:  # bottom right
            print("SOMETHING WENT WRONG")
        else:
            x += 1



for y in range(6, -7, -1):
    for x in range(-6, 7):
        print(format(grid[(x, y)], " ^8d"), end=" ")
    print()
