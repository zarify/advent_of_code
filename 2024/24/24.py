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


# Part A
pref_wires, out = run(gates)
answer = int("".join(str(w) for w in out), 2)
print(f"Part A: {answer}")


# Part B
# adder rules: - https://www.reddit.com/r/adventofcode/comments/1hla5ql/comment/m3kws15/
# - output gate: must be ^ unless it's the last bit (z45)
# - not x,y inputs and not z output: must be &, |, not ^
# - look one ahead:
#   - a ^ with xy inputs must be ^, otherwise the input gate is faulty
#   - an & must be an | with this as an input, else the & gate is fault

out_wires = set()
for i, g in enumerate(gates):
    if g["out"][0] == "z" and g["op"] != "XOR" and g["out"] != "z45":
        out_wires.add(g["out"])
    if g["in"][0][0] not in "xy" and g["in"][1][0] not in "xy" and g["out"][0] != "z":
        if g["op"] == "XOR":
            out_wires.add(g["out"])
    if g["op"] == "XOR" and g["in"][0][0] in "xy" and g["in"][1][0] in "xy":
        sus = [ga for ga in gates if g["out"] in ga["in"] and ga["op"] == "XOR"]
        if sus == [] and g["in"] != ("x00", "y00"):
            out_wires.add(g["out"])
    if g["op"] == "AND":
        sus = [ga for ga in gates if g["out"] in ga["in"] and ga["op"] == "OR"]
        if sus == [] and g["in"] != ("x00", "y00"):
            out_wires.add(g["out"])
print(f"Part B: {','.join(sorted(out_wires))}")
