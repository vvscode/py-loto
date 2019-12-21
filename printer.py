class Printer():

  def print_card(self, card):
    print(f'Card: {len(card.numbers)} / {len(card.crossed_numbers)}') 
    print(' '.join(map(str, card.numbers)))

  def print_player(self, player):
    is_winner = player.is_winner

    print(f'---\nPlayer "{player.name}')

    for card_num, card in enumerate(player.cards, start=1):
      print(f'Card #{card_num}')
      self.print_card(card)

    print('\n')
