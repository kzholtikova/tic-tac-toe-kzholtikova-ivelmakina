from math import inf
from game import FIRST_PLAYER, SECOND_PLAYER, FIELD_SIZE, get_empty_cells, check_winner


def evaluate(field, depth):
    # verify by depth if the game state is terminate
    """
    Evaluate the current state of the game.
    Returns:
        -10 if 'X' wins, 10 if 'O' wins, 0 for a tie, None if the game is ongoing.
    """
    # Use check_winner() here to determine if there's a winner or if the game is ongoing
    return


def get_best_move(field, depth, is_max_player):
    score = evaluate(field, depth)
    if score is not None:
        return score

    best_score = -inf if is_max_player else inf
    best_move = (-inf, -inf) if is_max_player else (inf, inf)
    player = SECOND_PLAYER if is_max_player else FIRST_PLAYER

    empty_cells = get_empty_cells(field)
    for cell in empty_cells:
        x, y = zip(*cell)
        # print(x, y)
        field[x][y] = player
        score = get_best_move(field, depth - 1, not is_max_player)
        best_score = max(best_score, score) if is_max_player else min(best_score, score)
        best_move = cell if best_score == score else best_move
        field[x][y] = '_'

    return best_move
