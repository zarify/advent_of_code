from collections import Counter

with open("input") as f:
    data = f.read().strip().split("\n")


def prng(n):
    while True:
        s = n
        # step 1
        s = ((n * 64) ^ n) % 16777216
        # step 2
        s = (int(s / 32) ^ s) % 16777216
        # step 3
        s = ((s * 2048) ^ s) % 16777216
        n = s
        yield s


total = 0  # Part A accumulator

deltas = []  # difference from last value
amounts = []  # last number value
seeds = tuple(map(int, (d for d in data)))


for s in seeds:
    p = prng(s)
    pdelta = [None]
    pamounts = [s % 10]
    prev = s % 10
    for i in range(2000):
        n = next(p)
        first = n % 10
        pamounts.append(first)
        pdelta.append(first - prev)
        prev = first
    deltas.append(pdelta)
    amounts.append(pamounts)

    total += n

# Part A
print(f"Part A: {total}")

# Part B
seq_prices = Counter()
# go through each column examining each sequence, and use the counter to track accumulated
# value of that sequence
for di, d in enumerate(deltas):
    seqs = set()
    for i in range(2, len(d) - 3):
        s = tuple(d[i : i + 4])
        # add the price to the counter if we haven't seen this yet in this column
        if s not in seqs:
            seq_prices[s] = seq_prices.get(s, 0) + amounts[di][i + 3]
        seqs.add(tuple(d[i : i + 4]))


print(f"Part B: {seq_prices.most_common()[0]}")
