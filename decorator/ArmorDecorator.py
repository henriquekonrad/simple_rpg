class ArmorDecorator:
    def __init__(self, hero, defense_bonus):
        self.hero = hero
        self.defense_bonus = defense_bonus
        self.name = hero.name
        self.hp = hero.hp + defense_bonus
        self.attack = hero.attack

    def set_attack_strategy(self, strategy):
        self.hero.set_attack_strategy(strategy)

    def attack_enemy(self, enemy):
        self.hero.attack_enemy(enemy)