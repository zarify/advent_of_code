from collections import deque
from collections import namedtuple
from functools import cache

data = """029A
980A
179A
456A
379A""".strip().split("\n")

realdata = """780A
539A
341A
189A
682A""".strip().split("\n")

NUMPAD = """789
456
123
X0A""".split("\n")

DPAD = """X^A
<v>""".split("\n")

DIRS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
RDIRS = {v: k for k, v in DIRS.items()}

nmap = {(x, y): c for y, row in enumerate(NUMPAD) for x, c in enumerate(row)}
dmap = {(x, y): c for y, row in enumerate(DPAD) for x, c in enumerate(row)}

Pos = namedtuple("Position", ["point", "direction"])


def cpos(c, m):
    for k, v in m.items():
        if c == v:
            return k


def traverse(p, e, mtype):
    if p == e:
        return [[Pos(p, "A")]]
    m = nmap if mtype == "num" else dmap
    seen = set()
    paths = []
    queue = deque([[Pos(p, "")]])  # positions, direction string
    while queue:
        path = queue.popleft()
        seen.add(path[-1].point)
        for d, o in DIRS.items():
            np = Pos((path[-1].point[0] + o[0], path[-1].point[1] + o[1]), d)
            if np.point == e:
                paths.append(path + [np, Pos(np.point, "A")])
                continue
            # not been here before, in the map, and not the blank space
            if np.point not in seen and np.point in m and m[np.point] != "X":
                queue.append(path + [np])
    shortest = min([len(p) for p in paths])
    return [p for p in paths if len(p) == shortest]


def explore(code, mtype):
    prev = "A"
    paths = [""]
    m = nmap if mtype == "num" else dmap
    for c in code:
        start = cpos(prev, m)
        end = cpos(c, m)
        traversals = traverse(start, end, mtype)
        prev = c

        tstrings = [
            "".join([d.direction for d in tp]) for tp in [t for t in traversals]
        ]
        forked = []
        for p in paths:
            for i, t in enumerate(tstrings):
                forked.append(p + t)
        paths = forked
    return paths


# (from, to): resulting_dpad_path
d_moves = {
    ("A", "A"): "A",
    ("^", "^"): "A",
    (">", ">"): "A",
    ("v", "v"): "A",
    ("<", "<"): "A",
    ("A", "^"): "<A",
    ("^", "A"): ">A",
    ("A", ">"): "vA",
    (">", "A"): "^A",
    ("v", "^"): "^A",
    ("^", "v"): "vA",
    ("v", "<"): "<A",
    ("<", "v"): ">A",
    ("v", ">"): ">A",
    (">", "v"): "<A",
    ("A", "v"): "<vA",
    ("v", "A"): "^>A",
    ("A", "<"): "v<<A",
    ("<", "A"): ">>^A",
    (">", "<"): "<<A",
    ("<", ">"): ">>A",
    ("<", "^"): ">^A",
    ("^", "<"): "v<A",
    (">", "^"): "<^A",
    ("^", ">"): "v>A",
}


@cache
def expand(path, depth):
    prev = "A"
    transitions = {}
    for c in path:
        transitions[(prev, c)] = transitions.get((prev, c), 0) + 1
        prev = c
    if depth == 1:
        return sum([len(d_moves[k]) * v for k, v in transitions.items()])
    else:
        total = 0
        total += sum(
            [expand(d_moves[k], depth - 1) * v for k, v in transitions.items()]
        )
        return total


total_2 = 0
total_25 = 0
for code in realdata:
    paths = explore(code, "num")
    path_val_2 = min([expand(p, 2) for p in paths])
    path_val_25 = min([expand(p, 25) for p in paths])
    code_val = int(code.rstrip("A"))
    total_2 += code_val * path_val_2
    total_25 += code_val * path_val_25
print(f"Part A: {total_2}")
print(f"Part B: {total_25}")
