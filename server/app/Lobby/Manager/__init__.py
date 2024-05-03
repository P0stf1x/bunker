from app.Lobby import Lobby

class LobbyManager():
    def __init__(self) -> None:
        self._lobbies: dict[str, Lobby] = {}

    def create_lobby(self) -> str:
        lobby = Lobby()
        lobby_id = lobby.id
        self._lobbies.setdefault(lobby_id, lobby)
        return lobby_id

    def get_all_lobby_ids(self) -> list[str]:
        return list(self._lobbies.keys())

    def get_lobby(self, lobby_id: str) -> Lobby | None:
        return self._lobbies.get(lobby_id)

    def delete_lobby(self, lobby_id: str) -> None:
        self._lobbies.pop(lobby_id)