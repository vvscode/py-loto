import random

class Game():
  def __init__(self):
    self.numbers = list(range(1, 91))
    self.card_numbers = []
    random.shuffle(self.numbers)

  def is_finished(self):
    return len(self.numbers) == 0

  def get_next_number(self):
    return self.numbers.pop()

  def get_card_numbers(self):
    numbers = list(range(1, 91))
    random.shuffle(numbers)
    numbers = numbers[0:15]
    numbers.sort()
    if numbers in self.card_numbers:
      return self.get_card_numbers()

    self.card_numbers.append(numbers)
    return numbers