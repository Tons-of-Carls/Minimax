import gameLogic
import time


def get_move(state: gameLogic.GameState) -> (int, int):
    # start_time = time.monotonic()
    winner = gameLogic.check_winner(state)
    if winner is not None:
        raise gameLogic.GameEnded

    possible_moves = state.get_possible_moves()
    heuristic = []

    for move in possible_moves:
        heuristic.append((minimax(state.make_move(move, gameLogic.COMPUTER), False), move))
        if heuristic[-1][0] == 1:
            return heuristic[-1][1]

    try:
        # return time.monotonic() - start_time
        return max(heuristic, key=lambda move_set : move_set[0])[1]
    except ValueError:
        print("Value Error Raised: seems to be no possible moves : get_move")
        print("Possible Moves: " + str(possible_moves))
        print("Heuristic: " + str(heuristic))
        print("Winner Variable: " + str(winner))
        print(state)
        return gameLogic.TIE


def get_max_min_player(maximizer):
    return gameLogic.COMPUTER if maximizer else gameLogic.PLAYER


def minimax(state: gameLogic.GameState, maximizer: bool) -> int:
    winner = gameLogic.check_winner(state)
    if winner is not None:
        return winner

    possible_moves = state.get_possible_moves()
    heuristic = []

    for move in possible_moves:
        heuristic.append(minimax(state.make_move(move, get_max_min_player(maximizer)), not maximizer))
        if heuristic[-1] == get_max_min_player(maximizer):
            return heuristic[-1]


    try:
        if maximizer:
            return max(heuristic)
        else:
            return min(heuristic)
    except ValueError:
        print("Value Error Raised: seems to be no possible moves : minimax")
        print("Possible Moves: " + str(possible_moves))
        print("Heuristic: " + str(heuristic))
        print("Winner Variable: " + str(winner))
        print("Maximizer: " + str(maximizer))
        print(state)
        return gameLogic.TIE