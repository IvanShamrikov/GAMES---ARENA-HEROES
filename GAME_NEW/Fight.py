

class Fight():
    def __init__(self, init_player_unit, init_comp_unit, init_fight_counter):
        self.player_unit = init_player_unit
        self.comp_unit = init_comp_unit
        self.fight_counter = init_fight_counter

    def fight_start(self):
        self.display_start_board()
        self.hitmaker()
        self.display_final_board()
        

    def display_start_board(self):
        print(f'''
    ---------------------------------
    ******** FIGHT #{self.fight_counter} BOARD ********
    ---------------------------------
    Player                   Computer
    {self.player_unit.name}                     {self.comp_unit.name}

    LET'S THE FIGHT BEGIN!
''')
    
    def hitmaker(self):
        self.player_unit.hit(self.comp_unit)
        self.comp_unit.hit(self.player_unit)
        
    def display_final_board(self):
        print()
        self.player_unit.unit_info()
        self.comp_unit.unit_info()
        print("-----------------------------------")