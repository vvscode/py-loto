import inspect
import pathlib
import unittest.mock as mock

from py_loto.printer import Printer
from py_loto.player import Player

dir = pathlib.Path(__file__).parent.absolute()


def get_random_int_mock():
    i = 0

    def random_randint(a, b):
        nonlocal i
        r = a + i
        i = i + 1
        return r

    return random_randint


def get_random_choice_mock():
    i = 0

    def random_randint(a):
        nonlocal i
        r = a[i]
        i = i + 1
        return r

    return random_randint


def get_snapshot(snapshot_name):
    with open(f"{dir}/printer_test.{snapshot_name}.snapshot") as f:
        return f.read()


def set_snapshot(snapshot_name, content):
    with open(f"{dir}/printer_test.{snapshot_name}.snapshot", "w") as f:
        return f.write(content)


def test_print_player_with_no_cards(capsys):
    player = Player("Sam")
    printer = Printer()
    with mock.patch("random.randint", get_random_int_mock()), mock.patch(
        "random.choice", get_random_choice_mock()
    ):
        printer.print_player(player)

    captured = capsys.readouterr()
    # to update snapshot
    # set_snapshot(inspect.stack()[0][3], captured.out)

    assert captured.out == get_snapshot(
        inspect.stack()[0][3]
    ), "Should print player name if no cards"


def test_print_player_with_single_card(capsys):
    player = Player("Sam")
    printer = Printer()
    player.add_card([1, 2, 3])

    with mock.patch("random.randint", get_random_int_mock()), mock.patch(
        "random.choice", get_random_choice_mock()
    ):
        printer.print_player(player)

    captured = capsys.readouterr()

    # to update snapshot
    # set_snapshot(inspect.stack()[0][3], captured.out)

    assert captured.out == get_snapshot(
        inspect.stack()[0][3]
    ), "Should print player name if no cards"


def test_print_player_with_partially_filled_card(capsys):
    player = Player("Sam")
    printer = Printer()
    player.add_card([1, 2, 3])
    player.step(1)
    player.step(2)

    with mock.patch("random.randint", get_random_int_mock()), mock.patch(
        "random.choice", get_random_choice_mock()
    ):
        printer.print_player(player)

    captured = capsys.readouterr()

    # to update snapshot
    # set_snapshot(inspect.stack()[0][3], captured.out)

    assert captured.out == get_snapshot(
        inspect.stack()[0][3]
    ), "Should print player name if no cards"
