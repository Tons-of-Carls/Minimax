import human
import computer
import gameLogic
import time

NUMBER_OF_TEST = 100

def run():
    current_game_state = gameLogic.GameState(None)

    total_time = 0

    for i in range(NUMBER_OF_TEST):
        print(i)
        total_time += computer.get_move(current_game_state)

    print(total_time / NUMBER_OF_TEST)


if __name__ == "__main__":
    run()