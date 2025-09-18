class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.attack_strategy = None

    def set_attack_strategy(self, strategy):
        self.attack_strategy = strategy

    def attack_enemy(self, enemy):
        if self.attack_strategy:
            damage = self.attack_strategy.attack(self)
            enemy.hp -= damage
            print(f"{self.name} atacou {enemy.name} causando {damage} de dano!")
        else:
            enemy.hp -= self.attack
            print(f"{self.name} atacou {enemy.name} causando {self.attack} de dano!")