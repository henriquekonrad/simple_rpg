# equipment/EquipmentManager.py

class EquipmentManager:
    def __init__(self, base_hero):
        self.base_hero = base_hero
        self.weapon = None
        self.armor = None
    
    @property
    def name(self):
        return self.base_hero.name
    
    @property
    def hp(self):
        return self.base_hero.hp
    
    @hp.setter
    def hp(self, value):
        self.base_hero.hp = value
    
    @property
    def attack(self):
        base_attack = self.base_hero.attack
        weapon_bonus = self.weapon.attack_bonus if self.weapon else 0
        return base_attack + weapon_bonus
    
    @property
    def defense(self):
        armor_bonus = self.armor.defense_bonus if self.armor else 0
        return armor_bonus
    
    def equip_weapon(self, attack_bonus, name=""):
        print(f"[EQUIPAMENTO] {name} equipado!")
        if self.weapon:
            print(f"[EQUIPAMENTO] {self.weapon.name} foi substituído!")
        self.weapon = type('Weapon', (), {'attack_bonus': attack_bonus, 'name': name})()
    
    def equip_armor(self, defense_bonus, name=""):
        print(f"[EQUIPAMENTO] {name} equipado!")
        if self.armor:
            print(f"[EQUIPAMENTO] {self.armor.name} foi substituído!")
        self.armor = type('Armor', (), {'defense_bonus': defense_bonus, 'name': name})()
    
    def set_attack_strategy(self, strategy):
        self.base_hero.set_attack_strategy(strategy)
    
    def attack_enemy(self, enemy):
        if self.base_hero.attack_strategy:
            damage = self.base_hero.attack_strategy.attack(self)
        else:
            damage = self.attack
        
        if hasattr(enemy, 'take_damage'):
            enemy.take_damage(damage)
        else:
            enemy.hp -= damage
        print(f"{self.name} atacou {enemy.name} causando {damage} de dano!")
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.base_hero.hp -= actual_damage
        if self.defense > 0:
            print(f"{self.name} bloqueou {damage - actual_damage} de dano com armadura!")
        return actual_damage