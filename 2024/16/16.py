with open("input") as f:
    data = f.read().strip().split("\n")

m = {}
# facings and available moves
f = {
    (0, 1): [(1, 0), (-1, 0), (0, 1)],
    (0, -1): [(1, 0), (-1, 0), (0, -1)],
    (1, 0): [(0, 1), (0, -1), (1, 0)],
    (-1, 0): [(0, 1), (0, -1), (-1, 0)],
}
facings = {(0, 1): ">", (0, -1): "<", (1, 0): "v", (-1, 0): "^"}
for r, row in enumerate(data):
    for c, v in enumerate(row):
        m[(r, c)] = "#" if v == "#" else "."
        if v == "S":
            pos = (r, c)
        elif v == "E":
            end = (r, c)


class Reindeer:
    def __init__(self, pos, facing, seen, cost):
        self.pos = pos
        self.facing = facing
        self.seen = seen
        self.cost = cost
        self.babies = []
        self.exhausted = False

    def move(self, target):
        self.babies = []  # don't want to drag the kids around!
        self.seen.add((self.pos, self.facing))
        if self.pos == target:  # arrived!
            self.exhausted = True
            return True
        # potential moves: [(pos, facing, cost), ...]
        potentials = []
        for d in f[self.facing]:
            np = (self.pos[0] + d[0], self.pos[1] + d[1])
            if m[np] == "#" or (np, d) in self.seen or np in self.path_points():
                continue
            if d == self.facing:
                # check for positions we've moved before, not turn combos
                if np in self.path_points():
                    continue
                potentials.append((np, d, self.cost + 1))
            else:
                if (self.pos, d) in self.seen:  # made this turn before
                    continue
                potentials.append((self.pos, d, self.cost + 1000))

        if len(potentials) == 0:  # this reindeer has exhausted all options
            self.exhausted = True
        else:
            # update this reindeer according to the first valid move/turn
            self.pos = potentials[0][0]
            self.facing = potentials[0][1]
            self.cost = potentials[0][2]
            # add clones for the other valid moves
            for p in potentials[1:]:
                self.babies.append(
                    Reindeer(
                        p[0],  # position
                        p[1],  # facing
                        self.seen.copy(),  # copy of seen positions and facings
                        p[2],  # cost
                    )
                )

        return False  # not arrived

    def path_points(self):
        return [p[0] for p in self.seen]

    def get_babies(self):
        return self.babies

    def can_move(self):
        return not self.exhausted

    def get_cost(self):
        return self.cost

    def __repr__(self):
        return f"{self.pos} {facings[self.facing]} cost {self.cost}"


def traverse(herd, end):
    winners = []
    global_costs = {}  # maintain global costs and use to proactively prune
    while herd:
        new_reindeer = []
        for reindeer in herd:
            # move the reindeer and check if it has arrived at end
            arrived = reindeer.move(end)
            # add any reindeer who have arrived to the winners list
            if arrived:
                winners.append(reindeer)
            # collect any new reindeer from forks in the path
            new_reindeer.extend(reindeer.get_babies())
        # prune tired reindeer from the herd and add any babies
        herd.extend(new_reindeer)

        for r in herd:
            if r.cost < global_costs.get((r.pos, r.facing), float("inf")):
                global_costs[(r.pos, r.facing)] = r.cost
            # exhaust reindeer whoses costs are higher than the current best
            # map position/facing cost
            if r.cost > global_costs.get((r.pos, r.facing), float("inf")):
                r.exhausted = True

        # exhaust reindeer, winners, and those whose costs are too high
        herd = [r for r in herd if r.can_move()]

        if winners:  # prune reindeer who have costs greater than lowest winner
            lowest = min([w.cost for w in winners])
            herd = [r for r in herd if r.cost <= lowest]
        # input("...")

    return winners


def vis(path, m):
    m = m.copy()
    for r in range(max(p[0] for p in m) + 1):
        for c in range(max(p[1] for p in m) + 1):
            if (r, c) in path:
                print("R", end="")
            else:
                print(m[(r, c)], end="")
        print()


rudolf = Reindeer(pos, (0, 1), set([pos]), 0)

# Part A
winners = traverse([rudolf], end)
min_cost = min([r.cost for r in winners])
print(f"Part A: {min_cost}")

# Part B
winners = [w for w in winners if w.cost == min_cost]
path_points = set().union(*[r.path_points() for r in winners])
print(f"Part B: {len(path_points)-1}")
