
def extrap(seq):
    seq = [int(s) for s in seq]
    vals = [seq[0]] # last values in each sequence
    while True:
        diffs = []
        for i, s in enumerate(seq[:-1]):
            diffs.append(seq[i+1] - s)
        else:
            vals.append(diffs[0])
        seq = diffs
        if all(d == 0 for d in diffs):
            break
    v = 0
    for val in vals[::-1]:
        val -= v
        v = val
    return v


with open("9_1.txt") as f:
    data = f.read().splitlines()
    total = 0
    for line in data:
        total += extrap(line.split())
    print(total)