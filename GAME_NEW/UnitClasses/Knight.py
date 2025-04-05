from .Unit import Unit
from .Items import Abilities

class Knight(Unit):
   
    def __init__(self, init_name = "Knight", init_health_default = 1000, init_attack_default = 200):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default
        self.ability = Abilities("SplashAttack", 50, 4, "Knight can splash all enemy units at % power")

