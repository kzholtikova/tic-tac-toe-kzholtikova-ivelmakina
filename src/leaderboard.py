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

    def record_game_results(self, winner, player1, player2):
        all_usernames = [player.username for player in Leaderboard().players]
        if player1.username not in all_usernames:
            self.add_player(player1)
        if player2.username not in all_usernames:
            self.add_player(player2)
        self.load_leaderboard()

        current_players = [player for player in self.players if player.username in [player1.username, player2.username]]
        if winner is None:
            for player in current_players:
                player.ties += 1
            return

        for player in current_players:
            if player.username == winner.username:
                player.victories += 1
            else:
                player.defeats += 1

    def save_leaderboard(self, winner, player1, player2):
        self.record_game_results(winner, player1, player2)
        self.players = sorted(self.players, key=lambda p: (-p.victories, -(p.victories + p.defeats + p.ties)))

        with open(LEADERBOARD_PATH, "w") as file:
            for player in self.players:
                file.write(player.__str__() + "\n")

    def display_leaderboard(self):
        if len(self.players) == 0:
            print("There were no any rounds yet :(")
            return

        print("{:<20} {:<3} {:<3} {:<3}".format("player", "w", "d", "l"))
        print("-" * 30)

        for rank, player in enumerate(self.players, start=1):
            print("{:<1}. {:<17} {:<3} {:<3} {:<3}".format(rank, player.username, player.victories, player.defeats,
                                                           player.ties))

    @staticmethod
    def clear_leaderboard():
        file = open(LEADERBOARD_PATH, "w")
        file.close()
