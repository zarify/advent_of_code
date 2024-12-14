import math

with open("input") as f:
    data = f.read().strip().split("\n")

robots = []
for d in data:
    p, v = map(lambda x: tuple(map(int, x.strip("pv=").split(","))), d.split())
    robots.append((p, v))

w, h = 101, 103
# w, h = 11, 7  # test


def vis(positions):
    for r in range(h):
        for c in range(w):
            n = positions.count((c, r))
            print(n if n else ".", end="")
        print()


# Part A
def sim(r, seconds):
    p, v = r

    dx = v[0] * seconds
    dy = v[1] * seconds

    np = ((p[0] + dx) % w, (p[1] + dy) % h)
    return np


positions = [sim(r, 100) for r in robots]
q1 = len([p for p in positions if p[0] < w // 2 and p[1] < h // 2])
q2 = len([p for p in positions if p[0] > (w // 2) and p[1] < h // 2])
q3 = len([p for p in positions if p[0] < w // 2 and p[1] > (h // 2)])
q4 = len([p for p in positions if p[0] > (w // 2) and p[1] > (h // 2)])
print(f"Part A: {q1 * q2 * q3 * q4}")

# Part B
# Damnit, I went out of my way NOT to do an interative solution and now I have to
# use one 🤣🤣🤣


def is_tightly_clustered(data, threshold):
    if len(data) < 2:
        return False  # Not enough data to determine clustering

    mean_x = sum(x for x, y in data) / len(data)
    mean_y = sum(y for x, y in data) / len(data)
    std_dev_x = math.sqrt(sum((x - mean_x) ** 2 for x, y in data) / len(data))
    std_dev_y = math.sqrt(sum((y - mean_y) ** 2 for x, y in data) / len(data))

    return std_dev_x < threshold and std_dev_y < threshold


def per_second(robs, seconds):
    robots = [[a, b] for a, b in robs]
    for s in range(1, seconds):
        for r in robots:
            p, v = r
            p = ((p[0] + v[0]) % w, (p[1] + v[1]) % h)
            r[0] = p
        # see if the data is clustered and print it out if so for visual analysis
        vals = [r[0] for r in robots]
        if is_tightly_clustered(vals, threshold=20):
            print(f"***** {s} SECONDS *****")
            vis([r[0] for r in robots])
            return

        if s % 1000 == 0:
            print(f"{s:,} seconds")


per_second(robots, 20000)
