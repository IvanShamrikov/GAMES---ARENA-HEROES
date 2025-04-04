import Arena
import Team
import UnitClasses
import colorama
import time
import Shop
# colorama.init(autoreset=True)
# print(colorama.Fore.RED + "dsa")
# print(colorama.Back.YELLOW + "dsa")
# print(colorama.Style.NORMAL)

class Game():
    player_name = None
    player_gold = 1000
    all_arenas = 5
    arena_counter = 0
    player_team = None
    shop = None
    game_result = None

    def start_board(self):
        print('''
        ----------------------------------------------------------------------------------------------------------------
        
                                        **********   GAME OF HEROES   **********
        
                                            -- The game by Ivan Shamrikov --
        
        ----------------------------------------------------------------------------------------------------------------
              
            ''')
        self.player_name = input("Type your name, young Hero! ---> ")
        time.sleep(1)
        print(f'''
Welcome, my young hero {self.player_Name}!
Here is some money ({self.player_gold}gold), you need to make your own 
squad and fight in {self.all_arenas} arenas.
Let's play the Game!         
        ''')
        time.sleep(1)

        self.player_team = Team.Team()

        start_team = [UnitClasses.Knight(),
                      UnitClasses.Healer(),
                      UnitClasses.Catapult(),
                      UnitClasses.Defender()]
        self.player_team.team.extend(start_team)
        
        print(f'''
Wow! You have a squad with 4 heroes!
Knight is a truly leader. Every forth move he recharge his SplashAttack - 
    he can splash all enemy units at 50% power.
Healer has very important SuperAbility - every third move he can heal
    all teammates by 20% from they maxHP
Catapult by its SuperAttack hits x2 damage to the chosen enemy unit. 
    Recharge takes 4 moves.
Defender create shield for all teammetes for the next hit and reflect some damage. 
    Recharge takes 4 moves

There is two more class of Heroes 
Wizard is a long-range fighter. He can stun all enemy units for next fight and reduce crit chance to 0 for the next moves.
    Recharge takes 4 moves.
Archer's PoisonedArrow do 50 damage to 1 enemy unit for the next  2 fights. Recharge takes 3 moves.

Now we are going to the Unit's shop, where you can buy 1 unit to complete 
squad (5 units). ''')
        print()



    def up_team(self):
        pass
    
    def final_winner_board(self):
        pass

    def final_looser_board(self):
        pass

    def start_game(self):
        
        self.start_board()

        while self.arena_counter < self.all_arenas:
            shop = Shop.Shop(self.player_team, self.player_gold)
            game_after_shop = shop.welcome_board()
            
            if game_after_shop == False:
                self.game_result = False
                break
            
            arena = Arena.Arena(self.player_team, self.arena_counter)
            arena.start_arena()

            if len(self.team.alive_team) < 0:
                self.game_result = False
                break
            
            self.arena_counter += 1
            self.up_team()

        if self.game_result == True:
            self.final_winner_board()
        elif self.game_result == False:
            self.final_looser_board()

    