from card_view import print_card

def print_player(player):
  is_winner = player.is_winner

  print(f'---\nPlayer "{player.name}')

  for card_num, card in enumerate(player.cards, start=1):
    print(f'Card #{card_num}')
    print_card(card)

  print('\n')
