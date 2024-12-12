with open("input") as f:
    data = f.read().strip().split("\n")

# build a dictionary out of the garden with format {(row, column): letter, ... }
garden = {}
for r, row in enumerate(data):
    for c, g in enumerate(row):
        garden[(r, c)] = g

# direction offsets plus the name of the side that is being checked (used for counting sides)
dirs = {(0, 1): "right", (0, -1): "left", (1, 0): "bottom", (-1, 0): "top"}


# sort all of the positions with sides from the garden bed according to their side name (from `dirs`)
# and then by the relevant side axis (x or y), and finally the off axis. This means edges should be
# in sorted order according to their direction, and we can identify new sides by changes in direction
# or jumps in the off axis (e.g. ((0, 1), "bottom") then ((0, 3), "bottom") is a new side as there is a
# non 1 jump in the column value
def discover_edges(positions):
    last_side = None
    last_axis = None
    last_off = None
    edges = 0
    for p, d in sorted(
        positions,
        key=lambda x: (
            x[1],
            (x[0][1] if x[1] in ("left", "right") else x[0][0]),
            (x[0][0] if x[1] in ("left", "right") else x[0][1]),
        ),
    ):
        if last_side is None:
            last_axis = p[1] if d in ("left", "right") else p[0]
            last_side = d
            last_off = p[0] if d in ("left", "right") else p[1]
            edges += 1
            continue
        axis = p[1] if d in ("left", "right") else p[0]
        off_axis = p[0] if d in ("left", "right") else p[1]
        if axis == last_axis and d == last_side and last_off == off_axis - 1:
            last_off = off_axis
            continue
        edges += 1
        last_axis = p[1] if d in ("left", "right") else p[0]
        last_off = p[0] if d in ("left", "right") else p[1]
        last_side = d

    return edges


# execute a search from `pos` for all adjacent letters that are the same
# as this is being built, also maintain a list of positions that lie on
# an edge for side counting later on
def explore(pos):
    area = 0
    perimeter = 0
    edges = []
    queue = [pos]
    c = garden[pos]  # current garden tile
    seen = set()
    while queue:
        pos = queue.pop()
        if pos in seen:
            continue
        seen.add(pos)
        area += 1
        for d in dirs:
            nxt = (pos[0] + d[0], pos[1] + d[1])
            if nxt in seen:
                continue
            if nxt not in garden:
                perimeter += 1
                edges.append(
                    (pos, dirs[d])
                )  # add the current position and relative edge position
                continue
            if garden[nxt] == c and nxt not in seen:
                queue.append(nxt)
            else:
                perimeter += 1
                edges.append((pos, dirs[d]))

    return area, perimeter, edges, seen


costsA = []
costsB = []
seen = set()
for k, v in garden.items():
    if k not in seen:
        a, p, e, s = explore(k)
        seen.update(s)
        costsA.append(a * p)
        costsB.append(a * discover_edges(e))

# Part A
print(f"Part A: $ {sum(costsA)}")

print(f"Part B: $ {sum(costsB)}")
