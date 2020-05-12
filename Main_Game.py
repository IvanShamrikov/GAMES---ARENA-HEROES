import time
import Arena
import Team
from Shop import Shop
import Warior_Classes

class Main_Game():
    player_Name = None
    player_gold = 10000
    all_arenas = 10
    player_exp = 100
    counter_arena = 1
    alive_player_team = None
    dead_player_team = None
    status_of_game = True
    shop = None



    def welcome_board(self):
        print('''
        ----------------------------------------------------------------------------------------------------------------
        
                                        **********   GAME OF HEROES   **********
        
                                            -- The game by Ivan Shamrikov --
        
        ----------------------------------------------------------------------------------------------------------------''')

        print()
        self.player_Name = input("Enter your name, young Hero ---> ")
        print()
        print(f'''
Welcome, my young hero {self.player_Name}!
Here is some money, you need to make your own squad and fight in 10 arenas.
Let's play the Game!         
        
        ''')
        self.main_game()

    def main_game(self):
        self.alive_player_team = Team.Team(team= [], name= f"{self.player_Name}'s squad")
        self.dead_player_team = Team.Team(team=[], name=f"{self.player_Name}'s dead units")
        self.alive_player_team.team.append(Warior_Classes.Unit_Barbarian(**{"helmet_name": "Iron Helmet", "helmet_value": 300, "boots_name": "Iron boots", "boots_value": 300, "shield_name": "Leather shield", "shield_value": 100, "bodyarmor_name": "Wooden bodyarmor", "bodyarmor_value": 100, "weapon_name": "Wooden cudgel", "weapon_value": 300, "ability_item_name": "Fitness Training 2 lvl", "ability_item_value": 0.2, "abilyty_recharger_moves": 1}))
        self.alive_player_team.team.append(Warior_Classes.Unit_Archer(**{"helmet_name": "Iron Helmet", "helmet_value": 300, "boots_name": "Iron boots", "boots_value": 300, "shield_name": "Wooden shield", "shield_value": 200, "bodyarmor_name": "Golden bodyarmor", "bodyarmor_value": 400, "weapon_name": "Bow 3 lvl", "weapon_value": 600, "ability_item_name": "Bow Dash 3 lvl", "ability_item_value": 0.6, "abilyty_recharger_moves": 0}))
        self.alive_player_team.team.append(Warior_Classes.Unit_Knight(**{"helmet_name": "Golden helmet", "helmet_value": 400, "boots_name": "Iron boots", "boots_value": 300, "shield_name": "Platinum shield", "shield_value": 500, "bodyarmor_name": "Golden bodyarmor", "bodyarmor_value": 400, "weapon_name": "Steel sword", "weapon_value": 600, "ability_item_name": "Karate Training 1 lvl", "ability_item_value": 2, "abilyty_recharger_moves": 2}))
        self.alive_player_team.team.append(Warior_Classes.Unit_Magician(**{"helmet_name": "Golden helmet", "helmet_value": 400, "boots_name": "Iron boots", "boots_value": 300, "shield_name": "Platinum shield", "shield_value": 500, "bodyarmor_name": "Golden bodyarmor", "bodyarmor_value": 400, "weapon_name": "Magic Stick 4 lvl", "weapon_value": 500, "ability_item_name": "Poison Book 2 lvl", "ability_item_value": 0.2, "abilyty_recharger_moves": 3}))

        print(f'''
Wow! You have a squad from 4 heroes!
Barbarian - very strong and powerful. Every forth move he recharge his SuperHit - he can attack all enemy's units.
Archer hits enemies with his bow. His SuperHit - Archer attack a few time one enemy's unit.
Knight is a truly leader. He can stun one of the enemy's unit for several moves.
Magician's SuperHit  is to poison all all enemy's units with his Magic Stick.

There is one more class of Heroes - Healer. It can heel his squad, but for now you don't have any.
Now we are going to the Unit's shop, where you can buy 1 Healer to your squad. ''')
        print()


        while True:

                if len(self.alive_player_team.team) < 5 and self.player_gold < self.check_min_price_of_units():
                    win_status = False
                    self.endgame(win_status) #QUESTION
                    break
                elif self.counter_arena > 10:
                    win_status = True
                    self.endgame(win_status)
                    break


                for i in self.alive_player_team.team:
                    i.health_in_fight = i.health_default

                shop = Shop(player_gold= self.player_gold, player_team= self.alive_player_team)
                shop.units_shopping()
                self.player_gold = shop.player_gold
                self.alive_player_team = shop.player_team

                arena = Arena.Arena(player_team= self.alive_player_team, counter_arena= self.counter_arena)

                time.sleep(2)
                player_results = arena.player_results()

                self.dead_player_team = self.dead_player_team.team.append(player_results[1])
                self.alive_player_team.team = player_results[0]


                if self.alive_player_team.team:

                    time.sleep(2)
                    self.reward_calculator()
                    self.counter_arena +=1
                    print()#FIXME: use multilines prints
                    print()
                    print("Are you ready to prepare for the next Arena? Let's go shopping to buy new units and items!")
                    print()
                    print()

                else:
                    print()
                    print("You loose in this arena. You should buy a new squad.")
                    print("Are you ready to prepare for this Arena one more time? Let's go shopping to buy new units and items!")
                    print()
                    input("Press ENTER to continue -->")


    def reward_calculator(self):
        time.sleep(2)
        print(f'''
        -----------------------------------
                ARENA #{self.counter_arena} REWARD DASH
        ''')

        self.player_gold += 10000
        time.sleep(2)
        print("You earn 10'000 of gold in this Arena")
        print()
        print("Power up your units:")
        for unit in self.alive_player_team.team:
            unit.level += 1
            unit.health_default += 200
            unit.power_default += 200
            time.sleep(1)
            print(f"{unit.name} --> Level +1, Health +200, Power +100")






    def check_min_price_of_units (self):
        barbarian = Warior_Classes.Unit_Barbarian()
        archer = Warior_Classes.Unit_Archer()
        healer = Warior_Classes.Unit_Healer()
        knight = Warior_Classes.Unit_Knight()
        magician = Warior_Classes.Unit_Magician()

        units = [barbarian, archer, healer,knight, magician]
        print()
        prices = []
        for i in units:
            prices.append(i.buy_cost)
        return min(prices)


    def endgame(win_status):

        if win_status:
            print('''
            -----------------------------------------------------
                        ******** GAME OVER ********
                            You win the Game
            -----------------------------------------------------
                        You have win in all 10 Arenas


''')


        else:
            print('''
            ------------------------------------------------------------
                            ******** GAME OVER ********
                               You loose the Game
            ------------------------------------------------------------
                        You have no money to buy any units
                            
                        
''')
        while True:
            answer = input("Do you want to play another game? Enter Y/N -->>> ")
            if answer.lower() not in ("y", "n"):
                print()
                print("Something went wrong. Let's try again")
                continue
            elif answer.lower() == "n":
                print("Have a nice day!")
                break
            else:
                main_game.welcome_board()
                break



main_game = Main_Game()
main_game.welcome_board()

