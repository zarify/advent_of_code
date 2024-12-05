with open("input") as f:
    rules, pages = f.read().strip().split("\n\n")
    rules = [tuple(map(int, x.split("|"))) for x in rules.split("\n")]
    updates = [list(map(int, x.split(","))) for x in pages.split("\n")]


def is_sorted(pages, rules):
    for before, after in rules:
        if before not in pages or after not in pages:
            continue
        if pages.index(before) > pages.index(after):
            return False
    return True


incorrect = []

# Part A:
totalA = 0
for u in updates:
    if is_sorted(u, rules):
        totalA += u[len(u) // 2]
    else:
        incorrect.append(u)

print(f"Part A: {totalA}")

# Part B:
totalB = 0


def sort_update(pages, rules):
    # strip unnecessary rules for this update
    u_rules = [(b, a) for b, a in rules if a in pages and b in pages]
    for first, second in u_rules:
        first_idx, second_idx = pages.index(first), pages.index(second)
        if first_idx > second_idx:
            # find the lowest matching index that uses the first number
            # and insert
            new_pos = min(
                [
                    pages.index(r_second)
                    for r_first, r_second in u_rules
                    if r_first == first
                ]
            )
            # shift the first number to the new position
            # and pop the old value from its (+1) position
            pages.insert(new_pos, first)
            pages.pop(first_idx + 1)
    return pages[len(pages) // 2]


print(f"Part B: {sum(sort_update(fix, rules) for fix in incorrect)}")
