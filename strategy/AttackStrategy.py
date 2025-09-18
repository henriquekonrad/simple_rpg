class SwordAttack:
    def attack(self, character):
        return character.attack + 5  # espada dá +5 de dano

class MagicAttack:
    def attack(self, character):
        return character.attack + 10  # magia dá +10 de dano
    
class ClawAttack:
    def attack(self, character):
        return character.attack +- 5 # garra é mais arriscada de utilizar