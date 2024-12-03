def build_map(t):
  dsts = {}
  for val in t:
    d, s, r = val.split()
    s, d, r = int(s), int(d), int(r)
    dsts[d] = [s, r]
  return dsts

def in_seeds(v, seeds):
  for s, r in seeds:
    if v >= s and v < s + r:
      return True
  return False

with open("5_1.txt") as f:
  data = f.read().split("\n\n")
  seeds = [int(x) for x in data[0].split()[1:]]
  actuals = []
  for i in range(len(seeds))[::2]:
    actuals.append([seeds[i], seeds[i+1]])
  actuals = sorted(actuals, key=lambda x: x[0])

  maps = []
  for line in data[1:]:
    maps.append(build_map(line.split("\n")[1:]))
  maps = maps[::-1]

  val = 0
  while True:
    v = val
    for m in maps:
        for d, (s, r) in m.items():
            if v >= d and v < d + r:
                off = v - d
                v = s + off
                break

    if in_seeds(v, actuals):
      break
    val += 1
  print(val)