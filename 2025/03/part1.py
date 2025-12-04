fn = "input"
with open(fn) as f:
    data = list(list(map(int, list(x))) for x in f.read().strip().split("\n"))

def largest(row, n):
    nums = []
    idx = -1
    for i in range(n):
        # find the index of the largest number up until
        # the end of the list taking into account how many
        # numbers we have left to find
        big_idx = row.index(max(row[idx+1:len(row)-n+i+1]), idx+1)
        nums.append(row[big_idx])
        idx = big_idx
    return int(''.join(map(str, nums)))


# Part A
total = 0
for row in data:
    total += largest(row, 2)

print(f"Part A: {total}")
if fn == "test":
    assert total == 357

# Part B
total = 0
for row in data:
    total += largest(row, 12)
print(f"Part B: {total}")
if fn == "test":
    assert total == 3121910778619