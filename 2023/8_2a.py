import re

with open("8_1.txt") as f:
    data = f.read().splitlines()
    nav = data[0]
    dirs = {}
    for line in data[2:]:
        m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        dirs[m.group(1)] = (m.group(2), m.group(3))
    steps = []
    locs = [x for x in dirs.keys() if x[-1] == "A"]
    for loc in locs:
        s = 0
        while True:
            d = nav[s % len(nav)]
            idx = "LR".index(d)
            loc = dirs[loc][idx]
            s += 1
            if loc[-1] == "Z":
                break
        steps.append(s)
    print(steps)
    # [11567, 19637, 15871, 21251, 12643, 19099]
    import math
    from functools import reduce
    print(reduce(math.lcm, steps))
