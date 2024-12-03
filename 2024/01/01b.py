with open("input") as f:
    data = f.read().strip().split("\n")
total = 0
data = [tuple(map(int, x.split())) for x in data]
first = [x[0] for x in data]
second = [x[1] for x in data]
for n in first:
    if n not in second:
        continue
    total += n * second.count(n)
print(total)