import Team
import time
import Fight

class Arena():
    def __init__(self, init_p_team, init_arena_counter):
        self.player_team = init_p_team
        self.arena_counter = init_arena_counter
        self.comp_team = Team.Team()

    def start_arena(self):
        self.comp_team.create_rand_comp_team()
        self.arena_set_health()
        self.arena_start_board()
        time.sleep(5)
        self.arena_fight()
        self.arena_final_board()

    def arena_set_health(self):
        for team in [self.player_team.team, self.comp_team.team]:
            for unit in team:
                unit.health_in_fight = unit.health_with_armor

    def arena_start_board(self):
        print(f'''
                                    ------------------------------------------------------------
                                            ******** ARENA #{self.arena_counter} BOARD ********
                                    ------------------------------------------------------------
                                                        Welcome to the Arena!
                                    {self.player_team.name}                VS                  {self.comp_team.name}
                                                                                
                    ''')
        print("PLAYER TEAM")
        self.player_team.team_info()

        print()
        print("COMPUTER TEAM")
        self.comp_team.team_info()

    def arena_final_board(self):
        print(f'''
                    ------------------------------------------------------------
                            ******** ARENA #{self.arena_counter} FINAL BOARD ********
                    ------------------------------------------------------------
                    {self.player_team.name}                VS                  {self.comp_team.name}
                    ''')
        
        if len(self.player_team.alive_team) == 0  and len(self.comp_team.alive_team) == 0:
            winner = None
        elif len(self.player_team.alive_team) != 0:
            winner = self.player_team
        else:
            winner = self.comp_team
        
        if not winner:
            print("There is no winners in this Arena. Both teams are DEAD")
        else:
            print(f"The winner of #{self.arena_counter} Arena is: {self.winner.name}")

            time.sleep(2)
            print(f"ALIVE UNITS of {winner.name} squad:")
            winner.alive_team.team_info()

            print() 

            time.sleep(2)
            print(f"DEAD UNITS of {winner.name} squad:")
            winner.dead_team.team_info()

        print("-"*30)


    def arena_fight(self):
        fight_counter = 1

        while len(self.player_team.alive_team) !=0 and len(self.comp_team.alive_team) != 0:
                
            if fight_counter % 2 != 0:
                #хід гравця
                print()
                print("Player - choose your fighter!")

                self.player_team.team_info(True)
                player_unit = self.player_team.choose_unit_by_player()

                print()
                print("Player - choose your enemy's unit to fight!")
                self.comp_team.team_info(True)
                comp_unit = self.comp_team.choose_unit_by_player()
                
            else:
                #хід компа
                comp_unit = self.comp_team.chose_random_unit()
                player_unit = self.player_team.chose_random_unit()

                print("Хід компа")
                

            fight = Fight.Fight(player_unit, comp_unit, fight_counter)
            fight.fight_start()

            fight_counter += 1

            if fight_counter == 4:
                break