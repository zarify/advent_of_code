import re

with open("part1.txt") as f:
    data = f.read().strip().split("\n")

bags = {}
pattern = re.compile(r"(\d+) (.+) bag")
for d in data:
    bag, contents = d.split(" bags contain ")
    for b in contents.split(", "):
        if b == "no other bags.":
            bags[bag] = []
        else:
            m = pattern.match(b)
            if m:
                bags.setdefault(bag, []).append((int(m.group(1)), m.group(2)))
            else:
                print("No match", b, bag)

def can_contain(bag, target):
    if target in [b for _, b in bags[bag]]:
        return True
    return any(can_contain(b, target) for _, b in bags[bag])

# Part 1
print(sum(can_contain(bag, "shiny gold") for bag in bags))

def count_bags(bag):
    return sum(n + n * count_bags(b) for n, b in bags[bag])

# Part 2
print(count_bags("shiny gold"))