FIRST_PLAYER = 'X'
SECOND_PLAYER = 'O'

is_valid_coordinate = lambda x: 0 <= x < 3
coordinate_to_index = lambda x: int(x) - 1


def is_cell_free(row, col, field):
    return field[row][col] == '_'


def input_move(field):
    is_valid_move = False
    while not is_valid_move:
        try:
            row, column = map(coordinate_to_index, input("Enter a row and a column to make a move: ").split(' '))
            if not all(map(is_valid_coordinate, (row, column))):
                print("Row and column values must be in range 1-3.")
                continue
            if not is_cell_free(row, column, field):
                print("This cell is already taken! Choose another one.")
                continue
        except ValueError as e:
            print("Invalid numbers.")
        else:
            return row, column


def print_field(field):
    print("-" * 3)
    for row in field:
        print("|", *row, "|")
    print("-" * 3)
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
