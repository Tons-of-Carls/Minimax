import copy
import gameLogic


class InvalidMove(Exception):
    pass


class GameState:
    def __init__(self, state: [[int]]):
        if state is None:
            self.state = [[None, None, None],
                          [None, None, None],
                          [None, None, None]]
        else:
            self.state = state

    def make_move(self, move: (int, int), player: int):
        if self.state[move[0]][move[1]] is None:
            new_state = copy.deepcopy(self.state)
            new_state[move[0]][move[1]] = player
            return GameState(new_state)
        print("-----INVALID MOVE-----")
        print(self)
        print("Row: " + str(move[0]))
        print("Col: " + str(move[1]))
        print("Player: " + str(player))
        print("-----INVALID MOVE-----")
        raise InvalidMove

    def get_move(self, row: int, col: int) -> int:
        return self.state[row][col]

    def get_possible_moves(self) -> []:
        possible_moves = []
        for row in range(3):
            for col in range(3):
                if self.state[row][col] is None:
                    possible_moves.append((row, col))
        return possible_moves

    # Diagonals
    def get_top_left_diagonal(self):
        return [self.get_move(0, 0), self.get_move(1, 1), self.get_move(2, 2)]

    def get_top_right_diagonal(self):
        return [self.get_move(0, 2), self.get_move(1, 1), self.get_move(2, 0)]

    # Rows
    def get_first_row(self):
        return [self.get_move(0, 0), self.get_move(0, 1), self.get_move(0, 2)]

    def get_second_row(self):
        return [self.get_move(1, 0), self.get_move(1, 1), self.get_move(1, 2)]

    def get_third_row(self):
        return [self.get_move(2, 0), self.get_move(2, 1), self.get_move(2, 2)]

    def get_first_column(self):
        return [self.get_move(0, 0), self.get_move(1, 0), self.get_move(2, 0)]

    # Columns
    def get_second_column(self):
        return [self.get_move(0, 1), self.get_move(1, 1), self.get_move(2, 1)]

    def get_third_column(self):
        return [self.get_move(0, 2), self.get_move(1, 2), self.get_move(2, 2)]

    @staticmethod
    def get_player(player):
        return "X" if player == gameLogic.COMPUTER else "O"

    def __str__(self):
        game_state_string = "-------\n"
        for row in self.state:
            for player in row:
                if player is None:
                    game_state_string += "| "
                else:
                    game_state_string += "|"+GameState.get_player(player)
            game_state_string += "|\n"
            game_state_string += "-------\n"
        return game_state_string