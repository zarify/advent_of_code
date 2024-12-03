def all_combos(s):
    """
    Return a list of all possible combinations of the string
    replacing ? characters with either a . or a # character
    recursively.
    For example "???.###" should return ["###.###","#..###","#.#.###", ...] etc
    """
    if "?" not in s:
        return [s]
    
    combos = []
    for c in [".", "#"]:
        new_s = s.replace("?", c, 1)
        combos.extend(all_combos(new_s))
    
    return combos

def validate_combos(combos):
  valid_combos = []
  for combo in combos:
     c, p = combo.split()
     p = [int(x) for x in p.split(",")]
     c = [x for x in c.split(".") if len(x)]
     if len(c) == len(p):
        if all(len(x) == y for x, y in zip(c, p)):
          valid_combos.append(combo)
  return valid_combos

def unfold_data(data):
   for i, d in enumerate(data):
      springs, checksum = d.split()
      springs = "?".join([springs] * 5)
      checksum = ",".join([checksum] * 5)
      data[i] = springs + " " + checksum
   return data

with open("12b.txt") as f:
  data = f.read().splitlines()
  data = unfold_data(data)

  total = 0
  for d in data:
    combos = all_combos(d)
    valid_combos = validate_combos(combos)
    total += len(validate_combos(combos))
  print(total)