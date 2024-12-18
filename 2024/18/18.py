from collections import deque

with open("input") as f:
    data = f.read().strip().split("\n")

# (x, y) coords
mem = [tuple(map(int, x.split(","))) for x in data]
mem_map = {}
# start position
pos = (0, 0)
# bottom right corner (target)
far = (70, 70)

mem_map = {(x, y): "." for x in range(far[0] + 1) for y in range(far[1] + 1)}

dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}


# drop byte `i` into the memory map
def drop(i):
    mem_map[mem[i]] = "#"


def vis(costs=None):
    for y in range(far[0] + 1):
        for x in range(far[1] + 1):
            c = mem_map[(x, y)]
            if costs and (x, y) in costs:
                c = " "
            print(c, end="")
        print()


def traverse(p):
    queue = deque([(p, 0)])
    costs = {p: 0}
    while queue:
        p, cost = queue.popleft()
        for d in dirs:
            np = (p[0] + d[0], p[1] + d[1])
            if np not in mem_map or mem_map[np] == "#":
                continue
            ncost = cost + 1
            if np not in costs:
                queue.append((np, ncost))
            costs[np] = min((costs.get(np, float("inf")), ncost))
    return costs


# Part A
for i in range(1024):
    drop(i)
costs = traverse(pos)
print(f"Part A: {costs[far]}")

# Part B
# Brute force is probably not the right direction to take!
# ...but anyway 😅
iter = 1025
while True:
    drop(iter)
    costs = traverse(pos)
    if far not in costs:
        break
    iter += 1

print(f"Part B: {mem[iter]} (iters: {iter})")
