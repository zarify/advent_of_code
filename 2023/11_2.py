from itertools import combinations

def distance_between(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

with open("11.txt") as f:
    data = [list(x) for x in f.read().splitlines()]
    blank_x = []
    blank_y = []
    # expand the universe
    # add columns from the back
    for i in range(len(data[0]))[::-1]:
        blank = all([x[i] == "." for x in data])
        if blank:
            blank_x.append(i)
    # add rows from the bottom
    for i in range(len(data))[::-1]:
        blank = all([x == "." for x in data[i]])
        if blank:
            blank_y.append(i)
    
    # find all the '#' characters and record their x, y coordinates
    MULT = 1000000
    coords = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                hash_x = x
                hash_y = y
                hash_x += len([x for x in blank_x if x < hash_x]) * (MULT - 1)
                hash_y += len([y for y in blank_y if y < hash_y]) * (MULT - 1)
                coords.append((hash_x, hash_y))
    # find all pairs of coordinates with all combinations
    pairs = list(combinations(coords, 2))
    print(len(pairs))
    print(sum([distance_between(p[0], p[1]) for p in pairs]))