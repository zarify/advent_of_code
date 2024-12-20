from collections import deque

with open("input") as f:
    data = f.read().strip().split("\n")

mmap = {(x, y): c for y, row in enumerate(data) for x, c in enumerate(row)}
dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}
pos = [p for p in mmap if mmap[p] == "S"][0]
end = [p for p in mmap if mmap[p] == "E"][0]


# calculate the cost for moving to all points on the path
def traverse(p):
    queue = deque([(p, 0)])
    costs = {p: 0}
    while queue:
        p, cost = queue.popleft()
        for d in dirs:
            np = (p[0] + d[0], p[1] + d[1])
            if np not in mmap or mmap[np] == "#":
                continue
            ncost = cost + 1
            if np not in costs:
                queue.append((np, ncost))
            costs[np] = min((costs.get(np, float("inf")), ncost))
    return costs


# build a set of offsets up to distance `d` with the x, y offset
# and the distance it takes to get there
def calc_offsets(d):
    offsets = set()
    for x in range(0, d + 1):
        for y in range(0, d + 1):
            cost = abs(x) + abs(y)
            if cost > d or (x == 0 and y == 0):
                continue
            offsets.add((-x, y, cost))
            offsets.add((x, y, cost))
            offsets.add((-x, -y, cost))
            offsets.add((x, -y, cost))
    return offsets


# find all points reachable using the given set of cheat offsets
# from position p and return the cost savings for each point found
def cheat(p, costs, offsets):
    cost = costs[p]  # original location
    cost_savings = []
    for k in offsets:
        p2 = (p[0] + k[0], p[1] + k[1])
        d = k[2]
        if p2 not in costs or costs[p2] <= cost:
            continue  # not on the path or no cost saving
        saving = costs[p2] - cost - d
        if saving > 2:
            cost_savings.append(saving)

    return cost_savings  # cost differential


map_times = traverse(pos)
end_cost = map_times[end]

print(f"Map costs {end_cost}")

# Part A
valid_cheatsA = []
offsetsA = calc_offsets(2)
for p in [pos for pos in map_times if pos != end]:
    valid_cheatsA.extend([c for c in cheat(p, map_times, offsetsA) if c >= 100])
print(f"Part A: {len(valid_cheatsA)}")

valid_cheatsB = []
offsetsB = calc_offsets(20)
for p in [pos for pos in map_times if pos != end]:
    valid_cheatsB.extend([c for c in cheat(p, map_times, offsetsB) if c >= 100])
print(f"Part A: {len(valid_cheatsB)}")
