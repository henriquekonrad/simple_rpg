from characters.Hero import Hero

class HeroBuilder:
    def __init__(self):
        self.name = "Hero"
        self.hp = 100
        self.attack = 10

    def set_name(self, name):
        self.name = name
        return self

    def set_hp(self, hp):
        self.hp = hp
        return self

    def set_attack(self, attack):
        self.attack = attack
        return self

    def build(self):
        return Hero(self.name, self.hp, self.attack)