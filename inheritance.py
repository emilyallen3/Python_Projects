#Inheritance Submission Assignment Step 237
#Emily Allen

class Game:
    #Created the parent class Game and 4 attributes
    name = "None Provided"
    publish_date = "01/01/1973"
    number_players = 1
    avg_duration = "0 hrs"

class Video_Game(Game):
    #Created a child class of Game with 2 attributes
    gaming_system = "Atari"
    online_play = True

class Board_Game(Game):
    #Created a child class of Game with 2 attributes
    number_dice = 0
    board_dimensions = "12 x 12 in"
