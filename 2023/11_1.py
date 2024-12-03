from itertools import combinations

def distance_between(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

with open("11.txt") as f:
    data = [list(x) for x in f.read().splitlines()]
    # expand the universe
    # add columns from the back
    for i in range(len(data[0]))[::-1]:
        blank = all([x[i] == "." for x in data])
        if blank:
            for d in data:
                d.insert(i + 1, ".")
    # add rows from the bottom
    for i in range(len(data))[::-1]:
        blank = all([x == "." for x in data[i]])
        if blank:
            data.insert(i + 1, ["."] * len(data[0]))
    
    # find all the '#' characters and record their x, y coordinates
    coords = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                coords.append((x, y))
    # find all pairs of coordinates with all combinations
    pairs = list(combinations(coords, 2))
    print(len(pairs))
    print(sum([distance_between(p[0], p[1]) for p in pairs]))