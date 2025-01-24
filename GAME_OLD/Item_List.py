class Item():
    def __init__(self, item_class, item_type, item_material, item_value, item_price, item_for_unit):
        self.item_class = item_class
        #FIXME: etc....

class Item_List():
    leather_hemlet_obj = Item(**{"item_class": "ARMOR","item_type": "Helmet","item_material": "Leather helmet","item_value": 100,"item_price": 200,"item_for_unit": "All"})
    leather_helmet = {"item_class": "ARMOR","item_type": "Helmet","item_material": "Leather helmet","item_value": 100,"item_price": 200,"item_for_unit": "All"}
    wooden_helmet = {"item_class": "ARMOR","item_type": "Helmet","item_material": "Wooden helmet","item_value": 200,"item_price": 400,"item_for_unit": "All"}
    iron_helmet = {"item_class": "ARMOR","item_type": "Helmet","item_material": "Iron helmet","item_value": 300,"item_price": 600,"item_for_unit": "All"}
    golden_helmet = {"item_class": "ARMOR","item_type": "Helmet","item_material": "Golden helmet","item_value": 400,"item_price": 800,"item_for_unit": "All"}
    platinum_helmet= {"item_class": "ARMOR","item_type": "Helmet","item_material": "Platinum helmet","item_value": 500,"item_price": 1000,"item_for_unit": "All"}

    helmets = {"Leather helmet": leather_helmet, "Wooden helmet": wooden_helmet, "Iron helmet": iron_helmet, "Golden helmet": golden_helmet, "Platinum helmet": platinum_helmet}



    leather_boots = {"item_class": "ARMOR","item_type": "Boots","item_material": "Leather boots","item_value": 100,"item_price": 200,"item_for_unit": "All"}
    wooden_boots= {"item_class": "ARMOR","item_type": "Boots","item_material": "Wooden boots","item_value": 200,"item_price": 400,"item_for_unit": "All"}
    iron_boots= {"item_class": "ARMOR","item_type": "Boots","item_material": "Iron boots","item_value": 300,"item_price": 600,"item_for_unit": "All"}
    golden_boots= {"item_class": "ARMOR","item_type": "Boots","item_material": "Golden boots","item_value": 400,"item_price": 800,"item_for_unit": "All"}
    platinum_boots= {"item_class": "ARMOR","item_type": "Boots","item_material": "Platinum boots","item_value": 500,"item_price": 1000,"item_for_unit": "All"}

    boots = {"Leather boots": leather_boots, "Wooden boots": wooden_boots, "Iron boots": iron_boots, "Golden boots": golden_boots, "Platinum boots": platinum_boots}



    leather_shield = {"item_class": "ARMOR","item_type": "Shield","item_material": "Leather shield","item_value": 100,"item_price": 200,"item_for_unit": "All"}
    wooden_shield= {"item_class": "ARMOR","item_type": "Shield","item_material": "Wooden shield","item_value": 200,"item_price": 400,"item_for_unit": "All"}
    iron_shield= {"item_class": "ARMOR","item_type": "Shield","item_material": "Iron shield","item_value": 300,"item_price": 600,"item_for_unit": "All"}
    golden_shield= {"item_class": "ARMOR","item_type": "Shield","item_material": "Golden shield","item_value": 400,"item_price": 800,"item_for_unit": "All"}
    platinum_shield= {"item_class": "ARMOR","item_type": "Shield","item_material": "Platinum shield","item_value": 500,"item_price": 1000,"item_for_unit": "All"}

    shields = {"Leather shield": leather_shield, "Wooden shield": wooden_shield, "Iron shield": iron_shield, "Golden shield": golden_shield, "Platinum shield": platinum_shield}



    leather_bodyarmor = {"item_class": "ARMOR","item_type": "Bodyarmor","item_material": "Leather bodyarmor","item_value": 100,"item_price": 200,"item_for_unit": "All"}
    wooden_bodyarmor= {"item_class": "ARMOR","item_type": "Bodyarmor","item_material": "Wooden bodyarmor","item_value": 200,"item_price": 200,"item_for_unit": "All"}
    iron_bodyarmor= {"item_class": "ARMOR","item_type": "Bodyarmor","item_material": "Iron bodyarmor","item_value": 300,"item_price": 200,"item_for_unit": "All"}
    golden_bodyarmor= {"item_class": "ARMOR","item_type": "Bodyarmor","item_material": "Golden bodyarmor","item_value": 400,"item_price": 200,"item_for_unit": "All"}
    platinum_bodyarmor= {"item_class": "ARMOR","item_type": "Bodyarmor","item_material": "Platinum bodyarmor","item_value": 500,"item_price": 200,"item_for_unit": "All"}

    bodyarmors = {"Leather bodyarmor": leather_bodyarmor, "Wooden bodyarmor": wooden_bodyarmor, "Iron bodyarmor": iron_bodyarmor, "Golden bodyarmor": golden_bodyarmor, "Platinum bodyarmor": platinum_bodyarmor}


    stone_cudgel = {"item_class": "WEAPON","item_type": "Cudgel","item_material":"Stone cudgel","item_value": 200,"item_price": 400,"item_for_unit": "Barbarian"}
    wooden_cudgel = {"item_class": "WEAPON","item_type": "Cudgel","item_material":"Wooden cudgel","item_value": 300,"item_price": 600,"item_for_unit": "Barbarian"}
    iron_cudgel = {"item_class": "WEAPON","item_type": "Cudgel","item_material":"Iron cudgel","item_value": 400,"item_price": 800,"item_for_unit": "Barbarian"}
    golden_cudgel = {"item_class": "WEAPON","item_type": "Cudgel","item_material":"Golden cudgel","item_value": 500,"item_price": 1000,"item_for_unit": "Barbarian"}
    steel_cudgel = {"item_class": "WEAPON","item_type": "Cudgel","item_material":"Steel cudgel","item_value": 600,"item_price": 1200,"item_for_unit": "Barbarian"}

    cudgels = {"Stone cudgel": stone_cudgel, "Wooden cudgel": wooden_cudgel, "Iron cudgel": iron_cudgel, "Golden cudgel": golden_cudgel, "Steel cudgel": steel_cudgel}



    stone_sword = {"item_class": "WEAPON","item_type": "Sword","item_material":"Stone sword","item_value": 200,"item_price": 400,"item_for_unit": "Knight"}
    wooden_sword = {"item_class": "WEAPON","item_type": "Sword","item_material":"Wooden sword","item_value": 300,"item_price": 600,"item_for_unit": "Knight"}
    iron_sword = {"item_class": "WEAPON","item_type": "Sword","item_material":"Iron sword","item_value": 400,"item_price": 800,"item_for_unit": "Knight"}
    golden_sword = {"item_class": "WEAPON","item_type": "Sword","item_material":"Golden sword","item_value": 500,"item_price": 1000,"item_for_unit": "Knight"}
    steel_sword = {"item_class": "WEAPON","item_type": "Sword","item_material":"Steel sword","item_value": 600,"item_price": 1200,"item_for_unit": "Knight"}

    swords = {"Stone sword": stone_sword, "Wooden sword": wooden_sword, "Iron sword": iron_sword, "Golden sword": golden_sword, "Steel sword": steel_sword}


    magic_stick_1_lvl = {"item_class": "WEAPON","item_type": "Magic stick","item_material":"Magic Stick 1 lvl","item_value": 200,"item_price": 400,"item_for_unit": "Magician"}
    magic_stick_2_lvl = {"item_class": "WEAPON","item_type": "Magic stick","item_material":"Magic Stick 2 lvl","item_value": 300,"item_price": 600,"item_for_unit": "Magician"}
    magic_stick_3_lvl = {"item_class": "WEAPON","item_type": "Magic stick","item_material":"Magic Stick 3 lvl","item_value": 400,"item_price": 800,"item_for_unit": "Magician"}
    magic_stick_4_lvl = {"item_class": "WEAPON","item_type": "Magic stick","item_material":"Magic Stick 4 lvl","item_value": 500,"item_price": 1000,"item_for_unit": "Magician"}
    magic_stick_5_lvl = {"item_class": "WEAPON","item_type": "Magic stick","item_material":"Magic Stick 5 lvl","item_value": 600,"item_price": 1200,"item_for_unit": "Magician"}

    magic_sticks = {"Magic Stick 1 lvl": magic_stick_1_lvl, "Magic Stick 2 lvl": magic_stick_2_lvl, "Magic Stick 3 lvl": magic_stick_3_lvl, "Magic Stick 4 lvl": magic_stick_4_lvl, "Magic Stick 5 lvl": magic_stick_5_lvl}

    knife_1_lvl = {"item_class": "WEAPON", "item_type": "Knife", "item_material": "Knife 1 lvl", "item_value": 200, "item_price": 400, "item_for_unit": "Healer"}
    knife_2_lvl = {"item_class": "WEAPON", "item_type": "Knife", "item_material": "Knife 2 lvl","item_value": 300, "item_price": 600, "item_for_unit": "Healer"}
    knife_3_lvl = {"item_class": "WEAPON", "item_type": "Knife", "item_material": "Knife 3 lvl","item_value": 400, "item_price": 800, "item_for_unit": "Healer"}
    knife_4_lvl = {"item_class": "WEAPON", "item_type": "Knife", "item_material": "Knife 4 lvl","item_value": 500, "item_price": 1000, "item_for_unit": "Healer"}
    knife_5_lvl = {"item_class": "WEAPON", "item_type": "Knife", "item_material": "Knife 5 lvl","item_value": 600, "item_price": 1200, "item_for_unit": "Healer"}

    knifes = {"Knife 1 lvl": knife_1_lvl, "Knife 2 lvl": knife_2_lvl, "Knife 3 lvl": knife_3_lvl, "Knife 4 lvl": knife_4_lvl, "Knife 5 lvl": knife_5_lvl}


    bow_1_lvl = {"item_class": "WEAPON","item_type": "Bow","item_material":"Bow 1 lvl","item_value": 200,"item_price": 400,"item_for_unit": "Archer"}
    bow_2_lvl = {"item_class": "WEAPON","item_type": "Bow","item_material":"Bow 2 lvl","item_value": 300,"item_price": 600,"item_for_unit": "Archer"}
    bow_3_lvl = {"item_class": "WEAPON","item_type": "Bow","item_material":"Bow 3 lvl","item_value": 400,"item_price": 800,"item_for_unit": "Archer"}
    bow_4_lvl = {"item_class": "WEAPON","item_type": "Bow","item_material":"Bow 4 lvl","item_value": 500,"item_price": 1000,"item_for_unit": "Archer"}
    bow_5_lvl = {"item_class": "WEAPON","item_type": "Bow","item_material":"Bow 5 lvl","item_value": 600,"item_price": 1200,"item_for_unit": "Archer"}

    bows = {"Bow 1 lvl": bow_1_lvl, "Bow 2 lvl": bow_2_lvl, "Bow 3 lvl": bow_3_lvl, "Bow 4 lvl": bow_4_lvl, "Bow 5 lvl": bow_5_lvl}


    poison_book_1_lvl = {"item_class": "ABILITIES","item_type": "Poison Book","item_material":"Poison Book 1 lvl","item_value": 0.1,"item_price": 1000,"item_for_unit": "Magician"}
    poison_book_2_lvl = {"item_class": "ABILITIES","item_type": "Poison Book","item_material":"Poison Book 2 lvl","item_value": 0.2,"item_price": 2000,"item_for_unit": "Magician"}
    poison_book_3_lvl = {"item_class": "ABILITIES","item_type": "Poison Book","item_material":"Poison Book 3 lvl","item_value": 0.3,"item_price": 3000,"item_for_unit": "Magician"}

    poison_books = {"Poison Book 1 lvl": poison_book_1_lvl, "Poison Book 2 lvl": poison_book_2_lvl, "Poison Book 3 lvl": poison_book_3_lvl}



    medic_book_1_lvl = {"item_class": "ABILITIES","item_type": "Medic Book","item_material":"Medic Book 1 lvl","item_value": 0.2,"item_price": 1000,"item_for_unit": "Healer"}
    medic_book_2_lvl = {"item_class": "ABILITIES","item_type": "Medic Book","item_material":"Medic Book 2 lvl","item_value": 0.4,"item_price": 2000,"item_for_unit": "Healer"}
    medic_book_3_lvl = {"item_class": "ABILITIES","item_type": "Medic Book","item_material":"Medic Book 3 lvl","item_value": 0.6,"item_price": 3000,"item_for_unit": "Healer"}

    medic_books = {"Medic Book 1 lvl": medic_book_1_lvl, "Medic Book 2 lvl": medic_book_2_lvl, "Medic Book 3 lvl": medic_book_3_lvl}



    fitness_training_1_lvl = {"item_class": "ABILITIES","item_type": "Fitness Training","item_material":"Fitness Training 1 lvl","item_value": 0.1,"item_price": 1000,"item_for_unit": "Barbarian"}
    fitness_training_2_lvl = {"item_class": "ABILITIES","item_type": "Fitness Training","item_material":"Fitness Training 2 lvl","item_value": 0.2,"item_price": 2000,"item_for_unit": "Barbarian"}
    fitness_training_3_lvl = {"item_class": "ABILITIES","item_type": "Fitness Training","item_material":"Fitness Training 3 lvl","item_value": 0.3,"item_price": 3000,"item_for_unit": "Barbarian"}

    fitness_trainings = {"Fitness Training 1 lvl": fitness_training_1_lvl, "Fitness Training 2 lvl": fitness_training_2_lvl, "Fitness Training 3 lvl": fitness_training_3_lvl}



    karate_training_1_lvl = {"item_class": "ABILITIES","item_type": "Karate Training","item_material":"Karate Training 1 lvl","item_value": 2,"item_price": 1000,"item_for_unit": "Knight"}
    karate_training_2_lvl = {"item_class": "ABILITIES","item_type": "Karate Training","item_material":"Karate Training 2 lvl","item_value": 3,"item_price": 2000,"item_for_unit": "Knight"}
    karate_training_3_lvl = {"item_class": "ABILITIES","item_type": "Karate Training","item_material":"Karate Training 3 lvl","item_value": 4,"item_price": 3000,"item_for_unit": "Knight"}

    karate_trainings = {"Karate Training 1 lvl": karate_training_1_lvl, "Karate Training 2 lvl": karate_training_2_lvl, "Karate Training 3 lvl": karate_training_3_lvl}



    bow_dash_1_lvl = {"item_class": "ABILITIES","item_type": "Bow Dash","item_material":"Bow Dash 1 lvl","item_value": 0.4,"item_price": 1000,"item_for_unit": "Archer"}
    bow_dash_2_lvl = {"item_class": "ABILITIES","item_type": "Bow Dash","item_material":"Bow Dash 2 lvl","item_value": 0.6,"item_price": 2000,"item_for_unit": "Archer"}
    bow_dash_3_lvl = {"item_class": "ABILITIES","item_type": "Bow Dash","item_material":"Bow Dash 3 lvl","item_value": 0.8,"item_price": 3000,"item_for_unit": "Archer"}

    bow_dashs = {"Bow Dash 1 lvl": bow_dash_1_lvl, "Bow Dash 2 lvl": bow_dash_2_lvl, "Bow Dash 3 lvl": bow_dash_3_lvl}



    armour = {
        "HELMETS": helmets,
        "BOOTS": boots,
        "SHIELDS": shields,
        "BODY ARMOR": bodyarmors}
    weapon = {
        "CUDGELS": cudgels,
        "SWORDS": swords,
        "STICKS": magic_sticks,
        "Knifes": knifes,
        "BOWS": bows}
    abilities = {
        "POISON BOOKS": poison_books,
        "MEDIC BOOKS": medic_books,
        "Fitness Training": fitness_trainings,
        "Karate Training": karate_trainings,
        "Bow Dash": bow_dashs}


    all_items = {
        "ARMOUR": armour,
        "WEAPON": weapon,
        "ABILITIES": abilities}


    def output_all_items(self):
        for chapter in self.all_items:
            print()
            print(chapter)
            x = self.all_items[chapter]
            for i in x:
                print()
                print(f"    {i}")
                y = x[i]
                for j in y:
                    d=y[j]
                    a = d['item_material']
                    b = d["item_value"]
                    c = d["item_price"]
                    p = d["item_type"]
                    e = d["item_for_unit"]
                    print(f"        {a}, Value: {b}, Price: {c}, For whom: {e}")

    def create_All_items_keys_and_All_items_in_one_dict(self):
        items_keys = []
        items_dict = {}
        for chapter in self.all_items:
            x = self.all_items[chapter]
            for i in x:
                y = x[i]
                for j in y:
                    items_keys.append(y[j]['item_material'])
                    items_dict[j] = y[j]
        return [items_keys, items_dict]







a = Item_List()

