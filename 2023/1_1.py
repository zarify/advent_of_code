import re
def coord(s):
    s = re.sub(r"\D", "", s)
    return int(s[0] + s[-1])
with open("1_1.txt") as f:
    data = f.read().strip().split("\n")
    data = [coord(x) for x in data]
    print(sum(data))