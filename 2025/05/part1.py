fn = "input"


def update_ranges(start, end, fresh):
    updated = False
    for i, (s, e) in enumerate(fresh):
        if start == s and end == e:
            # range is the same
            updated = True
        elif start >= s and end <= e:
            # subset of the range
            updated = True
        elif start <= s and end >= e:
            # superset of the range
            updated = True
            fresh[i][0] = start
            fresh[i][1] = end
        elif start < s and end >= s:
            # extends left
            fresh[i][0] = start  # update left side of range
            updated = True
        elif start <= e and end > e:
            # extends right
            fresh[i][1] = end  # update right end of range
            updated = True
    # only add to fresh if we're in merge mode
    if not updated:
        fresh.append([start, end])


def in_range(n, fresh):
    for fr in fresh:
        if n >= fr[0] and n <= fr[1]:
            return True
    return False


with open(fn) as f:
    fresh = []
    inv = []
    for line in f.read().strip().split("\n"):
        if "-" in line:  # inventory range
            start, end = map(int, line.split("-"))
            update_ranges(start, end, fresh)
        elif line.isdigit():  # inventory item
            inv.append(int(line))

# now let's keep merging until we end up with the same
# length list
while True:
    newfresh = []
    for start, end in fresh:
        update_ranges(start, end, newfresh)
    if len(fresh) == len(newfresh):
        break
    fresh = newfresh

# Part A
total = 0
for i in inv:
    if in_range(i, fresh):
        total += 1

print(f"Part A: {total}")
if fn == "test":
    assert total == 3
elif fn == "input":
    assert total == 739

# Part B
total = 0

for fr in fresh:
    total += fr[1] - fr[0] + 1

print(f"Part B: {total}")
if fn == "test":
    assert total == 14
elif fn == "input":
    assert total == 344486348901788
