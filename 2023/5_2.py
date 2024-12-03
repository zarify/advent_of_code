

def build_map(t):
  dsts = {}
  for val in t:
    d, s, r = val.split()
    s, d, r = int(s), int(d), int(r)
    dsts[s] = [d, r]
  return dsts

def build_map2(t):
  dsts = {}
  for val in t:
    d, s, r = val.split()
    s, d, r = int(s), int(d), int(r)
    for i in range(s, s + r):
      dsts[i] = d + i
  return dsts

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
  min_val = None
  for s, r in actuals:
    for i in range(s, s + r):
      val = i
      for m in maps:
        for s, [d, r] in m.items():
          if val >= s and val < s + r:
            off = val - s
            val = d+off
            break
      if min_val is None or val < min_val:
        min_val = val



  print(min_val)
