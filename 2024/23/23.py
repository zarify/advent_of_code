from itertools import combinations
from collections import defaultdict
from collections import Counter

with open("input") as f:
    data = f.read().strip().split("\n")

conns = [d.split("-") for d in data]

uniques = set([a for a, _ in conns] + [b for _, b in conns])

# keep track of the set of computers each one links to
computers = defaultdict(set)
for a, b in conns:
    computers[a].add(b)
    computers[b].add(a)


def find_subnets(set_len):
    sets = set()
    for c in uniques:
        for k in computers[c]:
            links = [
                link for link in computers[k] if link in computers[c] and link != c
            ]
            if len(links) == 0:
                continue
            # add the links if we don't care about set length (Part B) or only
            # want to find a specific length (Part A)
            if len(links) >= set_len - 2:
                link_combos = [
                    tuple(sorted([c, k] + list(combo)))
                    for combo in combinations(links, set_len - 2)
                ]
                sets.update(set(link_combos))
    return sets


# Part A
threes = find_subnets(3)
print(f"Part A: {len([t for t in threes if any([tl[0] == 't' for tl in t])])}")


# Part B
def check_subnet(links):
    # figure out which links link to each other and count the occurences of
    # each combination
    matched_counter = Counter()
    for link in links:
        matched = set([link])
        for olink in links:
            if olink == link:
                continue
            if link in computers[olink]:
                matched.add(olink)
        if len(matched) > 2:  # everything is going to link to at least one
            matched = tuple(sorted(matched))
            matched_counter[matched] = matched_counter.get(matched, 0) + 1
    # check if the number of computers matches the number of common links
    mc = matched_counter.most_common()[0][0]
    mcl = matched_counter.most_common()[0][1]
    if len(mc) == mcl + 1:
        return mc
    else:
        return None


found = []
for c in uniques:
    subset = check_subnet(tuple([c] + list(computers[c])))
    if subset:
        found.append(subset)
longest = sorted(found, key=len)[-1]
print(f"Part B: {','.join(longest)}")
