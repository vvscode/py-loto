def print_card(card):
  print(f'Card: {len(card.numbers)} / {len(card.crossed_numbers)}') 
  print(' '.join(map(str, card.numbers)))