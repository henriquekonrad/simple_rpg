import random

def gerar_espada():
    bonus = random.randint(10, 25)
    return f"Espada de Ferro +{bonus}", bonus

def gerar_martelo():
    bonus = random.randint(15, 30)
    return f"Martelo de Pedra +{bonus}", bonus

def gerar_armadura(tipo):
    if tipo == "Couro":
        bonus = random.randint(5, 15)
    elif tipo == "Ferro":
        bonus = random.randint(15, 25)
    return f"Armadura de {tipo} +{bonus}", bonus

def gerar_pocao():
    bonus = random.randint(10, 25)
    return f"Poção de Vida +{bonus}", bonus