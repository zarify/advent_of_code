import re

def validate(prev, nxt, curr):
    symbols = {'&', '/', '=', '$', '@', '#', '*', '+', '%', '-'}
    s = (prev if prev else '') + curr + (nxt if nxt else '')
    return any(c in symbols for c in s)

with open("3_1.txt") as f:
    total = 0
    data = f.read().strip().split("\n")
    for i,d in enumerate(data):
        for m in re.finditer(r"\b(\d+)\b", d):
            print(f"Start: {m.start()}, End: {m.end()-1}, Group: {m.group()}")
            prev = data[i-1][m.start()-(1 if m.start() > 0 else 0):m.end()+1] if i > 0 else None
            nxt = data[i+1][m.start()-(1 if m.start() > 0 else 0):m.end()+1] if i < len(data) - 1 else None
            curr = d[m.start()-(1 if m.start() > 0 else 0):m.end()+1]
            valid = validate(prev, nxt, curr)
            # print(f"\tprev: {prev}, nxt: {nxt}, curr: {curr} {'✅' if valid else '❌'}")
            if valid:
                total += int(m.group())
    print(total)