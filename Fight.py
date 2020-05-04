from random import randint
import time
from Warior_Classes import Unit_Barbarian
from Warior_Classes import Unit_Archer

class Fight():
    player_Unit = None
    enemy_Unit = None
    player_team = None
    enemy_team = None

    def __init__(self, player_Unit, enemy_Unit, fight_counter, player_team, enemy_team):
        self.player_Unit = player_Unit
        self.enemy_Unit = enemy_Unit
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.display_start_board(fight_counter)

    def display_start_board(self, fight_counter):
        time.sleep(2)
        print(f'''
                ---------------------------------
                ******** FIGHT #{fight_counter} BOARD ********
                ---------------------------------
                Player          VS          Enemy
                {self.player_Unit.name}                  {self.enemy_Unit.name}
                ''')
        print()
        print("Player unit - ", self.player_Unit.unit_info())
        print("Enemy unit - ", self.enemy_Unit.unit_info())
        print()
        print("LET'S THE FIGT BEGIN")
        print()
        self.attack()


    def attack(self):
        player_hit = self.player_Unit.power_for_fight
        enemy_hit = self.enemy_Unit.power_for_fight
        self.enemy_Unit.health_in_fight -= player_hit
        self.player_Unit.health_in_fight -= enemy_hit

        if self.enemy_Unit.health_in_fight_with_equip < 0 or self.enemy_Unit.health_in_fight_with_equip == 0:
            self.enemy_Unit.health_in_fight = 0
            self.enemy_Unit.helmet_value = 0
            self.enemy_Unit.boots_value = 0
            self.enemy_Unit.shield_value = 0
            self.enemy_Unit.bodyarmor_value = 0

            self.enemy_Unit.power_default = 0
            self.enemy_Unit.weapon_value = 0
            self.enemy_Unit.status = "Dead"

        if self.player_Unit.health_in_fight_with_equip < 0 or self.player_Unit.health_in_fight_with_equip == 0:
            self.player_Unit.health_in_fight = 0
            self.player_Unit.helmet_value = 0
            self.player_Unit.boots_value = 0
            self.player_Unit.shield_value = 0
            self.player_Unit.bodyarmor_value = 0

            self.player_Unit.power_default = 0
            self.player_Unit.weapon_value = 0
            self.player_Unit.status = "Dead"
        self.display_result_board(player_hit, enemy_hit)

    def display_result_board(self, player_hit, enemy_hit):
        print(f'{self.player_Unit.name} hit {self.enemy_Unit.name} by {player_hit} points')
        print(f'{self.enemy_Unit.name} hit {self.player_Unit.name} by {enemy_hit} points')
        print()
        print(f"{self.player_Unit.name} status - {self.player_Unit.status}, health: {self.player_Unit.health_in_fight_with_equip}")
        print(f"{self.enemy_Unit.name} status - {self.enemy_Unit.status}, health: {self.enemy_Unit.health_in_fight_with_equip}")
        print()
        print("-------------------------------")
        print()
        self.check_abilities()

    def check_abilities(self):
        if self.player_Unit.abilyty_recharger_moves == 0:
            print()
            print(f"{self.player_Unit.name} is ready to use SuperHit.")
            while True:
                answer = input("Do you want to use SuperHit? Enter Y/N -->>> ")
                if answer.lower() not in ("y", "n"):
                    print()
                    print("Something went wrong. Let's try again")
                    continue
                elif answer.lower() == "n":
                    break
                else:
                    self.player_Unit.abilyty_recharger_moves = 4
                    self.player_use_abilities()
                    break
        else: self.player_Unit.abilyty_recharger_moves -=1

        if self.enemy_Unit.abilyty_recharger_moves == 0:
            print()
            print(f"{self.enemy_Unit.name} is ready to use SuperHit.")
            self.enemy_Unit.abilyty_recharger_moves = 4
            self.comp_use_abilities()
        else: self.enemy_Unit.abilyty_recharger_moves -=1



    def player_use_abilities(self):
        print()


        if self.player_Unit.name == "Barbarian":
            super_value = self.player_Unit.power_with_equip * self.player_Unit.ability_item_value
            print(f"Everyone unit in {self.enemy_team.name}'s team get extra {super_value} hitpoints")

            for i in self.enemy_team.team:
                if i.status == "Alive":
                    print(f"    {i.name} takes {super_value} damage. Health: {i.health_in_fight_with_equip}-{super_value}", end="")
                    i.health_in_fight -= super_value
                    if i.health_in_fight_with_equip == 0 or i.health_in_fight_with_equip < 0:
                        i.health_in_fight = 0
                        i.helmet_value = 0
                        i.boots_value = 0
                        i.shield_value = 0
                        i.bodyarmor_value = 0
                        i.status = "Dead"
                    print(f", Status: {i.status}")
                else:
                    print(f"    {i.name} is already Dead")

        elif self.player_Unit.name == "Healer":
            print(f"Everyone unit in {self.player_team.name}'s team get healthpoints")
            print()
            for i in self.player_team.team:
                if i.status == "Alive":
                    super_value = i.health_default * self.player_Unit.ability_item_value
                    print(f"    {i.name} takes {super_value} healing points. Health: {i.health_in_fight_with_equip}+{super_value}, Status: {i.status}")
                    i.health_in_fight += super_value
                else:
                    print(f"    {i.name} is already Dead")

        elif self.player_Unit.name == "Knight":
            print(f"Please, choose unit from enemy squad to stun for the next {self.player_Unit.ability_item_value} fights")
            for x,i in enumerate(self.enemy_team.team):
                if i.status == "Alive":
                    print(f"{x + 1}. {i.name}, Health: {i.health_in_fight_with_equip}, Power: {i.power_with_equip}, Status: {i.status}")

            while True:
                print()
                answer = input(f"Please choose the number of enemy's unit -->")

                try:
                    int(answer)
                except:
                    print()
                    print("Something went wrong. Let's try again")
                    print()
                    continue
                else:
                    answer = int(answer)

                if answer not in range(1, len(self.player_team.team) + 1):
                    print()
                    print("Something went wrong. Let's try again------------------")
                    print()
                    continue

                self.enemy_team.team[answer - 1].stuned += self.player_Unit.ability_item_value
                print(f"{self.enemy_team.team[answer - 1].name} is stunned for the next {self.player_Unit.ability_item_value} fights")
                break

        elif self.player_Unit.name == "Magician":
            print(f"Everyone unit in {self.enemy_team.name}'s team get poisoned")

            for i in self.enemy_team.team:
                if i.status == "Alive":
                    super_value = i.health_default * self.player_Unit.ability_item_value
                    print(f"    {i.name} takes {super_value} damage. Health: {i.health_in_fight_with_equip}-{super_value}", end="")
                    i.health_in_fight -= super_value
                    if i.health_in_fight_with_equip == 0 or i.health_in_fight_with_equip < 0:
                        i.health_in_fight = 0
                        i.helmet_value = 0
                        i.boots_value = 0
                        i.shield_value = 0
                        i.bodyarmor_value = 0
                        i.status = "Dead"
                    print(f", Status: {i.status}")

                else:
                    print(f"    {i.name} is already Dead")

        elif self.player_Unit.name == "Archer":
            print(
                f"Please, choose unit from enemy squad to make tripple hit.")
            for x, i in enumerate(self.enemy_team.team):
                if i.status == "Alive":
                    print(f"{x + 1}. {i.name}, Health: {i.health_in_fight_with_equip}, Power: {i.power_with_equip}, Status: {i.status}")

            while True:
                print()
                answer = input(f"Please choose the number of enemy's unit -->")

                try:
                    int(answer)
                except:
                    print()
                    print("Something went wrong. Let's try again")
                    print()
                    continue
                else:
                    answer = int(answer)

                if answer not in range(1, len(self.player_team.team) + 1):
                    print()
                    print("Something went wrong. Let's try again------------------")
                    print()
                    continue

                super_value = self.player_Unit.ability_item_value * self.player_Unit.power_with_equip
                print(f"    {self.enemy_team.team[answer-1].name} takes {super_value}+{super_value}+{super_value} damage. Health: {self.enemy_team.team[answer-1].health_in_fight_with_equip}-{super_value * 3}", end="")
                self.enemy_team.team[answer-1].health_in_fight -= super_value * 3
                if self.enemy_team.team[answer-1].health_in_fight_with_equip == 0 or self.enemy_team.team[answer-1].health_in_fight_with_equip < 0:
                    self.enemy_team.team[answer-1].health_in_fight = 0
                    self.enemy_team.team[answer-1].helmet_value = 0
                    self.enemy_team.team[answer-1].boots_value = 0
                    self.enemy_team.team[answer-1].shield_value = 0
                    self.enemy_team.team[answer-1].bodyarmor_value = 0

                    self.enemy_team.team[answer-1].status = "Dead"
                print(f", Status: {self.enemy_team.team[answer-1].status}")

                break


    def comp_use_abilities(self):
        print()

        if self.enemy_Unit.name == "Barbarian":
            super_value = self.enemy_Unit.power_with_equip * self.enemy_Unit.ability_item_value
            print(f"Everyone unit in {self.player_team.name}'s team get {super_value} hitpoints")

            for i in self.player_team.team:
                if i.status == "Alive":
                    print(f"    {i.name} takes {super_value} damage. Health: {i.health_in_fight_with_equip}-{super_value}", end="")
                    i.health_in_fight -= super_value
                    if i.health_in_fight_with_equip == 0 or i.health_in_fight_with_equip < 0:
                        i.health_in_fight = 0
                        i.helmet_value = 0
                        i.boots_value = 0
                        i.shield_value = 0
                        i.bodyarmor_value = 0
                        i.status = "Dead"
                    print(f", Status: {i.status}")
                else:
                    print(f"    {i.name} is already Dead")

        elif self.enemy_Unit.name == "Healer":
            print(f"Everyone unit in {self.enemy_team.name}'s team get healthpoints")
            print()
            for i in self.enemy_team.team:
                if i.status == "Alive":
                    super_value = i.health_default * self.enemy_Unit.ability_item_value
                    print(
                        f"    {i.name} takes {super_value} healing points. Health: {i.health_in_fight_with_equip}+{super_value}, Status: {i.status}")
                    i.health_in_fight += super_value
                else:
                    print(f"    {i.name} is already Dead")

        elif self.enemy_Unit.name == "Knight":
            while True:
                rand = randint(0, len(self.player_team.team))
                if self.player_team.team[rand].status == "Alive":
                    self.player_team.team[rand].stuned += self.enemy_Unit.ability_item_value
                    break

            print(f"    {self.enemy_team.name} is choosing {self.player_team.team[rand]} unit to stun for the next {self.enemy_Unit.ability_item_value} fights")


        elif self.enemy_Unit.name == "Magician":
            print(f"Everyone unit in {self.player_team.name}'s team get poisoned")

            for i in self.player_team.team:
                if i.status == "Alive":
                    super_value = i.health_default * self.enemy_Unit.ability_item_value
                    print(f"    {i.name} takes {super_value} damage. Health: {i.health_in_fight_with_equip}-{super_value}", end="")
                    i.health_in_fight -= super_value
                    if i.health_in_fight_with_equip == 0 or i.health_in_fight_with_equip < 0:
                        i.health_in_fight = 0
                        i.helmet_value = 0
                        i.boots_value = 0
                        i.shield_value = 0
                        i.bodyarmor_value = 0
                        i.status = "Dead"
                    print(f", Status: {i.status}")

                else:
                    print(f"    {i.name} is already Dead")

        elif self.enemy_Unit.name == "Archer":
            super_value = self.enemy_Unit.ability_item_value * self.enemy_Unit.power_with_equip

            while True:
                rand = randint(0, len(self.player_team.team))
                if self.player_team.team[rand].status == "Alive":
                    unit_for_hit = self.player_team.team[rand]
                    print(f"    {unit_for_hit.name} takes {super_value}+{super_value}+{super_value} damage. Health: {unit_for_hit.health_in_fight_with_equip}-{super_value}", end="")
                    break

            unit_for_hit.health_in_fight -= super_value * 3

            if unit_for_hit.health_in_fight_with_equip == 0 or unit_for_hit.health_in_fight_with_equip < 0:
                unit_for_hit.health = 0
                unit_for_hit.helmet_value = 0
                unit_for_hit.boots_value = 0
                unit_for_hit.shield_value = 0
                unit_for_hit.bodyarmor_value = 0
                unit_for_hit.status = "Dead"
            print(f", Status: {unit_for_hit.status}")





# player_unit = Unit_Barbarian()
# enemy_unit = Unit_Archer()
#
# fight = Fight(player_unit, enemy_unit, 1)