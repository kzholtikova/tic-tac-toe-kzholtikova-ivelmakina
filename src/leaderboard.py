LEADERBOARD_PATH = "leaderboard.tsv"


class Player:
    def __init__(self, username, victories=0, defeats=0, ties=0):
        self.username = username
        self.victories = victories
        self.defeats = defeats
        self.ties = ties

    def __str__(self):
        return f"{self.username}\t{self.victories}\t{self.defeats}\t{self.ties}"

    def welcome_message(self):
        all_usernames = [player.username for player in Leaderboard().players]
        if self.username in all_usernames:
            print(f"Hi, {self.username}. Welcome again!")
        else:
            print(f"Hi, {self.username}! Good luck!")


class Leaderboard:
    def __init__(self):
        self.players = []
        self.load_leaderboard()

    def load_leaderboard(self):
        try:
            with open(LEADERBOARD_PATH, "r") as file:
                self.players = []
                for line in file:
                    username, victories, defeats, ties = line.strip().split("\t")
                    victories, defeats, ties = map(int, (victories, defeats, ties))
                    self.players.append(Player(username, victories, defeats, ties))
        except FileNotFoundError as e:
            pass

    @staticmethod
    def add_player(player: object):
        with open(LEADERBOARD_PATH, "a") as file:
            file.write(player.__str__() + "\n")