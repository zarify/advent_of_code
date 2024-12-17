from math import pow

with open("input") as f:
    data = f.read().strip().split("\n\n")

registers = {"ABC"[i]: int(v.split()[2]) for i, v in enumerate(data[0].split("\n"))}
program = list(map(int, data[1].split()[1].split(",")))

registers["IP"] = 0

output = []


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
    output.append(op)
    registers["IP"] += 2


commands = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

# Part A
while registers["IP"] < len(program):
    cmd = program[registers["IP"]]
    op = program[registers["IP"] + 1]
    # print(cmd, op)
    commands[cmd](op)
    # print(registers, output)
print(",".join(map(str, output)))

# Part B
