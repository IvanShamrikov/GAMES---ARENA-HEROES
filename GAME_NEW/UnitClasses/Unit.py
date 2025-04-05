from .Items import Abilities
from .Items import Weapon
from .Items import Armor
from abc import ABC



# def check_shield(func):
#     def wrapper(self, enemy):
#         if enemy.magic_shield:
#             print(f"{enemy.name} has a magic shield! No damage taken.")
#             enemy.magic_shield = False
#         else:
#             return func(self, enemy)
#     return wrapper


class Unit(ABC):
    name = ""
    ability = None

    attack_default = 0
    attack_with_weapon = property()

    health_default = 0
    health_with_armor = property()
    health_in_fight = 0

    weapon = Weapon()

    helmet = Armor()
    bodyarmor = Armor()
    boots = Armor()
    shield = Armor()

    status = "Alive"

    magic_shield = True
    stunned = True
    poisoned_moves = 3
    poisoned_damage = 50


    @attack_with_weapon.getter
    def attack_with_weapon(self):
        a = self.attack_default + self.weapon.value
        return a

    @health_with_armor.getter
    def health_with_armor(self):
        h = self.health_default + self.helmet.value + self.bodyarmor.value + self.shield.value + self.boots.value
        return h


    @staticmethod
    def check_effects(func):
        def wrapper(self, enemy):
            if self.poisoned_moves > 0:
                print(f"{self.name} is poisoned for {self.poisoned_moves} moves and gets {self.poisoned_damage} damage")
                self.health_in_fight -= self.poisoned_damage
                self.poisoned_moves -=1

            if self.stunned == True:
                print(f"{self.name} is stuned for this move and can't hit enemy")
                self.stunned == False
                return

            if enemy.magic_shield == True:
                print(f"{enemy.name} has a magic shield! No damage taken.")
                enemy.magic_shield = False
                return

            return func(self, enemy)
        return wrapper


    # @staticmethod
    # def check_abilities(func):
    #     def wrapper(self, enemy):
    #         if self.ability.cooldown > 0:
    #             self.ability.cooldown -= 1
    #         else:
    #
    #
    #
    #         return func(self, enemy)
    #     return wrapper

    @check_effects
    def hit(self, enemy):
        enemy.health_in_fight -= self.attack_with_weapon
        if enemy.health_in_fight <= 0:
            enemy.health_in_fight = 0
            enemy.status = "Dead"   
        print(f"{self.name} hit {enemy.name} by {self.attack_with_weapon}")
    

    def unit_info(self):
        print(f"{self.status} Name: {self.name}, health = {self.health_in_fight}, attack = {self.attack_with_weapon}")



        # Catapult = Abilities("SuperAttack", 2, 4, "Catapult hits x damage to the chosen enemy unit. ")
        # Healer = Abilities("SuperHeal", 20, 3, "Every third move Healer can heal all teammates by 20% from they maxHP")
        # Knight = Abilities("SplashAttack", 50, 4, "Knight can splash all enemy units at % power")

        # Wizard = Abilities("SuperStune", 1, 4, "Wizard can stun all enemy units for next fight")
        # Defender = Abilities("Shield", 1, 4,"Defender create shield for all teammates for the next hit and reflect some damage.")
        # Archer = Abilities("PoisonedArrow", 50, 3, "Archer does 50 damage to 1 enemy unit for the next 2 fights")
