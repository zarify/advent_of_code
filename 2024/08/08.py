from collections import defaultdict
from itertools import combinations

with open("input") as f:
    data = f.read().strip()

# figure out the dimensions of the area before turning it into
# a flat string without line breaks to make index processing as
# a stream nice and easy
width = data.index("\n")
height = data.count("\n") + 1
data = data.replace("\n", "")

# build up a dictionary of positions of non-blank spaces
positions = defaultdict(list)
for i, c in enumerate(data):
    row, col = i // width, i % width
    if c == ".":
        continue
    positions[c].append((row, col))


# visualise the antinode locations overlaid on the original area
def vis(positions, antinodes):
    data = []
    for _ in range(height):
        data.append(["."] * width)

    for k, v in positions.items():
        for p in v:
            data[p[0]][p[1]] = k
    for r, c in antinodes:
        data[r][c] = "#"
    print(*["".join(d) for d in data], sep="\n")
    print("\n")


# add the position to the given antinodes set if it's within the area
# and return success status to help with the loop processing for Part B
def validate(p, antinodes):
    if p[0] >= 0 and p[0] < height and p[1] >= 0 and p[1] < width:
        antinodes.add(p)
        return True
    return False


antinodes = set()  # Part A
resonant = set()  # Part B
for c, pos in positions.items():
    if len(pos) < 2:
        continue  # need 2 or more antennas
    combos = combinations(pos, 2)
    for combo in combos:
        dy = combo[0][0] - combo[1][0]
        dx = combo[0][1] - combo[1][1]
        # single antinode - Part A
        validate((combo[0][0] + dy, combo[0][1] + dx), antinodes)
        validate((combo[1][0] - dy, combo[1][1] - dx), antinodes)
        # resonant ripple - Part B
        # ripple out until both have left the area, multiplying distance
        # by the ripple count
        ripple = 0
        while True:
            r_pos = validate(
                (combo[0][0] + dy * ripple, combo[0][1] + dx * ripple), resonant
            )
            r_neg = validate(
                (combo[1][0] - dy * ripple, combo[1][1] - dx * ripple), resonant
            )
            ripple += 1
            # both have failed, time to bail
            if not r_pos and not r_neg:
                break


# vis(positions, antinodes)
print(f"Part A: {len(antinodes)}")

# Part B
print(f"Part B: {len(resonant)}")
