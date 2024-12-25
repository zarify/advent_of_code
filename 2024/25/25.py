with open("input") as f:
    data = f.read().strip().split("\n\n")

locks = []
keys = []

for d in data:
    d = d.split("\n")
    heights = []
    for i in range(len(d[0])):
        heights.append([dl[i] for dl in d].count("#") - 1)
    (locks if d[0][0] == "#" else keys).append(heights)


# Part A
total = 0
for l in locks:
    for k in keys:
        if all([kh + lh < 6 for kh, lh in zip(l, k)]):
            total += 1
print(f"Part A: {total}")
