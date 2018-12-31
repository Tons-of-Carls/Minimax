from gameState import GameState
from gameState import InvalidMove

PLAYER = -1
COMPUTER = 1
TIE = 0
NO_PLAYER = None

winner = NO_PLAYER


class GameEnded(Exception):
    pass


def _all_same(row: [int]):
    global winner
    if row == [PLAYER, PLAYER, PLAYER]:
        winner = PLAYER
        return True
    elif row == [COMPUTER, COMPUTER, COMPUTER]:
        winner = COMPUTER
        return True
    return False


def _check_winner(state: GameState) -> bool:
    return _all_same(state.get_first_column())       or \
           _all_same(state.get_first_row())          or \
           _all_same(state.get_second_column())      or \
           _all_same(state.get_second_row())         or \
           _all_same(state.get_third_column())       or \
           _all_same(state.get_third_row())          or \
           _all_same(state.get_top_left_diagonal())  or \
           _all_same(state.get_top_right_diagonal())


def check_winner(state: GameState) -> int or None:
    global winner
    if _check_winner(state):
        return winner
    elif len(state.get_possible_moves()) == 0:
        winner = TIE
        return TIE
    return NO_PLAYER


print("game logic")