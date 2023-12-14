from math import inf
import game
# from game import FIRST_PLAYER, SECOND_PLAYER, get_empty_cells, check_winner -> error???


USERNAME = "computer"


def evaluate(field):
    winner = game.check_winner(field)
    if winner == game.FIRST_PLAYER:
        return -10
    elif winner == game.SECOND_PLAYER:
        return 10
    else:
        return 0


def minimax(field, depth, is_max_player):
    if depth == 0:
        score = evaluate(field)
        return [None, score]

    best = [None, -inf] if is_max_player else [None, inf]
    player = game.SECOND_PLAYER if is_max_player else game.FIRST_PLAYER

    empty_cells = game.get_empty_cells(field)
    for cell in empty_cells:
        x, y = cell[0], cell[1]
        field[x][y] = player
        new_score = minimax(field, depth - 1, not is_max_player)
        new_score[0] = cell
        field[x][y] = '_'

        if (is_max_player and new_score[1] > best[1]) or (not is_max_player and new_score[1] < best[1]):
            best = new_score
    return best


def get_best_move(field, depth):
    best_move_x, best_move_y = minimax(field, depth, True)[0]
    return best_move_x, best_move_y
