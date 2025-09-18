class WeaponDecorator:
    def __init__(self, hero, attack_bonus):
        self.hero = hero
        self.attack_bonus = attack_bonus
        self.name = hero.name
        self.hp = hero.hp
        self.attack = hero.attack + attack_bonus

    def set_attack_strategy(self, strategy):
        self.attack_strategy = strategy
        self.hero.set_attack_strategy(strategy)

    def attack_enemy(self, enemy):
        # se tiver estratégia, usa ela mas adiciona o bônus de ataque
        if self.attack_strategy:
            damage = self.attack_strategy.attack(self)  # passa o decorator
        else:
            damage = self.attack + self.attack_bonus  # adiciona bônus direto
        enemy.hp -= damage
        print(f"{self.name} atacou {enemy.name} causando {damage} de dano!")