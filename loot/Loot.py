import random

class Loot:
    @staticmethod
    def gerar_upgrade_dano(nivel):
        if nivel == 1:
            bonus = random.randint(5, 10)
        elif nivel == 2:
            bonus = random.randint(10,20)
        elif nivel == 3:
            bonus = random.randint(30,40)
        return f"upgrade de dano nível {nivel} +{bonus}", bonus
    
    @staticmethod
    def gerar_upgrade_defesa(nivel):
        if nivel == 1:
            bonus = random.randint(5, 10)
        elif nivel == 2:
            bonus = random.randint(10, 20)
        elif nivel == 3:
            bonus = random.randint(20,30)
        return f"Armadura de {nivel} +{bonus}", bonus
    
    @staticmethod
    def gerar_pocao():
        bonus = random.randint(10, 25)
        return f"Poção de Vida +{bonus}", bonus