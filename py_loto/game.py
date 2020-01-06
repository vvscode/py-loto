import random


class Game:
    def __init__(self):
        self.on_game_step = lambda step_number: None
        self.numbers = list(range(1, 91))
        self.card_numbers = []
        random.shuffle(self.numbers)
        self.players = []

    def set_on_game_step(self, on_game_step):
        self.on_game_step = on_game_step

    def get_winner(self):
        return next(filter(lambda player: player.is_winner(), self.players), None)

    def add_player(self, player):
        self.players.append(player)

    def is_finished(self):
        return len(self.numbers) == 0 or self.get_winner() is not None

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

    def start(self):
        while not self.is_finished():
            step_number = self.get_next_number()
            for player in self.players:
                player.step(step_number)
                self.on_game_step(step_number)
