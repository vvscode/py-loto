from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, numbers):
        self.cards.append(Card(numbers))

    def is_winner(self):
        return any(card.is_full() for card in self.cards)

    def step(self, number):
        for card in self.cards:
            card.step(number)
