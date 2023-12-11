import game


def get_valid_answer():
    answer = input("Do you want a return match? ")
    while answer.lower() not in ['y', 'n', 'yes', 'no']:
        answer = input("Do you want a return match? ")
    return answer.lower()


def play():
    playing = True
    while playing:
        print("3. 2. 1. GO!!!")
        winner = game.play_round()
        playing = get_valid_answer() in ['y', 'yes']

    print("Bye!")


play()
