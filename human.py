import gameLogic


def get_move(state: gameLogic.GameState) -> (int, int):
    winner = gameLogic.check_winner(state)
    if winner is not None:
        raise gameLogic.GameEnded

    while True:
        try:
            row = int(input("Row: "))
            col = int(input("Column: "))
            if (row, col) not in state.get_possible_moves():
                raise gameLogic.InvalidMove
            return row, col
        except:
            print("Invalid Move!\nPlease pick a different spot.")