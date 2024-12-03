import re

def dir_connects(x, y, data, up, right, down, left):
    """
    Take characters at each direction from the current
    location and return the coordinate offsets of tiles
    that connect to it.
    """
    dirs = []
    c = data[y][x]
    if c in ["|", "L", "J", "S"] and up in ["|", "F", "7"]:
        dirs.append((x, y-1))
    if c in ["-", "L", "F", "S"] and right in ["7", "-", "J"]:
        dirs.append((x+1, y))
    if c in ["|", "F", "7", "S"] and down in ["|", "J", "L"]:
        dirs.append((x, y+1))
    if c in ["-", "J", "7", "S"] and left in ["L", "-", "F"]:
        dirs.append((x-1, y))

    return dirs

def chars_around(x, y, data):
    up = data[y-1][x] if y > 0 else " "
    right = data[y][x+1] if x < len(data[y]) - 1 else " "
    down = data[y+1][x] if y < len(data) - 1 else " "
    left = data[y][x-1] if x > 0 else " "
    return up, right, down, left

with open("10_1.txt") as f:
    data = [list(x) for x in f.read().splitlines()]
    for i, line in enumerate(data):
        if "S" in line:
            x = line.index("S")
            y = i
            break
    
    neighbours = dir_connects(x, y, data, *chars_around(x, y, data))
    steps = 0
    visited = {neighbours[0], neighbours[1]}
    while True:
        steps += 1
        nxt = []
        for n in neighbours:
            visited.add(n)
            nxt.extend(dir_connects(n[0], n[1], data, *chars_around(n[0], n[1], data)))
        neighbours = [x for x in nxt if x not in visited]
        if len(neighbours) == 0:
            break
        visited.update(neighbours)
    
    print(steps)