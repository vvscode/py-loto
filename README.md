## Лото

> Написать игру "Лото"
> Цель: Правила игры можно посмотреть: https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D1%82%D0%BE
> Реализуйте имитацию игры в лото.

![Gameplay](docs/gameplay.gif)

## How to run:

```bash
python3 run_me.py
```

## How to run tests:

```bash
pytest --cov=py_loto --capture=sys -vv
```

Example:

```bash
pytest --cov=py_loto --capture=sys -vv
=============================================================================== test session starts ================================================================================
platform darwin -- Python 3.7.5, pytest-5.3.2, py-1.8.1, pluggy-0.13.1 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/vvscode/repo/py-loto
plugins: cov-2.8.1
collected 12 items

py_loto/card__test.py::test_instantiating PASSED                                                                                                                             [  8%]
py_loto/card__test.py::test_fullfilling PASSED                                                                                                                               [ 16%]
py_loto/game_test.py::test_is_finished PASSED                                                                                                                                [ 25%]
py_loto/game_test.py::test_get_card_numbers PASSED                                                                                                                           [ 33%]
py_loto/game_test.py::test_get_next_number PASSED                                                                                                                            [ 41%]
py_loto/game_test.py::test_start PASSED                                                                                                                                      [ 50%]
py_loto/player_test.py::test_instantiating PASSED                                                                                                                            [ 58%]
py_loto/player_test.py::test_player_wins_on_full_card PASSED                                                                                                                 [ 66%]
py_loto/player_test.py::test_player_winds_on_any_card PASSED                                                                                                                 [ 75%]
py_loto/printer_test.py::test_print_player_with_no_cards PASSED                                                                                                              [ 83%]
py_loto/printer_test.py::test_print_player_with_single_card PASSED                                                                                                           [ 91%]
py_loto/printer_test.py::test_print_player_with_partially_filled_card PASSED                                                                                                 [100%]

---------- coverage: platform darwin, python 3.7.5-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
py_loto/__init__.py           0      0   100%
py_loto/card.py              12      0   100%
py_loto/card__test.py         9      0   100%
py_loto/game.py              33      2    94%
py_loto/game_test.py         45      0   100%
py_loto/player.py            12      0   100%
py_loto/player_test.py       28      0   100%
py_loto/printer.py           41      1    98%
py_loto/printer_test.py      51      2    96%
---------------------------------------------
TOTAL                       231      5    98%


================================================================================ 12 passed in 0.12s ================================================================================
```
