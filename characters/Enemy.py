import random

class Enemy:
    def __init__(self, name, hp, attack, loot_table=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.attack_strategy = None
        self.loot_table = loot_table or []
    
    def take_damage(self, damage):
        """Método para receber dano"""
        self.hp -= damage
        return damage
    
    def set_attack_strategy(self, strategy):
        self.attack_strategy = strategy
    
    def attack_hero(self, hero):
        if self.attack_strategy:
            damage = self.attack_strategy.attack(self)
        else:
            damage = self.attack
        
        # Usar take_damage ao invés de modificar HP diretamente
        if hasattr(hero, 'take_damage'):
            actual_damage = hero.take_damage(damage)
            print(f"{self.name} atacou {hero.name} causando {actual_damage} de dano!")
        else:
            hero.hp -= damage
            print(f"{self.name} atacou {hero.name} causando {damage} de dano!")
    
    def drop_loot(self):
        loot_drops = []
        for item_func, chance in self.loot_table:
            if random.random() < chance:
                item_name, bonus = item_func()
                loot_drops.append((item_name, bonus))
        return loot_drops