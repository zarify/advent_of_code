import re

with open("4_1.txt") as f:
  total = 0
  data = f.read().strip().split("\n")
  for card in data:
    m = re.match(r"Card\s+(\d+):\s+(.+) \|\s+(.+)", card)
    c_num = m.group(1)
    winning = m.group(2).split()
    on_card = m.group(3).split()
    n_winning = [x for x in on_card if x in winning]
    total += (2 ** (len(n_winning)-1)) if n_winning else 0
    #print(f"Card {c_num}: {len(n_winning)} winning numbers {n_winning} {(2 ** (len(n_winning)-1)) if n_winning else 0}")
  print(total)