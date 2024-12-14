import re
import math

with open("input") as f:
    data = f.read().strip().split("\n\n")

machines = []

button_pattern = re.compile(r"Button [AB]: X\+(\d+), Y\+(\d+)")
prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")

cost = {"A": 3, "B": 1}

for a, b, prize in [d.split("\n") for d in data]:
    ax, ay = map(int, re.match(button_pattern, a).groups())
    bx, by = map(int, re.match(button_pattern, b).groups())
    px, py = map(int, re.match(prize_pattern, prize).groups())
    machines.append({"P": (px, py), "A": (ax, ay), "B": (bx, by)})

big_machines = [
    {
        "P": (mach["P"][0] + 10000000000000, mach["P"][1] + 10000000000000),
        "A": mach["A"],
        "B": mach["B"],
    }
    for mach in machines
]


def cc(m):
    ax, ay = m["A"]
    bx, by = m["B"]
    px, py = m["P"]
    A = (px * by - py * bx) / (ax * by - ay * bx)
    B = (py * ax - px * ay) / (ax * by - ay * bx)
    if int(A) == A and int(B) == B:
        return int(A * cost["A"] + B * cost["B"])
    else:
        return 0


print(f"Part A: {sum([cc(m) for m in machines])}")
print(f"Part B: {sum([cc(m) for m in big_machines])}")
