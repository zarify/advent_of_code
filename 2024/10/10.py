with open("input") as f:
    data = f.read().strip().split("\n")

trail_map = {}
heads = []
width = len(data[0])
height = len(data)
for r, l in enumerate(data):
    for c, v in enumerate(l):
        trail_map[(r, c)] = int(v)
        if int(v) == 0:
            heads.append((r, c))

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))


def explore(loc):
    peaks = set()
    to_explore = [[loc]]
    trails = set()
    while to_explore:
        l = to_explore.pop()  # complete trail so far
        h = trail_map[l[-1]]  # current height
        if h == 9:
            peaks.add(l[-1])
            trails.add(tuple(l))
            continue
        for d in dirs:
            nxt = (l[-1][0] + d[0], l[-1][1] + d[1])
            if nxt not in trail_map:
                continue
            if trail_map[nxt] == h + 1:
                to_explore.append(l[:] + [nxt])

    return trails, peaks


exploring = [explore(h) for h in heads]
trails = [e[0] for e in exploring]
peaks = [e[1] for e in exploring]
# Part A
print(f"Part A: {sum([len(p) for p in peaks])}")

# Part B
print(f"Part B: {sum([len(t) for t in trails])}")
