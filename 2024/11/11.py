from functools import cache

with open("input") as f:
    data = f.read().strip().split()

# Rules:
# 0 repaced with 1
# even number of digits, gets split into two stones, left has left digits, right has right, strip leading zeroes
# else replaced with new stone *= 2024


# this caches the function so previously seen arguments won't need to be recalculated
# it's quite quick without it, but I wanted to at least use it :)
@cache
def transform(n):
    lk = len(n)
    if n == "0":
        return "1"
    elif lk % 2 == 0:
        lv = n[: lk // 2]
        rv = n[lk // 2 :].lstrip("0")
        if rv == "":
            rv = "0"
        return lv, rv
    else:
        return str(int(n) * 2024)


# ignore the order of the stones and just keep them in a dictionary in the format:
# { num_as_string: amount_we_currently_have, ... }
def blink(iters, nums):
    for _ in range(iters):
        # use a list version of the current dictionary so we don't accidentally
        # mutate results while we're calculating
        for k, v in list(nums.items()):
            n = transform(k)
            if isinstance(n, tuple):
                # add the v new numbers
                nums[n[0]] = nums.get(n[0], 0) + v
                nums[n[1]] = nums.get(n[1], 0) + v
                # reduce the old number by v
                nums[k] -= v
            else:
                # add the v transformed numbers
                nums[n] = nums.get(n, 0) + v
                # reduce the v old numbers
                nums[k] -= v

    return sum(nums.values())


initial_nums = {n: 1 for n in data}
print(f"Part A: {blink(25, initial_nums)}")
initial_nums = {n: 1 for n in data}
print(f"Part B: {blink(75, initial_nums)}")
