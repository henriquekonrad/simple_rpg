# eventManager/Handlers.py
from decorator.WeaponDecorator import WeaponDecorator
from decorator.ArmorDecorator import ArmorDecorator

def on_loot_drop(hero, item_name, bonus):
    print(f"[EVENT] Novo item dropado: {item_name} (+{bonus})")
    escolha = input(f"Equipar {item_name}? (s/n) ")
    
    if escolha.lower() == "s":
        if "Espada" in item_name or "Martelo" in item_name:
            # Se for EquipmentManager, usa o método equip_weapon
            if hasattr(hero, 'equip_weapon'):
                hero.equip_weapon(bonus, item_name)
            else:
                # Fallback para decorator
                hero = WeaponDecorator(hero, attack_bonus=bonus)
        elif "Armadura" in item_name:
            if hasattr(hero, 'equip_armor'):
                hero.equip_armor(bonus, item_name)
            else:
                hero = ArmorDecorator(hero, defense_bonus=bonus)
        elif "Poção" in item_name:
            hero.hp += bonus
            print(f"{hero.name} recuperou {bonus} de HP!")
    
    return hero