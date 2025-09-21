from builder.HeroBuilder import HeroBuilder
from characters.Enemy import Enemy
from prototype.EnemyPrototype import EnemyPrototype
from strategy.AttackStrategy import SwordAttack, MagicAttack, ClawAttack
from equipment.EquipManager import EquipmentManager
from eventManager.EventManager import EventManager
from eventManager.Handlers import on_loot_drop
from decorator.ArmorDecorator import ArmorDecorator
from loot.Loot import Loot
import random

def mostrar_status(hero, enemies):
    print(f"\n=== STATUS ===")
    defense = getattr(hero, 'defense', 0)
    print(f"{hero.name} HP: {hero.hp} | ATK: {hero.attack} | DEF: {defense}")
    
    # Mostrar equipamentos
    if hasattr(hero, 'weapon') and hero.weapon:
        print(f"Arma: {hero.weapon.name} (+{hero.weapon.attack_bonus} ATK)")
    if hasattr(hero, 'armor') and hero.armor:
        print(f"Armadura: {hero.armor.name} (+{hero.armor.defense_bonus} DEF)")
    
    for e in enemies:
        print(f"{e.name} HP: {e.hp}")
    print("==============\n")

event_manager = EventManager()
event_manager.subscribe("loot_drop", on_loot_drop)

# --- Criar herói com Equipment Manager ---
base_hero = HeroBuilder().set_name("Arthur").set_hp(200).set_attack(25).build()
hero = EquipmentManager(base_hero)  # Usar Equipment Manager ao invés de decorators

# --- Criar inimigos base com loot table ---
goblin_loot = [(lambda: Loot.gerar_espada("Ferro"), 0.5), (Loot.gerar_pocao, 0.3), (lambda: Loot.gerar_armadura("Couro"), 0.65)]
troll_loot = [(Loot.gerar_martelo, 0.5), (lambda: Loot.gerar_armadura("Ferro"), 0.5)]
orc_loot = [(lambda: Loot.gerar_espada("Aço"), 0.4), (lambda: Loot.gerar_armadura("Aço"), 0.54), (Loot.gerar_pocao, 0.25)]

goblin_base = Enemy("Goblin", 50, 10, goblin_loot)
troll_base = Enemy("Troll", 100, 20, troll_loot)
orc_base = Enemy("Orc", 170, 25, orc_loot)

# --- Definir waves ---
waves = [
    {
        "name": "Primeira Onda",
        "enemies": [EnemyPrototype(goblin_base).clone() for _ in range(3)]
    },
    {
        "name": "Segunda Onda", 
        "enemies": [EnemyPrototype(troll_base).clone() for _ in range(2)]
    },
    {
        "name": "Terceira Onda",
        "enemies": [
        EnemyPrototype(goblin_base).clone(),
        EnemyPrototype(troll_base).clone(), 
        EnemyPrototype(orc_base).clone()
    ]
    }
]

# --- Configura estratégia inicial do herói ---
hero.set_attack_strategy(SwordAttack())

# --- Loop principal ---
turn = 1
current_wave_index = 0
current_enemies = waves[current_wave_index]["enemies"]

print(f"\n=== Início do RPG ===")
print(f"Onda atual: {waves[current_wave_index]['name']}")

while hero.hp > 0 and current_wave_index < len(waves):
    print(f"\n--- Turno {turn} ---")
    mostrar_status(hero, current_enemies)
    
    # --- Jogador escolhe ataque ---
    escolha = input("1- Espada 2- Magia: ")
    if escolha == "1":
        hero.set_attack_strategy(SwordAttack())
    else:
        hero.set_attack_strategy(MagicAttack())
    
    # --- Atacar primeiro inimigo vivo ---
    alvo = current_enemies[0]
    hero.attack_enemy(alvo)
    
    # --- Verificar se inimigo morreu e dropar loot ---
    if alvo.hp <= 0:
        print(f"{alvo.name} foi derrotado!")
        loot = alvo.drop_loot()
        for item_name, bonus in loot:
            hero = event_manager.emit("loot_drop", hero, item_name, bonus) or hero
        current_enemies.pop(0)
    
    # --- Inimigos atacam ---
    for enemy in current_enemies:
        enemy.set_attack_strategy(ClawAttack())
        enemy.attack_hero(hero)
    
    # --- Checar se wave acabou ---
    if not current_enemies:
        current_wave_index += 1
        if current_wave_index < len(waves):
            current_enemies = waves[current_wave_index]["enemies"]
            print(f"\n=== Nova onda: {waves[current_wave_index]['name']} ===")
    
    turn += 1

# --- Fim do jogo ---
if hero.hp > 0:
    print("\nParabéns! Todos os inimigos foram derrotados!")
else:
    print("\nVocê morreu! Fim de jogo!")

# ============= ALTERNATIVA: Manter Decorators mas limitar slots =============
# Se quiser manter os decorators, posso criar um sistema que "desembrulha" 
# o herói antes de equipar um novo item do mesmo tipo.

def unwrap_decorators(hero, decorator_type):
    """Remove decorators de um tipo específico"""
    current = hero
    while hasattr(current, 'hero') and isinstance(current, decorator_type):
        current = current.hero
    return current

def equip_weapon_decorator(hero, attack_bonus):
    """Remove arma anterior e equipa nova"""
    from decorator.WeaponDecorator import WeaponDecorator
    # Remove decorators de arma existentes
    clean_hero = unwrap_decorators(hero, WeaponDecorator)
    # Mantém outros decorators (armadura)
    if isinstance(hero, ArmorDecorator):
        return WeaponDecorator(clean_hero, attack_bonus)
    else:
        return WeaponDecorator(clean_hero, attack_bonus)