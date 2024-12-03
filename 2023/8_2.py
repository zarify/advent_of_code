# far too slow to brute force it
# see 8_2a.py for the lowest common multiple solution
# instead

import re

with open("8_1.txt") as f:
    data = f.read().splitlines()
    nav = data[0]
    dirs = {}
    for line in data[2:]:
        m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        dirs[m.group(1)] = (m.group(2), m.group(3))
    steps = 0
    locs = [x for x in dirs.keys() if x[-1] == "A"]
    while True:
        d = nav[steps % len(nav)]
        idx = "LR".index(d)
        locs = [dirs[x][idx] for x in locs]
        steps += 1
        if all([x[-1] == "Z" for x in locs]):
            break
    print(steps)