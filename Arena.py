import Fight
import Team
import time
from Warior_Classes import Unit_Barbarian
from Warior_Classes import Unit_Archer


class Arena():
    player_team = None
    enemy_team = None
    fight_counter = 0
    counter_arena = 0
    alive_player_team = []
    dead_player_team = []
    winner = None

    def __init__(self, player_team, counter_arena):
        self.player_team = player_team
        self.counter_arena = counter_arena
        self.create_enemy_team()


    def create_enemy_team(self):
        self.enemy_team = Team.Team(team= [], name= "")
        self.enemy_team.create_random_team()
        self.display_arena_board()

    def display_arena_board(self):
        time.sleep(2)
        print(f'''
            ------------------------------------------------------------
                        ******** ARENA #{self.counter_arena} BOARD ********
            ------------------------------------------------------------
                                Welcome to the Arena!
            {self.player_team.name}                VS                  {self.enemy_team.name}
                                                 
        ''')
        print()
        print()
        print("PLAYER TEAM")
        self.player_team.team_info()

        print()
        print()
        print("ENEMY TEAM")
        self.enemy_team.team_info()

        self.arena_fight()

    def arena_fight(self):
        self.fight_counter = 1
        x = 0

        while self.player_team.check_alive_units() and self.enemy_team.check_alive_units():
            time.sleep(2)
            print()
            print(f'''
                    ---------------------------------------
                        CHOOSE UNITS TO THE FIGHT #{self.fight_counter}!
                    ''')


            if x % 2 == 0:
                print(f"Player - choose your fighter!")
                print(self.player_team.name)
                player_unit = self.player_team.choose_unit_by_player()
                print(f'Player choose {player_unit.name} from his squad')
                print()

                time.sleep(2)
                print(f"Player - choose your enemy's unit to fight!")
                print(self.enemy_team.name)
                enemy_unit = self.enemy_team.choose_unit_by_player()
                print(f'Player choose {enemy_unit.name} from enemy\'s squad')

            else:
                time.sleep(2)
                print(f"Enemy choose his fighter!")
                print(self.enemy_team.name)
                enemy_unit = self.enemy_team.choose_unit_by_comp()
                time.sleep(2)
                print(f'Enemy choose {enemy_unit.name} from enemy\'s squad')

                print()
                time.sleep(2)
                print(f"Enemy choose player's unit for the fight!")
                print(self.player_team.name)
                player_unit = self.player_team.choose_unit_by_comp()
                time.sleep(2)
                print(f'Enemy choose {player_unit.name} from player\'s squad')

            fight = Fight.Fight(player_unit, enemy_unit, self.fight_counter, player_team= self.player_team, enemy_team= self.enemy_team)
            self.fight_counter += 1
            x += 1

        self.display_result_board()

    def display_result_board(self):
        time.sleep(2)
        print(f'''
                    ------------------------------------------------------------
                        ******** ARENA #{self.counter_arena} RESULTS ********
                    ------------------------------------------------------------
                ''')

        if self.player_team.check_alive_units():
            self.winner = self.player_team
        elif self.enemy_team.check_alive_units():
            self.winner = self.enemy_team
        else:
            self.winner = None
            print(f"There is no winners in this Arena. Both teams are DEAD")

        if self.winner:
            print(f"The winner of #{self.counter_arena} Arena is: ", self.winner.name)

            time.sleep(2)
            print()
            print(f"ALIVE UNITS of {self.winner.name} squad:")
            alive_team_obj = Team.Team(self.winner.make_alive_team(), self.winner.name)
            alive_team_obj.team_info()

            time.sleep(2)
            print()
            print("DEAD UNITS of {self.winner.name} squad:")
            dead_team_obj = Team.Team(self.winner.dead_team_in_arena(), self.winner.name)

            if self.winner.dead_team_in_arena() != []:
                dead_team_obj.team_info()
            else:
                print("List of dead is empty")
            print()
            self.fight_counter +=1



    def player_results(self):
        self.alive_player_team = self.player_team.make_alive_team()
        self.dead_player_team = self.player_team.dead_team_in_arena()
        player_results = [self.alive_player_team, self.dead_player_team]

        return player_results




