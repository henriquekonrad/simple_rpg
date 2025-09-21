import random

class Loot:
    @staticmethod
    def gerar_espada(tipo):
        if tipo == "Ferro":
            bonus = random.randint(5, 15)
        elif tipo == "Aço":
            bonus = random.randint(40,60)
        return f"Espada de {tipo} +{bonus}", bonus
    
    @staticmethod
    def gerar_martelo():
        bonus = random.randint(15, 30)
        return f"Martelo de Pedra +{bonus}", bonus
    
    @staticmethod
    def gerar_armadura(tipo):
        if tipo == "Couro":
            bonus = random.randint(5, 15)
        elif tipo == "Ferro":
            bonus = random.randint(15, 25)
        elif tipo == "Aço":
            bonus = random.randint(30,40)
        return f"Armadura de {tipo} +{bonus}", bonus
    
    @staticmethod
    def gerar_pocao():
        bonus = random.randint(10, 25)
        return f"Poção de Vida +{bonus}", bonus