#Inheritance Submission Assignment Step 237
#Emily Allen

class Game:
    name = "None Provided"
    publish_date = "01/01/1973"
    number_players = 1
    avg_duration = "0 hrs"

class Video_Game(Game):
    gaming_system = "Atari"
    online_play = True

class Board_Game(Game):
    number_dice = 0
    board_dimensions = "12 x 12 in"
