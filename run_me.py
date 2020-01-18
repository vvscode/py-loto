#!/usr/bin/env python3
import random
from os import system, name
import time

from .py_loto.game import Game
from .py_loto.player import Player
from .py_loto.printer import Printer


def clear_console():
    system("cls" if name == "nt" else "clear")


# Setup game
game = Game()

names = ["Bob", "Sam", "Martin", "Anna", "Clar"]
number_of_players = random.randint(1, 2)
players = []
printer = Printer()
for i in range(number_of_players):
    player_name = names[i % len(names)]
    number_of_cards = random.randint(1, 2)
    player = Player(player_name)

    for j in range(number_of_cards):
        player.add_card(game.get_card_numbers())

    game.add_player(player)


def get_game_step_printer():
    step_index = 1

    def print_game_step(step_number):
        nonlocal step_index
        time.sleep(0.5)
        clear_console()
        step_number = game.get_next_number()
        print(f"Step #{step_index}: {step_number}")
        step_index = step_index + 1
        for player in game.players:
            printer.print_player(player)

    return print_game_step


game.set_on_game_step(get_game_step_printer())
print("Game start")
game.start()

winner = game.get_winner()
if winner is not None:
    print(f'Player "{winner.name}" won on step #{step_index}')
