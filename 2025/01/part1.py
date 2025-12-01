with open("input") as f:
    data = f.read().strip().split("\n")
    instructions = [((-1 if line[0] == "L" else 1), int(line[1:])) for line in data]

# Part A
pointer = 50
zeroes = 0

for direction, amount in instructions:
    pointer = (pointer + direction * amount) % 100
    if pointer == 0:
        zeroes += 1
print(f"Part A: {zeroes}")

# Part B

pointer = 50
zeroes = 0

for direction, amount in instructions:
    nextpointer = (pointer + direction * amount)
    zeroes +=  len([x for x in range(pointer, nextpointer, direction) if x % 100 == 0])

    pointer = nextpointer % 100

print(f"Part B: {zeroes}")