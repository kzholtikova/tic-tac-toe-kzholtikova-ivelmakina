import game
import leaderboard
import computer_player as computer

FIRST_PLAYER_SIGN = "X"
SECOND_PLAYER_SIGN = "O"

is_valid_name = lambda x: x.isalnum()
is_valid_command = lambda x: x.lower() in ("play", "leaderboard", "clear", "quit")


def get_valid_answer():
    answer = input("Do you want a return match? ")
    while answer.lower() not in ['y', 'n', 'yes', 'no']:
        answer = input("Do you want a return match? ")
    return answer.lower()
  

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
    playing = True
    while playing:
        first_player = leaderboard.Player(ask_name("Please, enter first player's name: "))
        second_player = leaderboard.Player(computer.USERNAME)
        first_player.welcome_message()
        second_player.welcome_message()
      
        print("3. 2. 1. GO!!!")
        winner = game.play_round()
        title_players(winner, first_player, second_player)
          
        playing = get_valid_answer() in ['y', 'yes']

    print("Bye!")


def get_command():
    command = input("Please, enter one of this commands (play, leaderboard, clear, guit): ")
    while not is_valid_command(command):
        print("Please, enter a valid command (play, leaderboard, clear)")
        command = input("Please, enter one of the commands (play, leaderboard, clear, quit): ")
    return command


def execute_command(command):
    if command == "play":
        play()
    elif command == "leaderboard":
        leaderboard.Leaderboard().display_leaderboard()
    elif command == "clear":
        leaderboard.Leaderboard().clear_leaderboard()

        
def main():
    command = get_command()
    while command != "quit":
        execute_command(command)
        command = get_command()

    print("Okay, see you!")
    exit()


main()
