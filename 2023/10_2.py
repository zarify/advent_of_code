import re


# https://imgur.com/a/ukstWKO
# mark all cells as U or D for up or down or _ for left-right
# use a regex to find all non _ tiles between opposite directions
# on a line, eg "U....D", "D.....U", "D____U"

def dir_connects(c, d, dir):
    """
    validate that the character c connections to the character d
    in direction dir
    """
    dirs = {
        "up": ["|LJSUD_", "|F7"],
        "right": ["-LFS_UD", "7-J"],
        "down": ["|F7SUD_", "|JL"],
        "left": ["-J7S_UD", "-FL"]
    }
    # print(f"Checking that {c} (in {dirs[dir][0]}) connects to {d} (in {dirs[dir][1]}) in {dir} ")
    return c in dirs[dir][0] and d in dirs[dir][1]

def at_dir(x, y, data, dir):
    """
    return the character at the next tile in the given direction
    """
    if dir == "up":
        return data[y-1][x] if y > 0 else " "
    if dir == "right":
        return data[y][x+1] if x < len(data[y]) - 1 else " "
    if dir == "down":
        return data[y+1][x] if y < len(data) - 1 else " "
    if dir == "left":
        return data[y][x-1] if x > 0 else " "

def move(x, y, dir):
    if dir == "up":
        return x, y - 1
    if dir == "right":
        return x + 1, y
    if dir == "down":
        return x, y + 1
    if dir == "left":
        return x - 1, y

def discover(x, y, data):
    """
    find all tiles that connect to the current location
    """
    dirs = {"up", "right", "down", "left"}
    valid = []
    for dir in dirs:
        if dir_connects(data[y][x], at_dir(x, y, data, dir), dir):
            valid.append((move(x, y, dir), dir))
    return valid


with open("10_1.txt") as f:
    data = [list(x) for x in f.read().splitlines()]
    for i, line in enumerate(data):
        if "S" in line:
            x = line.index("S")
            y = i
            connected = [d[1] for d in discover(x, y, data)]
            # replace the S with the appropriate symbol
            if "up" in connected and "down" in connected:
                data[y][x] = "|"
            elif "up" in connected and "left" in connected:
                data[y][x] = "J"
            elif "up" in connected and "right" in connected:
                data[y][x] = "L"
            elif "down" in connected and "left" in connected:
                data[y][x] = "7"
            elif "down" in connected and "right" in connected:
                data[y][x] = "F"
            else:
                data[y][x] = "-"
            break
    visited = {(x, y)}
    ordered = [[x, y]]
    while True:
        discovered = [d for d in discover(x, y, data) if d[0] not in visited]
        # print(discovered)
        if len(discovered) == 0:
            break
        d = discovered[0]
        x, y = d[0]
        dir = d[1]
        visited.add(d[0])
        ordered.append(list(d[0]))
        # print(f"Moving to {d[0]} in direction {dir}")
    # print("\n".join(["".join(x) for x in data]))

    # shoelace formula here
    # https://en.wikipedia.org/wiki/Shoelace_formula
    print(len(ordered))
    area = 0
    for i, o in enumerate(ordered):
        if i != len(ordered) - 1:
            area += (o[0] * ordered[i+1][1]) - (o[1] * ordered[i+1][0])
        else:
            area += (o[0] * ordered[0][1]) - (o[1] * ordered[0][0])
    print(f"Area: {abs(area)/2}")
    # now we use Pick's theorem to find the interior points
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    # area = interior_points + boundary_points / 2 - 1
    # so interior_points = area - boundary_points / 2 + 1
    interior_points = abs(area)/2 - len(ordered)/2 + 1
    print(f"Interior points: {interior_points}")



    outfile = open("10_2.txt", "w")
    total = 0
    # open up an image file and write each position to it as a pixel
    # where the pixel is black if is part of the path and white if
    # it is not
    import PIL.Image as Image
    im = Image.new("RGB", (len(data[0]), len(data)))
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (x, y) in visited:
                c = data[y][x]
                im.putpixel((x, y), (0, 0, 0))
            else:
                data[y][x] = " "
                im.putpixel((x, y), (255, 255, 255))
        else:
            line = "".join(data[y])
            # scan from left to right to determine which points
            # are inside the path
            inside = False
            last = ""
            # print(f"Line {y}")
            for i, c in enumerate(line):
                if not inside:
                    if c == "|":
                        inside = True
                        im.putpixel((i, y), (0, 255, 0)) # green start inside
                    elif c in "FL":
                        # these might be openers if later followed by J or 7
                        # so append them to last to check later
                        last += c
                        im.putpixel((i, y), (255, 255, 0))
                    elif c == "J" and "F" in last:
                        inside = True
                        last = ""
                        im.putpixel((i, y), (0, 255, 0)) # green start inside
                    elif c == "7" and "L" in last:
                        inside = True
                        last = ""
                        im.putpixel((i, y), (0, 255, 0)) # green start inside
                    elif c == "7" and "F" in last:
                        last = ""
                        im.putpixel((i, y), (150, 150, 0))
                    elif c == "-":
                        im.putpixel((i, y), (0, 0, 0))
                    else:
                        im.putpixel((i, y), (255, 0, 255)) # purple outside
                else:
                    if c == "|":
                        inside = False
                        im.putpixel((i, y), (0, 0, 255)) # blue end inside
                        last = ""
                    elif c in "FL":
                        # these might be closers if later followed by J or 7
                        # so append them to last to check later
                        last += c
                    elif c == "J" and "F" in last:
                        inside = False
                        last = ""
                        im.putpixel((i, y), (0, 0, 255))
                    elif c == "7" and "L" in last:
                        inside = False
                        last = ""
                        im.putpixel((i, y), (0, 0, 255))

                # print(f"\t{last}{c} inside={inside}")
            outfile.write(line + "\n")

    im.save("10_2.png")
    print(f"Filled amount: {total}")