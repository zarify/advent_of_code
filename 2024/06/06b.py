with open("input") as f:
    data = f.read().strip()

# what character is the guard initially?
g = [c for c in "^>v<" if c in data][0]
width = data.index("\n")
# don't want line breaks messing with my indexing
data = data.replace("\n", "")
height = len(data) // width
# guard initial position, column and row (x, y)
pos = (data.index(g) // width, data.index(g) % width)

# initial direction movement deltas
dirs = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
# right hand turn transforms
f = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
g = dirs[g]  # initial direction

# generate the guard area as a dict with symbols as values
# symbols can be on of: .#<>^v
guard_area = {}
for i, v in enumerate(data):
    r, c = i // width, i % width
    guard_area[(r, c)] = v


def traverse(pos, g, guard_area, loop_detect=False, self_modify=False):
    """
    Feel a bit dirty for returning ints in different contexts.
    If loop detection is set, return 1 for a loop and 0 for no loop.
    Otherwise return the number of unique positions in the path
    """
    seen = set()
    loop_walls = 0
    while pos[0] in range(height) and pos[1] in range(width):
        seen.add(pos if not loop_detect else (pos, g))
        new_pos = (pos[0] + g[0], pos[1] + g[1])
        if new_pos not in guard_area:
            break
        if guard_area[new_pos] == "#":
            g = f[g]
        else:
            pos = new_pos
        # check if our new position and facing is already in our history
        if loop_detect and (pos, g) in seen:
            return 1
    if self_modify:
        return loop_walls
    if not loop_detect:
        return len(seen)
    return 0


# Part A
print(f"Part A: {traverse(pos, g, guard_area, False)}")

# Part B
# Brute force version - be better to do this as the original traversal is
# happening and just check each step in front of the guard, but I'm lazy
obstacles = 0
for k, v in guard_area.items():
    if v != ".":
        continue
    guard_area[k] = "#"
    obstacles += traverse(pos, g, guard_area, True)
    guard_area[k] = "."

print(f"Part B: {obstacles}")
