import abc
from random import random

class Unit(abc.ABC):
    buy_cost = 0
    name = ""
    #NOTE: WHY not use __ private notation for _general_health_default_with_equip and others?
    
    health_default = 0
    _general_health_default_with_equip = 0
    health_in_fight = health_default
    _health_in_fight_with_equip = 0



    power_default = 0
    _power_with_equip = 0
    _power_for_fight = 0

    status = None
    level = 0
    experiance = 0
    abilyty_recharger_moves = 0 #Сколько ходов до перезерядки способности(ходов объекта)
    poison_longness = 2       #Длительность заклятия (любых ходов команды enemy)
    chance_critical_hit = 0    #Шанс критической атаки (+30% от Power). Разный у каждого типа персонажей.
    stuned = 0
    super = ""
    #FIXME: Add item class to your code helmet_name should not be a property of Unit this stands for all equipment not only hemlet
    helmet_name = "Helmet"
    helmet_value = 0

    boots_name = "Boots"
    boots_value = 0

    shield_name = "Shield"
    shield_value = 0

    bodyarmor_name = "Bodyarmor"
    bodyarmor_value = 0

    weapon_name = "Hands"
    weapon_value = 0

    ability_item_name = "Ability item"
    ability_item_value = 0




    def get_general_health_default_with_equip(self):
        general_health_default_with_equip = self.health_default + self.helmet_value + self.boots_value + self.shield_value + self.bodyarmor_value
        return general_health_default_with_equip

    def set_general_health_default_with_equip(self, health):
        self._general_health_default_with_equip = health

    def get_health_in_fight_with_equip(self):
        health_in_fight_with_equip = self.health_in_fight + self.helmet_value + self.boots_value + self.shield_value + self.bodyarmor_value
        return health_in_fight_with_equip

    def set_health_in_fight_with_equip(self, health):
        _health_in_fight_with_equip = health




    def get_power_with_equip(self):
        self._power_with_equip = self.power_default + self.weapon_value
        return self._power_with_equip

    def set_power_with_equip(self, power):
        self._power_with_equip = power


    def get_power_for_fight(self):
        rand = random()

        if self.stuned > 0:#FIXME: stuned must be boolean type or rename it stuned_for_seconds
            power_for_fight = 0
            print(f"{self.name} is stuned for this fight.")
            self.stuned -= 1
        elif rand < self.chance_critical_hit:
            power_for_fight = self.power_with_equip * 2
            print(f"{self.name} makes critical 2power hit.")
        else:
            power_for_fight = self.power_with_equip

        return power_for_fight

    def set_power_for_fight(self, power):
        self._power_for_fight = power




    #FIXME: consider using @property decorators https://docs.python.org/3/library/functions.html?highlight=property#property
    power_with_equip = property(get_power_with_equip, set_power_with_equip)
    power_for_fight = property (get_power_for_fight, set_power_for_fight)

    general_health_default_with_equip = property(get_general_health_default_with_equip, set_general_health_default_with_equip)
    health_in_fight_with_equip = property(get_health_in_fight_with_equip, set_health_in_fight_with_equip)







  
    def __init__(self,**kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


    def unit_info(self):
        unit_info = f"{self.name}, Status: {self.status}, Health: {int(self.health_in_fight_with_equip)}, Power: {self.power_with_equip}, Ability recharge: {self.abilyty_recharger_moves}"
        return unit_info








