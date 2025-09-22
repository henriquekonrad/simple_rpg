# ============= CORREÇÕES NECESSÁRIAS =============

# 1. CORRIGIR ArmorDecorator.py (tinha erro de sintaxe)
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

# 2. CORRIGIR WeaponDecorator.py (estava ok, só confirmando)
class WeaponDecorator:
    def __init__(self, hero, attack_bonus):
        self.hero = hero
        self.attack_bonus = attack_bonus
    
    @property
    def name(self):
        return self.hero.name
    
    @property
    def hp(self):
        return self.hero.hp
    
    @hp.setter
    def hp(self, value):
        self.hero.hp = value
    
    @property
    def defense(self):
        # Propaga defesa se existir
        return getattr(self.hero, 'defense', 0)
    
    @property
    def attack(self):
        base_attack = getattr(self.hero, 'attack', 0)
        return base_attack + self.attack_bonus
    
    def set_attack_strategy(self, strategy):
        self.hero.set_attack_strategy(strategy)
    
    def attack_enemy(self, enemy):
        if hasattr(self.hero, 'attack_strategy') and self.hero.attack_strategy:
            damage = self.hero.attack_strategy.attack(self)  # Passa o decorator
        else:
            damage = self.attack
        
        # Usar take_damage se disponível
        if hasattr(enemy, 'take_damage'):
            enemy.take_damage(damage)
        else:
            enemy.hp -= damage
        print(f"{self.name} atacou {enemy.name} causando {damage} de dano!")
    
    def take_damage(self, damage):
        # Se o herói base tem take_damage, usa ele
        if hasattr(self.hero, 'take_damage'):
            return self.hero.take_damage(damage)
        else:
            self.hero.hp -= damage
            return damage