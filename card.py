class Card():
  def __init__(self, numbers):
    self.numbers = []
    self.numbers.extend(numbers)
    self.crossed_numbers = []
    self.numbers.sort()

  def step(self, number):
    if number in self.numbers:
      self.crossed_numbers.append(number)
      self.crossed_numbers.sort()

  def is_full(self):
    return len(self.crossed_numbers) == len(self.numbers)