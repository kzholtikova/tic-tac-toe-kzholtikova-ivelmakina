is_valid_name = lambda x: x.strip() != ""


def ask_name(input_text):
    name = input(input_text)
    while not is_valid_name(name):
        print("Please, enter player's name.")
        name = input(input_text)
    return name
