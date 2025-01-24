from random import choice
from random import randrange
import Warior_Classes

class Team():
    name = ""
    team = []
    alive_team = []
    dead_team_for_arena = []

    def __init__(self, team, name):
        self.team = team
        self.name = name

    def team_info(self):
        for x, i in enumerate(self.team):
            print(x+1, ". ", i.unit_info())


    def create_random_team(self):
        name_lst = ["Monster's squad", "Crocodiles", "Supermen", "WoW wariors", "BlaBla squad", "Pink ponys"]
        rand = randrange(0, 6)
        self.name = name_lst[rand]

        while len(self.team) != 5:
            rand = randrange(1, 6)
            if rand == 1:
                self.team.append(Warior_Classes.Unit_Barbarian())
            elif rand == 2:
                self.team.append(Warior_Classes.Unit_Archer())
            elif rand == 3:
                self.team.append(Warior_Classes.Unit_Magician())
            elif rand == 4:
                self.team.append(Warior_Classes.Unit_Knight())
            elif rand == 5:
                self.team.append(Warior_Classes.Unit_Healer())




    def check_alive_units(self):
        for i in self.team:
            if i.status == "Alive":
                return True
        return False


    def choose_unit_by_player(self):
        self.team_info()
        while True:
            print()
            answer = input("Choose unit to the fight. Enter number of unit ---> ")
            if len(answer) != 1:
                print("Please, choose the number of unit.")
                continue
            elif True:
                try:
                    int(answer)
                except:
                    print("Please, enter a NUMBER.")
                    continue
                else:
                    answer = int(answer)

            if answer > len(self.team):
                print("Please, enter CORRECT number.")
                continue
            else:
                unit = self.team[answer - 1]

            if unit.status == "Dead":
                print("Please, enter a number of ALIVE player.")
                continue
            else:
                return unit


    def make_alive_team(self):
        self.alive_team = []
        for i in self.team:
            if i.status == "Alive":
                self.alive_team.append(i)
        else: return self.alive_team


    def dead_team_in_arena(self):
        dead_team_in_arena = []
        for i in self.team:
            if i.status == "Dead":
                dead_team_in_arena.append(i)
        return dead_team_in_arena


    def choose_unit_by_comp(self):
        self.team_info()
        print()
        self.alive_team = self.make_alive_team()
        unit = choice(self.alive_team)
        return unit


