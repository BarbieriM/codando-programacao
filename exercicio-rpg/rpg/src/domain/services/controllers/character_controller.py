from src.domain.models import Character

class CharacterController:
    def attack(self, character:Character) -> int:
        raise NotImplementedError()

    def block(self, character: Character) -> Character:
        raise NotImplementedError()

    def heal(self, character: Character) -> Character:
        raise NotImplementedError()
    
    def rest(self, character: Character) -> Character:
        raise NotImplementedError()
    
    def level_up(self, character:Character) -> Character:
        raise NotImplementedError()