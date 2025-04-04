import Team
import sqlite3
import UnitClasses


class Shop():
    def __init__(self, init_team, init_gold):
        self.team = init_team
        self.gold = init_gold
        

    def display_menu(self, list, menu_category):
        for i in range(len(list)):
            if menu_category == "item categories":
                print(f"{i}. {list[i][0]}")
            if menu_category == "units":
                print(f"{i}. {list[i][0]}, {list[i][1]} gold")
            if menu_category == "armor":
                pass
            if menu_category == "weapons":
                pass
            if menu_category == "abilities":
                pass

        print(f"{len(list)}. Show your team to analize")
        print(f"{len(list)+1}. Return to previous page")


    def ask_answer(self, list):
        while True:
            answer = input("Choose category -> ")

            try: 
                answer = int(answer)
            except:
                continue

            if answer < 0 or answer > len(list)+1: #if answer in list(range(0,len(data)+1))
                continue
            
            if answer == len(list):
                self.team.team_info()
                continue
            
            return answer

    def check_gold_for_min_units(self):   
        db = sqlite3.connect("Shop_DB.db")
        cursor = db.cursor()

        cursor.execute("SELECT name, price FROM units")
        data = cursor.fetchall()

        min_unit_price = 100000000
        for unit in data:
            if unit[1] < min_unit_price:
                min_unit_price = unit[1]
                min_unit_name = unit[0]
        
        units_to_buy = 5-len(self.team.team)
        min_gold_to_have = min_unit_price * units_to_buy
        
        return min_gold_to_have, min_unit_name, units_to_buy



    def welcome_board(self):
        min_gold_to_have, min_unit_name, units_to_buy = self.check_gold_for_min_units()    

        print(f'''
    --------------------------------------------------
                    WELCOME TO THE SHOP
    --------------------------------------------------       
    You have gold = {self.gold}

    Please, choose you want to do in shop:
    0. See all item categories
    1. Look at your team with all unit's items to analise
    2. Exit from the shop  
    ''')
        
        answer = ""
        while answer not in ["0","1", "2"]:
            answer = input("Choose category -> ")
            
            if answer not in ["0","1","2"]:
                print("Something went wrong. Try again")
                continue
        
            if answer == "0":
                self.item_types()
            if answer == "1":
                self.team.team_info()
                continue
            if answer == "2":
                if units_to_buy > 0 and self.gold > min_gold_to_have :
                    print(f'''You can't leave shop without full team (5 units), 
                          You should buy {units_to_buy}units. Cheapest is {min_unit_name}''')
                    continue
                elif units_to_buy > 0 and self.gold < min_gold_to_have:
                    print("You have no enough money to continue game")
                    return False
                
                return True

            break


    def item_types(self):
        print('''
        -----------------
            Item type
        -----------------
        ''')

        db = sqlite3.connect("Shop_DB.db")
        cursor = db.cursor()
        cursor.execute("SELECT name FROM item_types")
        data = cursor.fetchall()

        self.display_menu(data, "item categories")
        answer = self.ask_answer(data)

        if answer == len(data)+1:
            self.welcome_board()
            return
        else:
            eval(f"self.{data[0][0]}()")

        db.close()


    def units(self):
        if len(self.team.team) > 4:
            print("Your team is already full. Choose another shop")
            self.item_types()
            return

        print(f'''
        -----------------
              Units
        -----------------
        Gold = {self.gold}
        ''')
        db = sqlite3.connect("Shop_DB.db")
        cursor = db.cursor()
        cursor.execute("SELECT name, price FROM units")
        data = cursor.fetchall()

        self.display_menu(data, "units")
        answer = self.ask_answer(data)

        if answer == len(data)+1:
            self.item_types()
            return
        
        name  = data[answer][0]
        price = data[answer][1]
        
       
        if self.gold < price:
            print("You have no enough money.")
