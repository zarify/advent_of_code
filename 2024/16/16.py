from collections import deque

with open("test") as f:
    data = f.read().strip().split("\n")

m = {}
# facings and valid directions after a single rotation
f = {
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(1, 0), (-1, 0)],
    (1, 0): [(0, 1), (0, -1)],
    (-1, 0): [(0, 1), (-1, 0)],
}
facings = {(0, 1): ">", (0, -1): "<", (1, 0): "v", (-1, 0): "^"}
for r, row in enumerate(data):
    for c, v in enumerate(row):
        m[(r, c)] = "#" if v == "#" else "."
        if v == "S":
            pos = (r, c)
        elif v == "E":
            end = (r, c)


def traverse(m, pos, facing):
    costs = {p: (-1, None) for p in m}
    # traverse the map m from position pos with facing facing
    # keeping track of seen nodes and updating costs
    seen = set()
    queue = [(pos, facing)]
    costs[pos] = (0, facing)  # start position
    while queue:
        pos, facing = queue.pop()
        current_cost, from_dir = costs[pos]
        seen.add(pos)
        for d in f:
            nxt = (pos[0] + d[0], pos[1] + d[1])
            if m[nxt] == "#":
                continue
            if d == facing:
                nxt_cost = current_cost + 1
            else:
                nxt_cost = current_cost + 1001
            # check if the path to nxt is cheaper, even if it's
            # in seen
            if nxt_cost < costs[nxt][0] or costs[nxt][0] == -1:
                costs[nxt] = (nxt_cost, (d[0] * -1, d[1] * -1))
                if nxt in seen:
                    seen.remove(nxt)  # let us reprocess using the cheaper cost
            if nxt in seen:
                continue
            queue.append((nxt, d))
    return costs


def backtrack(costs, end):
    # backtrack from the end position, following the minimum cost route
    # until we reach pos (the start)
    # return the total number of positions traversed through
    seen = set()
    queue = [end]
    while queue:
        pos = queue.pop()
        seen.add(pos)
        cost, facing = costs[pos]
        nxt = [(pos[0] + d[0], pos[1] + d[1]) for d in f]
        # filter for visited positions and anything with no calculated cost
        nxt = [n for n in nxt if n not in seen and costs[n][1]]
        # any unseen neighbours that have the same minimum cost get
        # added to the processing queue
        for n in nxt:
            if costs[n][0] == costs[min(nxt, key=lambda x: costs[x][0])]:
                queue.append(n)

    return len(seen)


def vis(path, m):
    m = m.copy()
    for r in range(max(p[0] for p in m) + 1):
        for c in range(max(p[1] for p in m) + 1):
            if (r, c) in path:
                print("R", end="")
            else:
                print(m[(r, c)], end="")
        print()


# Part A
costs = traverse(m, pos, (0, 1))
print(f"Part A: {costs[end][0]}")

checking = [(7, 5), (7, 4), (7, 3), (8, 5)]
for c in checking:
    print(f"Cost of {c} is {costs[c]}")

# Part B
print(f"Part B: {backtrack(costs, end)}")
