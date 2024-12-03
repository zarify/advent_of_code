import re
card_vals = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
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
  sorted_cards = ''.join(sorted(cards, key=lambda card: (cards.count(card) if card != 'J' else 6, -card_vals.index(card)), reverse=True))
  # check if the first sorted card is a joker, if it is then find the next non-joker and replace
  # all jokers with that card
  if sorted_cards[0] == 'J' and sorted_cards != 'JJJJJ':
    nxt = sorted_cards.replace('J','')
    nxt = ''.join(sorted(nxt, key=lambda card: (nxt.count(card) if card != 'J' else 6, -card_vals.index(card)), reverse=True))[0]
    sorted_cards = sorted_cards.replace('J', nxt)
  score = 0
  for i, pattern in enumerate(patterns):
    if re.search(pattern, sorted_cards):
      score = i
      break
  else:
    score = i+1
  # print(cards, sorted_cards, score)
  return (score, [card_vals.index(c) for c in cards])


with open("7_1.txt") as f:
  data = f.read().strip().split("\n")
  hands = [line.split() for line in data]
  hands.sort(key=sort_hands, reverse=True)
  # print(hands)
  total = 0
  for i, hand in enumerate(hands):
    total += (i+1) * int(hand[1])
  print(total)