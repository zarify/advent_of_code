from functools import cache

with open("input") as f:
    data = f.read().strip().split("\n\n")

designs = data[0].split(", ")  # available towel designs
patterns = data[1].split("\n")  # patterns to match


@cache
def find_matches(to_match):
    # reached the end successfully
    if to_match == "":
        return 1
    total = 0
    for d in designs:
        if to_match.startswith(d):
            total += find_matches(to_match[len(d) :])
    return total


# Part A
print(f"Part A: {sum([find_matches(p) > 0 for p in patterns])}")

# Part B
print(f"Part B: {sum([find_matches(p) for p in patterns])}")
