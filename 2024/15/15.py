with open("input") as f:
    data = f.read().strip().split("\n\n")


def get_map(data, dbl=False):
    wh = {}
    # parse the warehouse map
    for r, row in enumerate(data[0].split("\n")):
        c_off = 0
        for c, v in enumerate(row):
            if dbl and v == "O":
                v = "["
            wh[(r, c + c_off)] = v
            if v == "@":
                pos = (r, c + c_off)  # robot position

            # add in the extra wide character where necessary
            if dbl and v == "[":
                wh[(r, c + c_off + 1)] = "]"
                c_off += 1
            elif dbl and v in "#.":
                wh[(r, c + c_off + 1)] = v
                c_off += 1
            elif dbl and v == "@":
                wh[(r, c + c_off + 1)] = "."
                c_off += 1

    return wh, pos


def get_commands(data):
    # convert the commands
    dirs = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
    commands = [dirs[c] for c in data[1].replace("\n", "")]
    return commands


def check_movable(positions, v, warehouse):
    movable = set()
    boxes = {"[": (0, 1), "]": (0, -1)}
    blocked = False
    for p in positions:
        # stop positions that aren't pushable propagating forwards
        if warehouse[p] == ".":
            continue
        np = (p[0] + v[0], p[1] + v[1])  # position this would move to
        if warehouse[np] == "#":
            blocked = True
            break
        movable.add(np)
        # if the next location is half a box and moving vertically, add the other half too
        if v[0] != 0 and warehouse[np] in "[]":
            np2 = (np[0], np[1] + boxes[warehouse[np]][1])
            if warehouse[np2] == "#":
                blocked = True
                break
            movable.add(np2)
    # so this is gross and I shouldn't have to do it
    # we don't want to add clear space to the propagation list if the whole
    # row isn't clear as this pushes the wrong things around later
    if not all([warehouse[p] == "." for p in movable]):
        movable = set([p for p in movable if warehouse[p] != "."])

    return [] if blocked else movable


def move_robot2(pos, warehouse, commands):
    # position to add if encountering a wide box

    for cmd in commands:
        nxt = (pos[0] + cmd[0], pos[1] + cmd[1])
        if nxt not in warehouse or warehouse[nxt] == "#":
            continue

        moving = [(pos,)]
        # will return either the next free position for all items,
        # in which case we break and get to shifting things, an empty
        # list for blocked moves, or the next lot of crates to check
        while movable := check_movable(moving[-1], cmd, warehouse):
            moving.append(movable)  # more movable things to check
            if all([warehouse[m] == "." for m in movable]):
                break  # found the next move

        if any([warehouse[m] != "." for m in moving[-1]]):
            continue
        moving.pop()
        for m in moving[::-1]:
            # update position of each item in m
            # and leave a blank space behind (which may then be updated by
            # another moving piece, which is why this is backwards)
            for p in m:
                np = (p[0] + cmd[0], p[1] + cmd[1])
                warehouse[np] = warehouse[p]
                warehouse[p] = "."
        if moving:
            pos = nxt

    return warehouse


def vis(warehouse):
    height = max([wh[0] for wh in warehouse]) + 1
    width = max([wh[1] for wh in warehouse]) + 1
    for r in range(height):
        for c in range(width):
            print(warehouse[(r, c)], end="")
        print()


def calc_coords(warehouse):
    total = 0
    for k, v in warehouse.items():
        if v not in "O[":
            continue
        total += 100 * k[0] + k[1]

    return total


wh, pos = get_map(data)
cmds = get_commands(data)

# Part A
wh_a = move_robot2(pos, wh, cmds)
print(f"Part A: {calc_coords(wh_a)}")


# Part B
wh_wide, pos = get_map(data, dbl=True)
wh_b = move_robot2(pos, wh_wide, cmds)
print(f"Part B: {calc_coords(wh_b)}")
