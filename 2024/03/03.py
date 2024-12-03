import re

with open("input") as f:
    data = f.read().strip().replace("\n", "")

patternA = re.compile(r"mul\((\d+),(\d+)\)")
nums = [tuple(map(int, x)) for x in re.findall(patternA, data)]
print("Part A:", sum([x[0] * x[1] for x in nums]))

# sub out all the don't ... do matches
dataB = re.sub(r"don't\(\).+?do\(\)", "", data)
# strip off any trailing but unterminated don't
dataB = dataB[: dataB.index("don't()")] if "don't()" in dataB else dataB
nums = [tuple(map(int, x)) for x in re.findall(patternA, dataB)]
print("Part B:", sum([x[0] * x[1] for x in nums]))

# another approach, start and stop processing, treat it like a stream
# of tokens
dataC = re.findall(r"(mul\(\d+,\d+\)|don't\(\)|do\(\))", data)
total = 0
processing = True
for i, d in enumerate(dataC):
    if d == "don't()":
        processing = False
    elif d == "do()":
        processing = True
    elif processing:
        nums = tuple(map(int, d.strip("mul()").split(",")))
        total += nums[0] * nums[1]
print("Part B (method 2):", total)
