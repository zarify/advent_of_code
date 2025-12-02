from math import floor, log10
import re

fn = "input"
with open(fn) as f:
    ids = [tuple(map(int, x.split("-"))) for x in f.read().strip().split(",")]

# Part 1
total = 0

for start, end in ids:
    for n in range(start, end+1):
        place = floor(log10(n) + 1)
        # don't count odd numbered 'strings'
        if place % 2 == 1:
            continue
        top = floor(n / 10**(place/2))
        bottom = n - top * 10**(place/2)
        if top == bottom:
            total += n

print(f"Part A: {total}")
if fn == "test":
    assert total == 1227775554, "Part A test checks out"

# Part 2
total = 0

for start, end in ids:
    for n in range(start, end+1):
        ns = str(n)
        m = re.fullmatch(r"^(\d+)\1+$", ns)
        if m:
            total += n

print(f"Part B: {total}")
if fn == "test":
    assert total == 4174379265, "Part B test checks out"