# ЗАКІНЧУЄМО ГРУ БО НЕМА ГРОШЕЙ СФОРМУВАТИ КОМАНДУ

        match name:
            case "Knight":
                unit = UnitClasses.Knight()
            case "Archer":
                unit = UnitClasses.Archer()
            case "Healer":
                unit = UnitClasses.Healer()
            case "Catapult":
                unit = UnitClasses.Catapult()
            case "Defender":
                unit = UnitClasses.Defender()
            case "Wizard":
                unit = UnitClasses.Wizard()
        self.team.team.append(unit)
        self.gold -= price

        print(f'''
              You have bought {name} for {price} gold!
              ''')
        db.close()

        if len(self.team.team) == 5:
            self.item_types()
        else:
            self.units()


    def choose_unit(self):
        self.team.team_info()

        unit = None
        while not unit:    
            answer = input("Choose unit to shop ---> ")

            try: 
                answer = int(answer)
            except:
                continue

            if answer < 0 or answer > len(self.team.team)-1 :
                continue
            
            unit = self.team.team[answer]
            return unit


    def choose_item(self, data, unit_id):
        result = []
        for ar in data:
            if ar[1] == "ALL" or ar[1] == unit_id:
                result.append(ar)
        print(result)

        for x in range(len(result)):
            name = result[x][0]
            value = result[x][2]
            price = result[x][3]
            print(f"{x}) {name} - {value} value - {price} gold")

        item = None
        while not item:    
            answer = input("Choose item to buy ---> ")
            try: 
                answer = int(answer)
            except:
                continue

            if answer < 0 or answer > len(result)-1 :
                continue
            
            item = result[answer]
            return item


    def armor(self):
        print(f'''
        -----------------
              Armor
        -----------------
        Gold = {self.gold}
        ''')

        db = sqlite3.connect("Shop_DB.db")
        cursor = db.cursor()
        
        unit = self.choose_unit()
        cursor.execute(f"SELECT id FROM units WHERE name = '{unit.name}'")
        data = cursor.fetchone()
        unit_id = data[0]

        cursor.execute("SELECT name, usable_for_unit, value, price FROM armor")
        data = cursor.fetchall()

        armor = self.choose_item(data, unit_id)
        armor_name = armor[0]
        armor_value = armor[2]
        armor_price = armor[3]

        db.close()

        if self.gold < armor_price:
            print("You have not enough money for this armor")
            self.item_types()
        
        if eval(f"unit.{armor_name.split()[1]}.value") > armor_value:
            print(f"You already have better armor of {armor_name}")
            self.item_types()

        # перевірка, чи наша броня дійсно гірша за ту, яку хочемо купити
        # надягання купленої броні.
        
        self.gold -= armor_price

        if armor_name.split()[1] == "helmet":
            unit.helmet.name  = armor_name
            unit.helmet.value = armor_value
        elif armor_name.split()[1] == "bodyarmor":
            unit.bodyarmor.name  = armor_name
            unit.bodyarmor.value = armor_value
        elif armor_name.split()[1] == "boots":
            unit.boots.name  = armor_name
            unit.boots.value = armor_value
        elif armor_name.split()[1] == "shield":
            unit.shield.name  = armor_name
            unit.shield.value = armor_value

        print(f"You have successfully  bought {armor_name} for {unit.name}")
        print()


    def weapons(self):
        print(f'''
        -----------------
              WEAPONS
        -----------------
        Gold = {self.gold}
        ''')

        db = sqlite3.connect("Shop_DB.db")
        cursor = db.cursor()
        
        unit = self.choose_unit()
        cursor.execute(f"SELECT id FROM units WHERE name = '{unit.name}'")
        data = cursor.fetchone()
        unit_id = data[0]

        cursor.execute(f"SELECT name, usable_for_unit, value, price FROM weapons WHERE usable_for_unit = '{unit_id}'")
        data = cursor.fetchall()

        weapon = self.choose_item(data, unit_id)
        weapon_name = weapon[0]
        weapon_value = weapon[2]
        weapon_price = weapon[3]

        db.close()

        if self.gold < weapon_price:
            print("You have not enough money for this armor")
            self.item_types()
            return
        
        if unit.weapon.value > weapon_value:
            print(f"You already have better weapon of {weapon_name}")
            self.item_types()
            return

        self.gold -= weapon_price
        unit.weapon.name = weapon_name
        unit.weapon.value = weapon_value

        print(f"You have successfully  bought {weapon_name} for {unit.name}")
        print()


    def abilities(self):
        print(f'''
        -----------------
            ABILITIES
        -----------------
        Gold = {self.gold}
        ''')

        db = sqlite3.connect("Shop_DB.db")
        cursor = db.cursor()
        
        unit = self.choose_unit()
        cursor.execute(f"SELECT id FROM units WHERE name = '{unit.name}'")
        data = cursor.fetchone()
        unit_id = data[0]

        cursor.execute(f"SELECT name, usable_for_unit, value, price FROM abilities WHERE usable_for_unit = '{unit_id}'")
        data = cursor.fetchall()

        ability = self.choose_item(data, unit_id)
        ability_name = ability[0]
        ability_value = ability[2]
        ability_price = ability[3]

        db.close()

        if self.gold < ability_price:
            print("You have not enough money for this ability")
            self.item_types()
            return

        if unit.ability.value > ability_value:
            print(f"You already have better ability of {ability_name}")
            self.item_types()
            return

        self.gold -= ability_price
        unit.ability.value = ability_value

        print(f"You have successfully  bought {ability_name} for {unit.name}")
        print()