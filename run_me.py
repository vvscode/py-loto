#!/usr/bin/env python3
import random
from os import system, name 
import time

from game import Game
from player import Player
from player_view import print_player

def clear_console(): 
  system('cls' if name == 'nt' else 'clear')

# Setup game
game = Game()

names = ['Bob', 'Sam', 'Martin', 'Anna', 'Clar']
number_of_players = random.randint(1, len(names))
players = []
for i in range(number_of_players):
  player_name = names[i % len(names)]
  number_of_cards = random.randint(1, 2)
  player = Player(player_name)
  for j in range(number_of_cards):
    player.add_card(game.get_card_numbers())
  players.append(player)

# Game loop
def get_winner():
  return next(filter(lambda player: player.is_winner(), players), None)

print('Game start')
step_index = 1
while not bool(get_winner()) and not game.is_finished():
  # time.sleep(1)
  clear_console()
  step_number = game.get_next_number()
  print(f'Step #{step_index}: {step_number}')
  step_index += 1
  for player in players:
    player.step(step_number)
    print_player(player)

winner = get_winner()
if winner is not None:
  print(f'Player "{winner.name}" won on step #{step_index}')
