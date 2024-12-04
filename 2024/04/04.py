with open("input") as f:
    data = f.read().strip().split("\n")


def count_xmas(s):
    return s.count("XMAS") + s[::-1].count("XMAS")


# Part A:
total = 0
# left and right for each row
for d in data:
    total += count_xmas(d)
# up and down
for i in range(len(data[0])):
    total += count_xmas("".join([d[i] for d in data]))

# diagonals - create a set of indices for diagonals
# we'll limit these for the non-square shape in the loop
x = [0] * len(data) + list(range(1, len(data[0])))
y = list(range(1, len(data)))[::-1] + [0] * len(data[0])
for c, r in zip(x, y):
    # create a diagonal from the bottom-left
    total += count_xmas(
        "".join(
            [data[r + i][c + i] for i in range(min((len(data) - r), len(data[0]) - c))]
        )
    )
    # starting from the bottom-right
    total += count_xmas(
        "".join(
            [
                data[r + i][len(data) - 1 - c - i]
                for i in range(min((len(data) - r), len(data[0]) - c))
            ]
        )
    )


print("Part A:", total)


# Part B
# Identify all the "A" character positions and then check rotations
# Originally checked top/bottom variations too, but it only wants
# diagonals
def check_x(r, c, data):
    # diagonal
    dl = (data[r - 1][c - 1] + data[r + 1][c + 1]) in ("MS", "SM")
    dr = (data[r - 1][c + 1] + data[r + 1][c - 1]) in ("MS", "SM")
    return dl and dr


total = 0
for r, d in enumerate(data):
    if r in (0, len(data) - 1):
        continue
    for c, letter in enumerate(data[r]):
        if c in (0, len(data[r]) - 1):
            continue
        if letter == "A":
            total += check_x(r, c, data)

print("Part B:", total)
