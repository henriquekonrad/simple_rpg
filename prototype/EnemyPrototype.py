import copy

class EnemyPrototype:
    def __init__(self, enemy):
        self.enemy = enemy

    def clone(self):
        return copy.deepcopy(self.enemy)
