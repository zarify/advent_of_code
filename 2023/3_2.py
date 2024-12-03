import re

def adj(s, i):
    nums = []
    for m in re.finditer(r"\b(\d+)\b", s):
        if m.start() in [i-1, i, i+1] or m.end()-1 in [i-1, i, i+1]:
            nums.append(int(m.group()))
    return nums

with open("3_1.txt") as f:
    total = 0
    data = f.read().strip().split("\n")
    for i,d in enumerate(data):
        for m in re.finditer("(\\*)", d):
            adjacent = []
            if i > 0:
                adjacent += adj(data[i-1], m.start())
            if i < len(data) - 1:
                adjacent += adj(data[i+1], m.start())
            adjacent += adj(d, m.start())
            if len(adjacent) == 2:
                total += adjacent[0] * adjacent[1]

    print(total)