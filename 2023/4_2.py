import re
import pprint

with open("4_1.txt") as f:
  card_count = {}
  data = f.read().strip().split("\n")
  for card in data:
    m = re.match(r"Card\s+(\d+):\s+(.+) \|\s+(.+)", card)
    c_num = int(m.group(1))
    card_count[c_num] = card_count.get(c_num, 0) + 1
    # print(f"Processing card {c_num} [{card_count[c_num]}]")
    winning = m.group(2).split()
    on_card = m.group(3).split()
    n_winning = [x for x in on_card if x in winning]
    # print(f"  {len(n_winning)} winning numbers: {n_winning}")
    # pprint.pprint(card_count)
    for i in range(len(n_winning)):
      card_count[c_num+i+1] = card_count.get(c_num+i+1, 0) + card_count[c_num]
    # pprint.pprint(card_count)
  # total number of cards
  print(sum(card_count.values()))