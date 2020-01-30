from .py_loto.player import Player


def test_instantiating():
    name = "Bob"
    player = Player(name)
    assert player.name == name, "Player should have name from instantiation"


def test_player_wins_on_full_card():
    player = Player("Bob")
    assert player.is_winner() == False, "No cards - no win"

    player.add_card([1, 2, 3])
    assert player.is_winner() == False, "Card is not full - no win"

    player.step(1)
    assert player.is_winner() == False, "Card is not full - no win"

    player.step(2)
    assert player.is_winner() == False, "Card is not full - no win"

    player.step(3)
    assert player.is_winner() == True, "Card is full - winner"


def test_player_winds_on_any_card():
    player = Player("Bob")
    assert player.is_winner() == False, "No cards - no win"

    player.add_card([1, 2, 3])
    player.add_card([5, 6])
    assert player.is_winner() == False, "Cards are not full - no win"

    player.step(1)
    assert player.is_winner() == False, "Cards are not full - no win"

    player.step(5)
    assert player.is_winner() == False, "Cards are not full - no win"

    player.step(6)
    assert player.is_winner() == True, "Card is full - winner"
