class ArmorDecorator:
    def __init__(self, hero, defense_bonus):
        self.hero = hero
        self.defense_bonus = defense_bonus
    
    @property
    def name(self):
        return self.hero.name
    
    @property
    def hp(self):
        return self.hero.hp
    
    @hp.setter  # ← ESTAVA FALTANDO O .setter
    def hp(self, value):
        self.hero.hp = value
    
    @property
    def attack(self):
        return self.hero.attack
    
    @property
    def defense(self):
        base_defense = getattr(self.hero, 'defense', 0)
        return base_defense + self.defense_bonus
    
    def set_attack_strategy(self, strategy):
        self.hero.set_attack_strategy(strategy)
    
    def attack_enemy(self, enemy):
        self.hero.attack_enemy(enemy)
    
    def take_damage(self, damage):
        # Aplica a defesa ao receber dano
        defense = getattr(self, 'defense', 0)
        actual_damage = max(1, damage - defense)  # Mínimo 1 de dano
        self.hero.hp -= actual_damage
        if defense > 0:
            print(f"{self.name} bloqueou {damage - actual_damage} de dano com armadura!")
        return actual_damage