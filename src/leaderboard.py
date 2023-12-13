LEADERBOARD_PATH = "leaderboard.tsv"


class Player:
    def __init__(self, username, victories=0, defeats=0, ties=0):
        self.username = username
        self.victories = victories
        self.defeats = defeats
        self.ties = ties


class Leaderboard:
    def __init__(self):
        self.players = []

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
