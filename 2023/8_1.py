import re

with open("8_1.txt") as f:
    data = f.read().splitlines()
    nav = data[0]
    dirs = {}
    for line in data[2:]:
        m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        dirs[m.group(1)] = (m.group(2), m.group(3))
    steps = 0
    loc = "AAA"
    while True:
        d = nav[steps % len(nav)]
        idx = "LR".index(d)
        loc = dirs[loc][idx]
        steps += 1
        if loc == "ZZZ":
            break
    print(steps)