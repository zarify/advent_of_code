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


# there's definitely a nicer way to sort this :)
def sort_update(pages, rules):
    while not is_sorted(pages, rules):
        for before, after in rules:
            if before not in pages or after not in pages:
                continue
            before_idx, after_idx = pages.index(before), pages.index(after)
            if before_idx > after_idx:
                pages.insert(after_idx, before)
                pages.pop(before_idx + 1)
    return pages[len(pages) // 2]


print(f"Part B: {sum(sort_update(fix, rules) for fix in incorrect)}")
