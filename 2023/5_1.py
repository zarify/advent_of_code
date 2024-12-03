import re

def nxt_map(vals, seeds):
  dsts = {}
  ret = []
  for val in vals:
    d, s, r = val.split()
    s, d, r = int(s), int(d), int(r)
    dsts[s] = [d, r]
  for seed in seeds:
    for s, [d, r] in dsts.items():
      if seed >= s and seed < s + r:
        off = seed - s
        ret.append(d+off)
        break
    else:
      ret.append(seed)
  return ret

with open("5_1.txt") as f:
  data = f.read().split("\n\n")
  seeds = [int(x) for x in data[0].split()[1:]]
  transforms = []
  for line in data[1:]:
    transforms.append(line.split("\n")[1:])
  for t in transforms:
    seeds = nxt_map(t, seeds)
  print(min(seeds))
