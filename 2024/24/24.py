from itertools import permutations, combinations
from copy import deepcopy

with open("input") as f:
    data = f.read().strip().split("\n\n")

ops = {
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
    "OR": lambda x, y: x | y,
}

wires = {k: int(v) for k, v in [d.split(": ") for d in data[0].split("\n")]}
gates = []
in_wires = set()
for d in data[1].split("\n"):
    w_in_1, op, w_in_2, _, w_out = d.split(" ")
    in_wires.add(w_in_1)
    in_wires.add(w_in_2)
    gates.append({"in": (w_in_1, w_in_2), "op": op, "out": w_out})
    # wires without an initial state get added with None
    wires[w_out] = wires.get(w_out, None)
    wires[w_in_1] = wires.get(w_in_1, None)
    wires[w_in_2] = wires.get(w_in_2, None)


def sim(w, gates):
    # look for `w` in output wires of all gates and try to process
    # recursively try and solve input wires to get a result
    g = [g for g in gates if g["out"] == w][0]
    in1, in2 = g["in"]

    if (wval1 := wires[in1]) is None:
        wval1 = sim(in1, gates)
    if (wval2 := wires[in2]) is None:
        wval2 = sim(in2, gates)

    if wval1 is None or wval2 is None:
        print(f"\t*** Failed to calculate {w}!")
        return None

    # calculate the result
    result = ops[g["op"]](wval1, wval2)
    # wires[w] = result
    return result


def run(gates):
    out = []
    pref_wires = {}
    for prefix in "xyz":
        pref_wires[prefix] = sorted(
            [w for w in wires if w[0] == prefix and w[1:].isdigit()],
            key=lambda x: int(x[1:]),
            reverse=True,
        )

    for w in pref_wires["z"]:
        out.append(sim(w, gates))

    return pref_wires, out


def shuffle(gates, n):
    index_combos = combinations(range(len(gates)), n)

    unique_pairs = []
    for combo in index_combos:
        pairs = list(combinations(combo, 2))
        if len(pairs) == n // 2:
            unique_pairs.append(pairs)

    for pairs in unique_pairs:
        for perm in permutations(pairs):
            dcopy = deepcopy(gates)
            swaps = []
            for a, b in perm:
                swaps.extend([dcopy[a]["out"], dcopy[b]["out"]])
                dcopy[a]["in"], dcopy[b]["in"] = dcopy[b]["in"], dcopy[a]["in"]
            yield swaps, dcopy


# Part A
pref_wires, out = run(gates)
answer = int("".join(str(w) for w in out), 2)
print(f"Part A: {answer}")


# Part B
def verify(x, y, z):
    return x & y == z


x_b = [wires[w] for w in pref_wires["x"]]
y_b = [wires[w] for w in pref_wires["y"]]
x_answer = int("".join([str(wires[w]) for w in pref_wires["x"]]), 2)
y_answer = int("".join([str(wires[w]) for w in pref_wires["y"]]), 2)
print(f"X: {[0] * (len(out) - len(x_b)) + x_b}")
print(f"Y: {[0] * (len(out) - len(y_b)) + y_b}")
print(f"Z: {out}")
print(x_answer, y_answer, answer, x_answer + y_answer)

# testing test case 3 - YES, this operates as I expect it should
# dc = deepcopy(gates)
# dc[0]["in"], dc[5]["in"] = dc[5]["in"], dc[0]["in"]
# dc[1]["in"], dc[2]["in"] = dc[2]["in"], dc[1]["in"]
# _, out = run(dc)
# answer = int("".join(str(w) for w in out), 2)
# print(f"x {x_answer} y {y_answer} z {answer} {verify(x_answer, y_answer, answer)}")

# WHAT IF
# we try a different assumption - we pick a bit in the calculate 'z' that is incorrect
# run a backward sim and try flipping the gates for two of the inputs and recalc, so
# rather than trying all the combos, limit ourselves to the gates that are actually giving
# bad results

# combos = shuffle(gates, 4)  # test3 is 2 pairs [4], real is 4 [8]
# for swaps, gate_copy in combos:
#     _, out = run(gate_copy)
#     answer = int("".join(str(w) for w in out), 2)
#     if verify(x_answer, y_answer, answer):
#         print(f"Found it {swaps}")
# print(f"x: {x_answer} y: {y_answer}, z: {answer}")
# should be (3, 5) and (0, 1)
