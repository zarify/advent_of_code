from functools import reduce
import operator

with open("6_1.txt") as f:
  data = f.read().splitlines()
  races = {}
  combos = []
  data[0] = data[0].replace(" ", "")
  data[1] = data[1].replace(" ", "")
  for t,d in zip(data[0].split(":")[1:], data[1].split(":")[1:]):
    t, d = int(t), int(d)
    combos.append(len([b for b in range(1, int(t)) if (b*t-b**2) > d]))
  print(combos)