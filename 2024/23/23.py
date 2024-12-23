from itertools import combinations
from functools import cache

with open("input") as f:
    data = f.read().strip().split("\n")

conns = [d.split("-") for d in data]

uniques = set([a for a, _ in conns] + [b for _, b in conns])


@cache
def check_pairs(pairs):
    num_pairs = len(pairs)
    pairs_found = 0
    for a, b in pairs:
        p = ([a, b], [b, a])
        if p[0] in conns or p[1] in conns:
            pairs_found += 1
    return pairs_found == num_pairs


def find_combos(n):
    combos = tuple(combinations(uniques, n))
    print(len(tuple(combos)))  # 23M combos
    combos = [c for c in combos if any([cl[0] == "t" for cl in c])]
    print(len(tuple(combos)))  # 2.3M combos still
    found = []
    for i, combo in enumerate(combos):
        pairs = tuple(combinations(combo, 2))
        if check_pairs(pairs):
            found.append(tuple(combo))
        if i % 1000 == 0:
            print(f"{i}, found {len(found)}")
    return found


# Part A
combos = find_combos(3)
t_start = sum([any([c[0] == "t" for c in combo]) for combo in combos])
print(f"Part A: {t_start}")
