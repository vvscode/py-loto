from py_loto.card import Card


def test_instantiating():
    card = Card([1, 2])
    assert card.is_full() == False, "New card should not be full"


def test_fullfilling():
    card = Card([1, 2])
    card.step(1)
    card.step(2)
    assert card.is_full() == True, "New card should be full"
