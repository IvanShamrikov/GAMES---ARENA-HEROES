import sqlite3

def create_shop():
    db = sqlite3.connect("Shop_DB.db")
    cursor = db.cursor()

    # ----------------- Create item_types ------------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS item_types(
                   id TEXT PRIMARY KEY,
                   name TEXT
                   )''')
    cursor.execute("INSERT INTO item_types VALUES ('it1', 'units')")
    cursor.execute("INSERT INTO item_types VALUES ('it2', 'armor')")
    cursor.execute("INSERT INTO item_types VALUES ('it3', 'weapons')")
    cursor.execute("INSERT INTO item_types VALUES ('it4', 'abilities')")

    # ----------------- Create units ------------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS units(
                   id TEXT PRIMARY KEY,
                   item_type TEXT,
                   name TEXT,
                   price INTEGER
                   )''')
    cursor.execute("INSERT INTO units VALUES ('u1', 'it1', 'Knight', 300)")
    cursor.execute("INSERT INTO units VALUES ('u2', 'it1', 'Healer', 300)")
    cursor.execute("INSERT INTO units VALUES ('u3', 'it1', 'Catapult', 300)")
    cursor.execute("INSERT INTO units VALUES ('u4', 'it1', 'Defender', 300)")
    cursor.execute("INSERT INTO units VALUES ('u5', 'it1', 'Wizard', 300)")
    cursor.execute("INSERT INTO units VALUES ('u6', 'it1', 'Archer', 300)")

     # ----------------- Create armor ------------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS armor(
                   id TEXT PRIMARY KEY,
                   item_type TEXT,
                   name TEXT,
                   usable_for_unit TEXT,
                   value INTEGER,
                   price INTEGER
                   )''')
    
    cursor.execute("INSERT INTO armor VALUES ('ar1', 'it2', 'wooden helmet', 'ALL', 100, 400)")
    cursor.execute("INSERT INTO armor VALUES ('ar2', 'it2', 'iron helmet', 'ALL', 200, 600)")
    cursor.execute("INSERT INTO armor VALUES ('ar3', 'it2', 'golden helmet', 'ALL', 300, 800)")

    cursor.execute("INSERT INTO armor VALUES ('ar4', 'it2', 'wooden bodyarmor', 'ALL', 100, 400)")
    cursor.execute("INSERT INTO armor VALUES ('ar5', 'it2', 'iron bodyarmor', 'ALL', 200, 600)")
    cursor.execute("INSERT INTO armor VALUES ('ar6', 'it2', 'golden bodyarmor', 'ALL', 300, 800)")

    cursor.execute("INSERT INTO armor VALUES ('ar7', 'it2', 'wooden boots', 'ALL', 100, 400)")
    cursor.execute("INSERT INTO armor VALUES ('ar8', 'it2', 'iron boots', 'ALL', 200, 600)")
    cursor.execute("INSERT INTO armor VALUES ('ar9', 'it2', 'golden boots', 'ALL', 300, 800)")

    cursor.execute("INSERT INTO armor VALUES ('ar10', 'it2', 'wooden shield', 'ALL', 100, 400)")
    cursor.execute("INSERT INTO armor VALUES ('ar11', 'it2', 'iron shield', 'ALL', 200, 600)")
    cursor.execute("INSERT INTO armor VALUES ('ar12', 'it2', 'golden shield', 'ALL', 300, 800)")

    

    # ----------------- Create weapons ------------------

    cursor.execute('''CREATE TABLE IF NOT EXISTS weapons(
                   id TEXT PRIMARY KEY,
                   item_type TEXT,
                   name TEXT,
                   usable_for_unit TEXT,
                   value INTEGER,
                   price INTEGER
                   )''')
    
    cursor.execute("INSERT INTO weapons VALUES ('wp1', 'it3', 'wooden sword', 'u1', 100, 800)")
    cursor.execute("INSERT INTO weapons VALUES ('wp2', 'it3', 'iron sword', 'u1', 200, 1200)")
    cursor.execute("INSERT INTO weapons VALUES ('wp3', 'it3', 'golden sword', 'u1', 300, 1600)")

    cursor.execute("INSERT INTO weapons VALUES ('wp4', 'it3', 'wooden knife', 'u2', 100, 800)")
    cursor.execute("INSERT INTO weapons VALUES ('wp5', 'it3', 'iron knife', 'u2', 200, 1200)")
    cursor.execute("INSERT INTO weapons VALUES ('wp6', 'it3', 'golden knife', 'u2', 300, 1600)")

    cursor.execute("INSERT INTO weapons VALUES ('wp7', 'it3', 'stone projectile', 'u3', 100, 800)")
    cursor.execute("INSERT INTO weapons VALUES ('wp8', 'it3', 'iron projectile', 'u3', 200, 1200)")
    cursor.execute("INSERT INTO weapons VALUES ('wp9', 'it3', 'explosive projectile', 'u3', 300, 1600)")

    cursor.execute("INSERT INTO weapons VALUES ('wp10', 'it3', 'wooden morgenstern', 'u4', 100, 800)")
    cursor.execute("INSERT INTO weapons VALUES ('wp11', 'it3', 'iron morgenstern', 'u4', 200, 1200)")
    cursor.execute("INSERT INTO weapons VALUES ('wp12', 'it3', 'gold morgenstern', 'u4', 300, 1600)")

    cursor.execute("INSERT INTO weapons VALUES ('wp13', 'it3', 'wooden baculus', 'u5', 100, 800)")
    cursor.execute("INSERT INTO weapons VALUES ('wp14', 'it3', 'iron baculus', 'u5', 200, 1200)")
    cursor.execute("INSERT INTO weapons VALUES ('wp15', 'it3', 'gold baculus', 'u5', 300, 1600)")

    cursor.execute("INSERT INTO weapons VALUES ('wp16', 'it3', 'wooden arrow', 'u6', 100, 800)")
    cursor.execute("INSERT INTO weapons VALUES ('wp17', 'it3', 'iron arrow', 'u6', 200, 1200)")
    cursor.execute("INSERT INTO weapons VALUES ('wp18', 'it3', 'explosive arrow', 'u6', 300, 1600)")

    # ----------------- Create abilities ------------------

    cursor.execute('''CREATE TABLE IF NOT EXISTS abilities(
                   id TEXT PRIMARY KEY,
                   item_type TEXT,
                   name TEXT,
                   usable_for_unit TEXT,
                   value INTEGER,
                   price INTEGER
                   )''')

    cursor.execute("INSERT INTO abilities VALUES ('ab1', 'it4', 'splash training lvl.1', 'u1', 0.6, 800)")
    cursor.execute("INSERT INTO abilities VALUES ('ab2', 'it4', 'splash training lvl.2', 'u1', 0.7, 1200)")
    cursor.execute("INSERT INTO abilities VALUES ('ab3', 'it4', 'splash training lvl.3', 'u1', 0.8, 1600)")

    cursor.execute("INSERT INTO abilities VALUES ('ab4', 'it4', 'heal training lvl.1', 'u2', 0.3, 800)")
    cursor.execute("INSERT INTO abilities VALUES ('ab5', 'it4', 'heal training lvl.2', 'u2', 0.4, 1200)")
    cursor.execute("INSERT INTO abilities VALUES ('ab6', 'it4', 'heal training lvl.3', 'u2', 0.5, 1600)")

    cursor.execute("INSERT INTO abilities VALUES ('ab7', 'it4', 'catapult training lvl.1', 'u3', 2.2, 800)")
    cursor.execute("INSERT INTO abilities VALUES ('ab8', 'it4', 'catapult training lvl.2', 'u3', 2.3, 1200)")
    cursor.execute("INSERT INTO abilities VALUES ('ab9', 'it4', 'catapult training lvl.3', 'u3', 2.5, 1600)")

    cursor.execute("INSERT INTO abilities VALUES ('ab10', 'it4', 'defender training lvl.1', 'u4', 0.1, 800)")
    cursor.execute("INSERT INTO abilities VALUES ('ab11', 'it4', 'defender training lvl.2', 'u4', 0.2, 1200)")
    cursor.execute("INSERT INTO abilities VALUES ('ab12', 'it4', 'defender training lvl.3', 'u4', 0.3, 1600)")

    cursor.execute("INSERT INTO abilities VALUES ('ab13', 'it4', 'archer training lvl.1', 'u6', 60, 800)")
    cursor.execute("INSERT INTO abilities VALUES ('ab14', 'it4', 'archer training lvl.2', 'u6', 70, 1200)")
    cursor.execute("INSERT INTO abilities VALUES ('ab15', 'it4', 'archer training lvl.3', 'u6', 80, 1600)")


    db.commit()
    db.close()




create_shop()