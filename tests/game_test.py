from ..py_loto.game import Game
from ..py_loto.player import Player


def test_is_finished():
    player_sam = Player('Sam')
    player_sam.add_card([1, 2, 3])

    player_bob = Player('Bob')
    player_bob.add_card([10, 11])

    game = Game()
    game.add_player(player_sam)
    game.add_player(player_bob)

    assert game.is_finished() == False, 'No winners in game - game is not finished'

    player_sam.step(1)
    assert game.is_finished() == False, 'No winners in game - game is not finished'

    player_sam.step(2)
    assert game.is_finished() == False, 'No winners in game - game is not finished'

    player_sam.step(3)
    assert game.is_finished() == True, 'We have winner - game is done'

    assert game.get_winner() == player_sam, 'The one who won is winner'


def test_get_card_numbers():
    game = Game()

    cards = []
    for i in range(10):
        card_numbers = game.get_card_numbers()
        assert card_numbers not in cards, 'All cards should be uniq'
        cards.append(card_numbers)


def test_get_next_number():
    game = Game()

    numbers = []
    for i in range(1, 91):
        numbers.append(game.get_next_number())

    numbers.sort()
    assert numbers == list(
        range(1, 91)), 'Should generate all numbers from 1 to 91'


def test_start():
    game = Game()
    player_sam = Player('Sam')
    player_sam.add_card(game.get_card_numbers())

    player_bob = Player('Bob')
    player_bob.add_card(['Some', 'failing', 'card'])

    game.add_player(player_sam)
    game.add_player(player_bob)

    game.start()

    assert game.is_finished() == True, 'Game finishes'
    assert player_sam.is_winner() == True, 'Sam won'
    assert player_bob.is_winner() == False, 'Bob lost'
    assert game.get_winner() == player_sam, 'Winner is correct one'
