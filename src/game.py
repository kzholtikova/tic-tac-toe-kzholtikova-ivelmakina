FIRST_PLAYER = 'X'
SECOND_PLAYER = 'O'
FIELD_SIZE = 3

is_valid_coordinate = lambda x: 0 <= x < FIELD_SIZE
coordinate_to_index = lambda x: int(x) - 1


def is_cell_free(row, col, field):
    return field[row][col] == '_'


def input_move(field):
    is_valid_move = False
    while not is_valid_move:
        try:
            row, column = map(coordinate_to_index, input("Enter a row and a column to make a move: ").split(' '))
            if not all(map(is_valid_coordinate, (row, column))):
                print(f"Row and column values must be in range 1-{FIELD_SIZE}.")
                continue
            if not is_cell_free(row, column, field):
                print("This cell is already taken! Choose another one.")
                continue
        except ValueError as e:
            print("Invalid numbers.")
        else:
            return row, column


def print_field(field):
    optimal_dash_num = FIELD_SIZE * 2 + 3
    print("-" * optimal_dash_num)
    for row in field:
        print("|", *row, "|")
    print("-" * optimal_dash_num)
    return


def check_winner(field):
    transposed_field = [list(row) for row in zip(*field)]
    diagonals = [field[i][i] for i in range(0, FIELD_SIZE)], [field[i][-(i + 1)] for i in range(0, FIELD_SIZE)]
    possible_wins = field + transposed_field + list(diagonals)
    return next((row[0] for row in possible_wins if row.count(row[0]) == FIELD_SIZE and row[0] != '_'), None)


def congratulate_player(winner):
    return print(f"{winner} won. Cheers!")


def play_round():
    game_field = [["_"] * FIELD_SIZE for _ in range(FIELD_SIZE)]
    current_player = FIRST_PLAYER

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
