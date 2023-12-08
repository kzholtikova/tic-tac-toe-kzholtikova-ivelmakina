FIRST_PLAYER = 'X'
SECOND_PLAYER = 'O'


def input_move():
    return row, column


def print_field():
    return


def check_winner(row, col):
    return winner


def congratulate_player(winner):
    return winner


def play():
    game_field = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    current_player = FIRST_PLAYER
    winner = None

    while not winner:
        row, column = input_move()
        game_field[row][column] = current_player
        print_field()
        winner = check_winner(row, column)
        if winner is not None:
            congratulate_player(winner)
            return winner
        current_player = FIRST_PLAYER if current_player == SECOND_PLAYER else SECOND_PLAYER
