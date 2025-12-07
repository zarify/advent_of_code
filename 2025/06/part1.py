fn = "input"

with open(fn) as f:
    # read each of the lines and split them, then transpose the data
    # this way worked fine and was nice and elegant for Part A, but...
    # data = list(zip(*[x.split() for x in f.read().strip().split("\n")]))
    # instead we have to do a linear search and preserve column positions
    lines = f.read().strip().split("\n")
    data = []
    last_idx = -1
    numlines = len(lines)
    for i in range(len(lines[0])):
        if all(line[i] == " " for line in lines):
            data.append([line[last_idx + 1 : i] for line in lines])
            last_idx = i
    else:
        data.append([line[last_idx + 1 :] for line in lines])


# Part A
total = 0

for row in data:
    op = row[-1]
    # I feel dirty for using eval here, but it's convenient and also
    # ignores any whitespace
    total += eval(op.join(row[:-1]))

print(f"Part A: {total}")
if fn == "test":
    assert total == 4277556

# Part B
total = 0

for row in data:
    op = row[-1]
    # use zip to transpose the columns
    lines = map(lambda x: "".join(x), [x for x in list(zip(*row[:-1]))])
    total += eval(op.join(lines))

print(f"Part B: {total}")
if fn == "test":
    assert total == 3263827
