from uuid import uuid4

class Player():
    def __init__(self, name) -> None:
        self.id = self.generate_id()
        self.name = name
    
    @staticmethod
    def generate_id() -> str:
        return str(uuid4())