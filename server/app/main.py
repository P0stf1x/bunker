from fastapi import FastAPI

from app.Lobby.Manager import LobbyManager

app = FastAPI()


lobby_manager = LobbyManager()


@app.get("/")
def read_root():
    return {"Hello": "Nikita"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/lobby/create")
def create_lobby():
    return lobby_manager.create_lobby()

@app.get("/lobby/delete/{id}")
def delete_lobby(id: str):
    lobby_manager.delete_lobby(id)

@app.get("/lobby/list")
def get_all_lobbies():
    return lobby_manager.get_all_lobby_ids()

@app.get("/lobby/{id}")
def get_lobby(id: str):
    return lobby_manager.get_lobby(id)