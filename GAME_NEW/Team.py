import random
import UnitClasses

class Team:
    alive_team = property()
    dead_team = property()
    
    def __init__(self, init_name = "NoName", init_team = []):
        self.name = init_name
        self.team = init_team

    @alive_team.getter
    def alive_team(self):
        result = []
        for u in self.team:
            if u.status == "Alive":
                result.append(u)
        return result

    @dead_team.getter
    def dead_team(self):
        result = []
        for u in self.team:
            if u.status == "Dead":
                result.append(u)
        return result

    def choose_unit_by_player(self):
        unit = None

        while not unit:
            x = input("Choose unit index - ")

            try:
                unit = self.team[int(x)]
            except:
                print("On no! Thmth went wrong. Try one more time")

        return unit
    
    def team_info(self, choosing = False):
        print(f'''
        ----------------------
              {self.name}
        ----------------------''')
                

        if len(self.dead_team) == 0 :
            for u in self.alive_team:
                if choosing == True:
                    print(self.alive_team.index(u), end= ")  ")
                u.unit_info()

        elif len(self.alive_team)==0:
            print("ALL UNITS ARE DEAD")
            for u in self.dead_team:
                u.unit_info()
        else:
            print ("ALIVE:")
            for u in self.alive_team:
                if choosing == True:
                    print(self.alive_team.index(u), end= ")  ")
                u.unit_info()
            print()
            print("DEAD:")
            for u in self.dead_team:
                u.unit_info()
            print()
        
    def create_rand_comp_team(self):
        all_names = ["Monster's Squad",
                     "Suicide Squad",
                     "Crocodiles",
                     "Supermen",
                     "WoW wariors",
                     "Aboba team",
                     "SchoolBoyRunAway",
                     "SkibidiToilets",
                     "RikRoll band",
                     "AliBaBa and 40 banditos",
                     "Chinchilla team"]
        self.name = random.choice(all_names)

        all_units = [UnitClasses.Archer,
                     UnitClasses.Catapult,
                     UnitClasses.Defender,
                     UnitClasses.Healer,
                     UnitClasses.Knight,
                     UnitClasses.Wizard]
        for i in range(5):
            self.team.append(random.choice(all_units)())

    def chose_random_unit(self):
        return random.choice(self.alive_team)