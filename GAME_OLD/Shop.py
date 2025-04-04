import time
import Team
import Warior_Classes
import Item_List


class Shop():
    player_gold = 0
    player_team = []
    item_list = Item_List.Item_List()
    shop_units = None

    def __init__(self, player_gold, player_team):
        self.player_gold = player_gold
        self.player_team = player_team
        # self.units_shopping()
        # self.items_shopping()



    def units_shopping(self):

        while True:
            print()
            time.sleep(2)
            print(f'''
        ------------------------------------------
                WELCOME TO THE UNIT SHOP
        ------------------------------------------

        You should buy some units for the battles.
        You must have 5 units.
        Now you have {len(self.player_team.team)} units and {self.player_gold} gold''')
            print()
            print()
            answer = input('''Please, choose, what do you like to do in the unit shop:
    1. Show all units and prices.
    2. Show your team with all unit's skills to analize.
    3. Exit from the unit shop.
Input the number here ---> ''')

            if answer == "1":
                    self.show_unit_shop()
            elif answer == "2":
                self.show_team_skills()
            elif answer == "3":
                if len(self.player_team.team) < 5:
                    print()
                    print()
                    print("Please, you shoud have 5 units in yoyr squad. Please, buy some units.")
                    continue
            else:
                print()
                print("Something went wrong. Let's try again")
                print()
                continue

            break

    def show_unit_shop(self):
        time.sleep(2)
        print(f'''
                ---------------------------
                        UNITS SHOP
                ---------------------------
                   You have {self.player_gold} of gold.''')
        barbarian = Warior_Classes.Unit_Barbarian()
        archer = Warior_Classes.Unit_Archer()
        healer = Warior_Classes.Unit_Healer()
        knight = Warior_Classes.Unit_Knight()
        magician = Warior_Classes.Unit_Magician()

        self.shop_units = {"Barbarian": barbarian, "Archer": archer, "Healer": healer, "Knight": knight, "Magician": magician}
        print()
        for i in self.shop_units:
            print(
                f"{i} --> Price: {self.shop_units[i].buy_cost} -->  Health: {self.shop_units[i].health_default}, Power: {self.shop_units[i].power_default}, Critical Hit: {int(self.shop_units[i].chance_critical_hit *100)}%, Super: {self.shop_units[i].super}")
        print()
        print()

        while True:

            print()
            answer = input('''Please, choose, what do you like to do next.
    1. Buy some unit.
    2. Exit to the main page of the unit shop.
Input the number here ---> ''')
            if answer != "1" and answer != "2":
                print()
                print("Something went wrong. Let's try again")
                print()
                continue
            elif answer == "1":
                self.buy_unit()
                break
            elif answer == "2":
                self.units_shopping()
                break


    def show_team_skills (self):
        time.sleep(2)
        print('''
        ---------------------------
              PLAYER'S UNITS
        ---------------------------''')

        print()
        if len(self.player_team.team) != 0:
            for i in self.player_team.team:
                print(f"{i.name} --> Health: {i.general_health_default_with_equip} | Power: {i.power_with_equip} | Level: {i.level} | Moves till super recharge: {i.abilyty_recharger_moves} | Critical Hit: {int(i.chance_critical_hit * 100)}% | Super: {i.super}")
        else: print("Sorry, but you don't have any units in your squad")
        print()
        while True:
            print(f"You have {self.player_gold} of gold.")
            print()
            answer = input('''Please, choose, what do you like to do next.
    1. Go to unit shop to buy some unit.
    2. Exit to the main page of the unit shop.
Input the number here ---> ''')
            if answer != "1" and answer != "2":
                print()
                print("Something went wrong. Let's try again")
                print()
                continue
            elif answer == "1":
                self.show_unit_shop()
                break
            elif answer == "2":
                self.units_shopping()
                break


    def buy_unit(self):
        while True:
            print()
            unit_key = input('''Please, type here name (Barbarian/Archer/Knight/Healer/Magician) of unit to buy --->>> ''')
            if unit_key.lower() not in ("barbarian", "archer", "knight", "healer", "magician"):
                print()
                print("Something went wrong. Let's try again")
                print()
                continue
            else:
                if self.player_gold < self.shop_units[unit_key].buy_cost:
                    print()
                    print("Sorry, but you have not enough gold. Choose another unit.")
                    print()
                    self.show_unit_shop()
                    break

                else:
                    bought_unit = self.shop_units[unit_key]
                    self.player_team.team.append(bought_unit)
                    self.player_gold -= self.shop_units[unit_key].buy_cost

                    print()
                    print(f"You have bought {bought_unit.name} for {self.shop_units[unit_key].buy_cost} gold")
                    print()

                    if len(self.player_team.team) == 5:
                        print("**********************************************************")
                        print("You have enough units in your squad. Let's go to ITEM SHOP")
                        print("**********************************************************")
                        self.items_shopping()
                    else:
                        self.show_unit_shop()
                    break





    def items_shopping(self):
        time.sleep(2)
        print('''
                ------------------------------------------
                         WELCOME TO THE ITEM SHOP
                ------------------------------------------
                ''')

        while True:
            print()
            answer = input('''Please, choose, what do you like to do in the item shop:
    1. Show all items and prices.
    2. Show your team with all unit's items to analize.
    3. Exit from the item shop.
Input the number here ---> ''')

            if answer == "1":
                self.show_item_shop()
                break
            elif answer == "2":
                self.show_team_items()
                break
            elif answer == "3":
                print()
                print("See you next time, by-by!")
                print()
                break
            else:
                print()
                print("Something went wrong. Let's try again")
                print()
                continue



    def show_item_shop(self):
        time.sleep(2)
        print('''
        ---------------------------
                   ITEMS
        ---------------------------
        ''')
        self.item_list.output_all_items()
        print()
        print()


        while True:
            print(f"You have {self.player_gold} of gold.")
            print()
            answer = input('''Please, choose, what do you like to do next.
    1. Buy some item.
    2. Exit to the main page of the item shop.
Input the number here ---> ''')
            if answer != "1" and answer != "2":
                print()
                print("Something went wrong. Let's try again")
                print()
            elif answer == "1":
                self.buy_items()
                break
            elif answer == "2":
                self.items_shopping()
                break

    def buy_items(self):
        items_keys, items_dict = self.item_list.create_All_items_keys_and_All_items_in_one_dict()

        while True:
            print()
            item_key = input("Please, type here item you want to buy. For exsample: Wooden Sword / Karate Practice 3 lvl / Magic Stick 4 lvl/ Iron bodyarmor --->>> ")
            if item_key not in items_keys:
                print()
                print("Something went wrong. Let's try again")
                print()
                continue

            if self.player_gold < items_dict[item_key]["item_price"]:
                print()
                print("Sorry, but you have not enough gold. Choose another item.")
                print()
                continue

            bought_item = items_dict[item_key]
            bought_item_name = item_key


            while True:
                print()
                print("You need choose to whom you will give that item:")
                print()

                for x, i in enumerate(self.player_team.team):
                    print(f"{x + 1}. {i.name} (Healts: {i.health_default} , Power: {i.power_default}    --->  {i.helmet_name}: {i.helmet_value}, {i.shield_name}: {i.shield_value}, {i.boots_name}: {i.boots_value}, {i.bodyarmor_name} : {i.bodyarmor_value}, {i.weapon_name}: {i.weapon_value}, {i.ability_item_name}:{i.ability_item_value}")

                print()
                answer = input("Please choose the number of unit to give him that item or enter 0 to choose new item --->")

                try:
                    int(answer)
                except:
                    print()
                    print("Something went wrong. Let's try again")
                    print()
                    continue
                else: answer = int(answer)
                if answer == 0:
                    self.show_item_shop()
                    break
                elif answer not in range(1, len(self.player_team.team)+1):
                    print()
                    print("Something went wrong. Let's try again------------------")
                    print()
                    continue


                unit = self.player_team.team[answer-1]

                #БЛОК ПРОВЕРКИ СОВМЕСТИМОСТИ ОРУЖИЯ И ПЕРСОНАЖА

                if bought_item["item_for_unit"] == unit.name or bought_item["item_for_unit"] == "All":
                    self.give_item_to_unit(bought_item, unit)
                else:
                    print()
                    print(f"Item {bought_item_name} is not for {unit.name}. Please, choose another unit to give him {bought_item_name}")
                    print()
                    continue
                break
            break


    def give_item_to_unit(self, item, unit):
        if item["item_class"] == "WEAPON":
            unit.weapon_name = item["item_material"]
            unit.weapon_value = item["item_value"]
        elif item["item_class"] == "ARMOUR":
            if item["item_type"] == "Helmet":
                unit.helmet_name = item["item_material"]
                unit.helmet_value = item["item_value"]
            if item["item_type"] == "Boots":
                unit.boots_name = item["item_material"]
                unit.boots_value = item["item_value"]
            if item["item_type"] == "Shields":
                unit.shield_name = item["item_material"]
                unit.shield_value = item["item_value"]
            if item["item_type"] == "Bodyarmor":
                unit.bodyarmor_name = item["item_material"]
                unit.bodyarmor_value = item["item_value"]
        elif item["item_class"] == "ABILITIES":
            unit.ability_item_name = item["item_material"]
            unit.ability_item_value = item["item_value"]

        self.player_gold -= item["item_price"]
        a = item["item_price"]
        b= item["item_material"]

        print()
        print(f"You have bought {b} for {a} gold")
        print()

        self.items_shopping()
        return None




    def show_team_items(self):
        time.sleep(2)
        print(f'''
        ---------------------------
                PLAYER'S ITEMS
        ---------------------------
        You have {self.player_gold} of gold''')

        print()
        if len(self.player_team.team) != 0:
            print()

            for i in self.player_team.team:
                print(f"{i.name} (Healts: {i.health_default} + {i.general_health_default_with_equip - i.health_default}, Power: {i.power_default} + {i.power_with_equip - i.power_default}) ---> {i.helmet_name}: {i.helmet_value} | {i.shield_name}: {i.shield_value} | {i.boots_name}: {i.boots_value} | {i.bodyarmor_name}: {i.bodyarmor_value} | {i.weapon_name}: {i.weapon_value} | {i.ability_item_name}: {i.ability_item_value}")
        else:
            print("Sorry, but you don't have any units in your squad")

        print()
        while True:
            print()
            answer = input('''Please, choose, what do you like to do next.
            1. Go to the item shop.
            2. Exit to the main page of the item shop.
Input the number here ---> ''')
            if answer != "1" and answer != "2":
                print()
                print("Something went wrong. Let's try again")
                print()
                continue
            elif answer == "1":
                self.show_item_shop()
                break
            elif answer == "2":
                self.items_shopping()
                break




g = 0
t = Team.Team([], "aaa")
a=Shop(g,t)