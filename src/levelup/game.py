from typing import Callable
from levelup.controller import GameController, Direction


class GameUI:
    # Yay Changes
    game: GameController

    def __init__(self):
        self.game = GameController()

    def prompt(self, message: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{message}\n> ")
            if validation_fn(response):
                break
        return response

    def start(self):
        print("""           d8888                                          d8b          
          d88888                                          Y8P          
         d88P888                                                       
        d88P 888 88888b.d88b.  88888b.   .d88b.  .d8888b  888  8888b.  
       d88P  888 888 "888 "88b 888 "88b d8P  Y8b 88K      888     "88b 
      d88P   888 888  888  888 888  888 88888888 "Y8888b. 888 .d888888
     d8888888888 888  888  888 888  888 Y8b.          X88 888 888  888 
    d88P     888 888  888  888 888  888  "Y8888   88888P' 888 "Y888888                             
                     _   _   _                      _         _             
      __ _ _ __   __| | | |_| |__   ___   _ __ ___ (_)___ ___(_)_ __   __ _ 
     / _` | '_ \ / _` | | __| '_ \ / _ \ | '_ ` _ \| / __/ __| | '_ \ / _` |
    | (_| | | | | (_| | | |_| | | |  __/ | | | | | | \__ \__ \ | | | | (_| |
     \__,_|_| |_|\__,_|  \__|_| |_|\___| |_| |_| |_|_|___/___/_|_| |_|\__, |
            _ __   __ _ _ __ | |_ ___                                 |___/ 
           | '_ \ / _` | '_ \| __/ __|                                      
           | |_) | (_| | | | | |_\__ \                                      
           | .__/ \__,_|_| |_|\__|___/                                      
           |_|                                                             """)
        print("You were an adventurer in this land.")
        print("During a quest to slay the most metal of dragons, you awake with no memory of that life.")
        print("Oh...  and you've lost your pants!  You should find them.")
        character = self.prompt("Enter character name", lambda x: len(x) > 0)
        self.game.create_character(character)
        valid_directions = [x.value for x in Direction]
        while True:
            response = self.prompt(
                f"Where should our pantsless hero go! {valid_directions}\n(or ctrl+c to quit)",
                lambda x: x in valid_directions,
            )
            self.game.move(Direction(response))
