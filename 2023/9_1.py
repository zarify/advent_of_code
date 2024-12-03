
def extrap(seq):
    seq = [int(s) for s in seq]
    vals = [seq[-1]] # last values in each sequence
    while True:
        diffs = []
        for i, s in enumerate(seq[:-1]):
            diffs.append(seq[i+1] - s)
        else:
            vals.append(diffs[-1])
        seq = diffs
        if all(d == 0 for d in diffs):
            break
    return sum(vals)


with open("9_1.txt") as f:
    data = f.read().splitlines()
    total = 0
    for line in data:
        total += extrap(line.split())
    print(total)