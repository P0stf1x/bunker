from uuid import uuid4
from app.Player import Player

class Lobby():
    def __init__(self) -> None:
        self.id = self.generate_id()
        self._players: dict[str, Player] = {}

    @staticmethod
    def generate_id() -> str:
        return str(uuid4())

    def add_player(self, name) -> str:
        player = Player(name)
        player_id = player.id
        self._players.setdefault(player_id, player)
        return player_id
        ...

    def get_all_player_ids(self) -> list[str]:
        return list(self._players.keys())

    def get_player(self, player_id) -> Player | None:
        return self._players.get(player_id)

    def remove_player(self, player_id) -> None:
        self._players.pop(player_id)
