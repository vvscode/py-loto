import random

class Printer():
  def __init__(self):
    self.cards_lines = {}

  def get_cards_lines(self, card):
    card_id = id(card)
    
    if card_id in self.cards_lines:
      return self.cards_lines[card_id]

    self.cards_lines[card_id] = self.get_new_card_lines(card.numbers)
    return self.cards_lines[card_id]

  def get_new_card_lines(self, numbers):
    lines = [
      [None] * 9,
      [None] * 9,
      [None] * 9
    ]
    line_numbers = []
    line_numbers.extend(numbers)
    while line_numbers:
      number = line_numbers[-1]
      column_index = random.randint(0, 8)

      empty_lines_indexes = [index for index, row in enumerate(lines) if row[column_index] is None]

      row_index = random.choice(empty_lines_indexes)
      numbers_in_column = len(lines) - len(empty_lines_indexes)

      if numbers_in_column < 2:
        lines[row_index][column_index] = number

        line_numbers.pop()

    return lines

  def print_card(self, card):
    lines = self.get_cards_lines(card)

    def cell_str(cell_value):
      if cell_value is None:
        str_value = ''
      elif cell_value in card.crossed_numbers:
        str_value = f'[{cell_value}]'
      else:
        str_value = str(cell_value)

      return f"{str_value.center(7, '_')}|"


    print('\n'.join([
      ''.join(map(cell_str, lines[0])),
      ''.join(map(cell_str, lines[1])),
      ''.join(map(cell_str, lines[2])),
    ]))

  def print_player(self, player):
    is_winner = player.is_winner

    print(f'---\nPlayer "{player.name}')

    for card_num, card in enumerate(player.cards, start=1):
      print(f'Card #{card_num}')
      self.print_card(card)

    print('\n')
