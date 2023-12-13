import leaderboard

FIRST_PLAYER_SIGN = "X"
SECOND_PLAYER_SIGN = "O"

is_valid_name = lambda x: x.strip() != ""


def ask_name(input_text):
    name = input(input_text)
    while not is_valid_name(name):
        print("Please, enter player's name.")
        name = input(input_text)
    return name


def title_players(winner_sign, player1, player2):
    if winner_sign == FIRST_PLAYER_SIGN:
        leaderboard.Leaderboard().save_leaderboard(player1, player1, player2)
    elif winner_sign == SECOND_PLAYER_SIGN:
        leaderboard.Leaderboard().save_leaderboard(player2, player1, player2)
    else:
        leaderboard.Leaderboard().save_leaderboard(None, player1, player2)