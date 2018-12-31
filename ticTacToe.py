import human
import computer
import gameLogic


def run():
    current_game_state = gameLogic.GameState(None)
    while True:
        print(current_game_state)
        current_game_state = current_game_state.make_move(human.get_move(current_game_state), gameLogic.PLAYER)
        print(current_game_state)
        current_game_state = current_game_state.make_move(computer.get_move(current_game_state), gameLogic.COMPUTER)
    print(current_game_state)


if __name__ == "__main__":
    try:
        run()
    except gameLogic.GameEnded:
        if gameLogic.winner != gameLogic.TIE:
            print("Player " + gameLogic.GameState.get_player(gameLogic.winner) + " Won the Game!!")
        else:
            print("It's a Tie!!")