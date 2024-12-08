from itertools import product
import operator

with open("input") as f:
    data = {}
    for d in f.readlines():
        k, v = d.split(": ")
        k, v = int(k), tuple(map(int, v.split()))
        data[k] = v

ops = {"+": operator.add, "*": operator.mul, "||": lambda x, y: int(str(x) + str(y))}


def validate(amt, nums, oplist):
    variants = list(product(oplist, repeat=len(nums)))
    for v in variants:
        total = nums[0]
        for num, op in zip(nums[1:], v):
            total = ops[op](total, num)
            if total > amt:
                continue  # exceeded total, skip the rest
        if total == amt:
            return True
    return False


# Part A
oplist = ["+", "*"]
total = 0
for k, v in data.items():
    if validate(k, v, oplist):
        total += k
print("Part A:", total)

# Part B
oplist = ["+", "*", "||"]
total = 0
for k, v in data.items():
    if validate(k, v, oplist):
        total += k
print("Part B:", total)
