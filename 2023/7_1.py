import re
card_vals = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
patterns = [
  r"(.)\1{4}", # five of a kind
  r"(.)\1{3}", # four of a kind
  r"(.)\1{2}(.)\2", # full house
  r"(.)\1{2}", # three of a kind
  r"(.)\1(.)\2", # two pair
  r"(.)\1", # one pair
]

def sort_hands(hand):
  cards, bid = hand
  sorted_cards = ''.join(sorted(cards, key=lambda card: (cards.count(card), card_vals.index(card)), reverse=True))
  score = 0
  for i, pattern in enumerate(patterns):
    if re.search(pattern, sorted_cards):
      score = i
      break
  else:
    score = i+1
  return (score, [card_vals.index(c) for c in cards])


with open("7_1.txt") as f:
  data = f.read().strip().split("\n")
  hands = [line.split() for line in data]
  hands.sort(key=sort_hands, reverse=True)
  total = 0
  for i, hand in enumerate(hands):
    total += (i+1) * int(hand[1])
  print(total)