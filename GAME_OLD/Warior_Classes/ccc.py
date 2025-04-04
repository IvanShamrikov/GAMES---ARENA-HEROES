from abc import ABC
import Items

class Unit(ABC):
    name = ""

    attack_default = 0
    attack_with_weapon = property()

    health_default = 0
    health_with_armor = property()
    health_in_fight = 0

    weapon = Items.Weapon()

    helmet = Items.Armor()
    bodyarmor = Items.Armor()
    boots = Items.Armor()
    shield = Items.Armor()

    status = "Alive"
    

    @attack_with_weapon.getter
    def attack_with_weapon(self):
        a = self.attack_default #+ self.weapon
        return a

    @health_with_armor.getter
    def health_with_armor(self):
        h = self.health_default # + self.helmet + self.bodyarmor + self.shield + self.boots
        return h


    def hit(self, enemy):
        enemy.health_in_fight -= self.attack_with_weapon
        if enemy.health_in_fight <= 0:
            enemy.health_in_fight = 0
            enemy.status = "Dead"        
        print(f"{self.name} hit {enemy.name} by {self.attack_with_weapon}")

    def unit_info(self):
        print(f"{self.status} Name: {self.name}, health = {self.health_in_fight}, attack = {self.attack_with_weapon}")