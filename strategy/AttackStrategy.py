class SwordAttack:
    def attack(self, character):
        return character.attack

class MagicAttack:
    def attack(self, character):
        return character.attack + 5

class ClawAttack:
    def attack(self, character):
        return character.attack + 2