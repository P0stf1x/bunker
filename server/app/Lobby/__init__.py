from uuid import uuid4

class Lobby():
    def __init__(self) -> None:
        self.id = self.generate_id()

    @staticmethod
    def generate_id() -> str:
        return str(uuid4())
