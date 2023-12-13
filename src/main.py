import leaderboard

FIRST_PLAYER_SIGN = "X"
SECOND_PLAYER_SIGN = "O"

is_valid_name = lambda x: x.strip() != ""
is_valid_command = lambda x: x.lower() in ("play", "leaderboard", "clear", "quit")


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


def play():
    first_player = leaderboard.Player(ask_name("Please, enter first player's name: "))
    second_player = leaderboard.Player(ask_name("Please, enter second player's name: "))
    first_player.welcome_message()
    second_player.welcome_message()

    title_players(FIRST_PLAYER_SIGN, first_player, second_player)

def get_command():
    command = input("Please, enter one of this commands (play, leaderboard, clear, guit): ")
    while not is_valid_command(command):
        print("Please, enter a valid command (play, leaderboard, clear)")
        command = input("Please, enter one of the commands (play, leaderboard, clear, quit): ")
    return command