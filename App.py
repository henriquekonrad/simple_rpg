from builder.HeroBuilder import HeroBuilder
from characters.Enemy import Enemy
from prototype.EnemyPrototype import EnemyPrototype
from strategy.AttackStrategy import SwordAttack, MagicAttack, ClawAttack
from decorator.ArmorDecorator import ArmorDecorator
from decorator.WeaponDecorator import WeaponDecorator
from eventManager.EventManager import EventManager
from eventManager.Handlers import on_loot_drop
from loot import Loot
import random

def mostrar_status(hero, enemies):
    print(f"\n=== STATUS ===")
    print(f"{hero.name} HP: {hero.hp}")
    for e in enemies:
        print(f"{e.name} HP: {e.hp}")
    print("==============\n")

event_manager = EventManager()
event_manager.subscribe("loot_drop", on_loot_drop)

# --- Criar herói ---
hero = HeroBuilder().set_name("Arthur").set_hp(120).set_attack(20).build()
hero = ArmorDecorator(hero, defense_bonus=30)

# --- Criar inimigos base com loot table ---
goblin_loot = [(Loot.gerar_espada, 0.5), (Loot.gerar_pocao, 0.3)]
troll_loot = [(Loot.gerar_martelo, 0.5), (lambda: Loot.gerar_armadura("Couro"), 0.5)]

goblin_base = Enemy("Goblin", 50, 10, goblin_loot)
troll_base = Enemy("Troll", 100, 15, troll_loot)

# --- Definir waves ---
waves = [
    {
        "name": "Primeira Onda",
        "enemies": [EnemyPrototype(goblin_base).clone() for _ in range(3)]
    },
    {
        "name": "Segunda Onda",
        "enemies": [EnemyPrototype(troll_base).clone() for _ in range(2)]
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
    escolha = input("1- Espada  2- Magia: ")
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
        for item_name, bonus in loot:  # se seu drop retorna (nome, bonus)
            hero = event_manager.emit("loot_drop", hero, item_name, bonus) or hero
        current_enemies.pop(0)

    # --- Inimigos atacam ---
    for enemy in current_enemies:
        # Estratégia de ataque simples para inimigos
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
    print("\nVocê morreu! Fim de jogo.")
