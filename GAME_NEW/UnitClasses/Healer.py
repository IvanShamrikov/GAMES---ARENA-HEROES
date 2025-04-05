from .Unit import Unit
from.Items import Abilities

class Healer(Unit):
   
    def __init__(self, init_name = "Healer", init_health_default = 700, init_attack_default = 150):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default
        self.ability = Abilities("SuperHeal", 20, 3, "Every third move Healer can heal all teammates by 20% from they maxHP")

