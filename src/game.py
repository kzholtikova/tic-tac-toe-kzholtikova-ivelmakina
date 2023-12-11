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

    while not all(row.count('_') == 0 for row in game_field):
        print(f"Current move: {current_player}")
        row, column = input_move(game_field)
        game_field[row][column] = current_player
        print_field(game_field)
        winner = check_winner(game_field)

        if winner is not None:
            congratulate_player(winner)
            return winner

        current_player = FIRST_PLAYER if current_player == SECOND_PLAYER else SECOND_PLAYER

    print("It's a tie!")
    return FIRST_PLAYER, SECOND_PLAYER
