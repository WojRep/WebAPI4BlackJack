import uuid


class Game(object):
    """
    Klasa od prowadzenia gry
    """
    def __init__(self, *args, **kwargs):
        """
        Tworzymy grę z graczami

        Args:
            players (int): Ilość graczy
        """
        self.players = []
        self.deck = []
        self.guid = uuid.uuid4()

    def new_player(self, name):
        self.players.append(Player(name))

    def new_game(self, players_name = ["Player1"]):
        self.new_player("Croupier")
        for player in players_name:
            self.new_player(player)


