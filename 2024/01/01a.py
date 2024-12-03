with open("input") as f:
    data = f.read().strip().split("\n")
total = 0
data = [tuple(map(int, x.split())) for x in data]
for x, y in zip(sorted([x[0] for x in data]), sorted([x[1] for x in data])):
    total += abs(x - y)
print(total)