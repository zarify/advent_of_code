def find_grad(seq):
    # find the change between each pair
    return [seq[i] - seq[i+1] for i,_ in enumerate(seq[:-1])]

def check_seq(seq):
    # check if each pair has the same direction
    same_grad = all(s < 0 for s in seq) or all(s > 0 for s in seq)
    # check if the magnitude of each pair's change is within range
    slight_grad = all(abs(s) in (1,2,3) for s in seq)
    return same_grad and slight_grad

with open("input") as f:
    data = f.read().strip().split("\n")
    data = [list(map(int, x.split())) for x in data]

totalA = 0
totalB = 0
for d in data:
    grad = find_grad(d)

    # PART A:
    # check if we're ok without changes
    if check_seq(grad):
        totalA += 1
        totalB += 1
    # PART B:
    else:
        # brute force it - I'm not proud
        for i in range(len(d)):
            if check_seq(find_grad(d[:i] + d[i+1:])):
                totalB += 1
                break

print("Part A:", totalA)
print("Part B:", totalB)