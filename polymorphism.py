#Polymorphism Submission Assignment Step 245
#Emily Allen

class Game:
    #Created the parent class Game and 4 attributes
    name = "None Provided"
    publish_date = "01/01/1973"
    number_players = 1
    avg_duration = "0 hrs"

        #This is a function of the parent class
    def Set_Up(self):
        entry_players = int(input("How many players: "))
        if entry_players > 1:
            print("Roll a dice to see who goes first.")
        else:
            print("Ready Player 1")
            

class Video_Game(Game):
    #Created a child class of Game with 2 attributes
    gaming_system = "Atari"
    online_play = True

    #This is the same function as the parent class but gives the option to play online
    def Set_Up(self):
            online_play = input("Would you like to play online: (Y/N)")
            if online_play == 'Y':
                print("Online Play Initiated")
            else:
                    print("Offline Play Mode")
            entry_players = int(input("How many players: "))
            if entry_players > 1:
                print("Roll a dice to see who goes first.")
            else:
                print("Ready Player 1")
    

class Board_Game(Game):
    #Created a child class of Game with 2 attributes
    number_players = 4
    number_dice = 2
    board_dimensions = "12 x 12 in"

    def Set_Up(self):
        entry_players = int(input("How many players: "))
        if entry_players > 1:
            print("Roll a dice to see who goes first.")
        else:
            print("Ready Player 1")


video_game = Video_Game()
video_game.Set_Up()

board_game = Board_Game()
board_game.Set_Up()
