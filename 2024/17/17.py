from math import pow
from collections import deque

with open("input") as f:
    data = f.read().strip().split("\n\n")

registers = {"ABC"[i]: int(v.split()[2]) for i, v in enumerate(data[0].split("\n"))}
program = list(map(int, data[1].split()[1].split(",")))

registers["IP"] = 0


def combo(n):
    return (0, 1, 2, 3, registers["A"], registers["B"], registers["C"], None)[n]


def adv(op):
    op = combo(op)
    registers["A"] = int(registers["A"] / pow(2, op))
    registers["IP"] += 2


def bdv(op):
    op = combo(op)
    registers["B"] = int(registers["A"] / pow(2, op))
    registers["IP"] += 2


def cdv(op):
    op = combo(op)
    registers["C"] = int(registers["A"] / pow(2, op))
    registers["IP"] += 2


def bxl(op):
    registers["B"] = registers["B"] ^ op
    registers["IP"] += 2


def bst(op):
    op = combo(op)
    registers["B"] = op % 8
    registers["IP"] += 2


def jnz(op):
    if registers["A"] != 0:
        registers["IP"] = op
    else:
        registers["IP"] += 2


def bxc(op):
    registers["B"] = registers["B"] ^ registers["C"]
    registers["IP"] += 2


def out(op):
    op = combo(op) % 8
    registers["IP"] += 2
    return op


#             0    1    2    3    4    5    6    7
commands = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def run():
    output = []
    while registers["IP"] < len(program):
        cmd = program[registers["IP"]]
        op = program[registers["IP"] + 1]
        v = commands[cmd](op)
        if v is not None:
            output.append(v)
    return output


# Part A
print(",".join(map(str, run())))

# Part B
# had to read up on some of the approaches on reddit for this, doubt I would have
# got it by myself
partials = deque(
    [(0, len(program) - 1)]
)  # BFS - DFS finds a higher soln before the lower one
found = False
while partials and not found:
    A, pos = partials.popleft()
    for i in range(8):
        registers = {"A": A * 8 + i, "B": 0, "C": 0, "IP": 0}
        o = run()
        if o == program[pos:]:  # how much of the solution are we checking?
            if pos == 0:  # gotten to the beginning and a complete match
                A = A * 8 + i
                found = True
                break
            partials.append((A * 8 + i, pos - 1))


print(f"Part B: {A}")
