fn = "input"
with open(fn) as f:
    data = {}
    for r, row in enumerate(f.read().strip().split("\n")):
        data[r] = {}
        for c, char in enumerate(list(row)):
            data[r][c] = char

rows = len(data.keys())
cols = len(data[0].keys())

def around(r, c, char, fmap):
    surrounding = 0
    for rn in range(r-1, r+2):
        row = fmap.get(rn, None)
        if row:
            for cn in range(c-1,c+2):
                if rn == r and cn == c:
                    continue # don't process own position
                fchar = row.get(cn, None)
                if fchar is None:
                    continue
                if fchar == char:
                    surrounding += 1
    return surrounding

def id_rolls(fmap):
    removable = []

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "@" and around(r, c, "@", data) < 4:
                removable.append((r, c))

    return removable

# Part A
rolls = len(id_rolls(data))
print(f"Part A: {rolls}")    

if fn == "test":
    assert rolls == 13

# Part B
rolls = 0
while True:
    removable = id_rolls(data)
    if len(removable) == 0:
        break
    for r, c in removable:
        data[r][c] = "x"
    rolls += len(removable)
print(f"Part B: {rolls}")

if fn == "test":
    assert rolls == 43