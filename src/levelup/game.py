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
        print("     You were an adventurer in this land.")
        print("     During a quest to slay the most metal of dragons, you awake with no memory of that life.")
        print("     Oh...  and you've lost your pants!  You should find them.")

        while True:
            self.help()
            command = self.prompt("Enter Command", lambda x: len(x) > 0)
            command = command.lower()
            if command in commands.keys():
                commands[command](self)

    def create_character(self):
        warrior = r'''
                          ,dM
                         dMMP
                        dMMM'
                        \MM/
                        dMMm.
                       dMMP'_\---.
                      _| _  p ;88;`.
                    ,db; p >  ;8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  ;_  |
                   |    |`T88P_ /  `\;
                   :_.-~|d8P'`Y/    /
                    \_   TP    ;   7`\
         ,,__        >   `._  /'  /   `\_
         `._ """"~~~~------|`\;' ;     ,'
            """~~~-----~~~'\__[|;' _.-'  `\
                    ;--..._     .-'-._     ;
                   /      /`~~"'   ,'`\_ ,/
                  ;_    /'        /    ,/
                  | `~-l         ;    /
                  `\    ;       /\.._|
                    \    \      \     \
                    /`---';      `----'
                   (     /            
        '''
        print(warrior)
        character = self.prompt("Character Name", lambda x: len(x) > 0)
        self.game.create_character(character)

    def play(self):
        print(f"Playing as {self.game.status.character.name}")
        valid_directions = [x.value for x in Direction]
        valid_options = [x.value for x in Direction]
        valid_options.append('q')
        play = True
        while play:
            response = self.prompt(
                f">>>>>Where should our pantsless hero go! {valid_directions}-->(or q quit)",
                lambda x: x in valid_options,
            )
            if response.lower() == 'q':
                self.quit()
                play = False
            else:
                self.game.move(Direction(response))

    def help(self):
        print("\n\n")
        print("\033[4mC\033[0mreate character")
        print("\033[4mP\033[0mlay")
        print("\033[4mQ\033[0muit")
        print("\n\n")     

    def quit(self):
        self.status()
    
    def exit_game(self):
        exit() 

    def status(self):
        status = self.game.get_status()
        print(status)

commands = {
    'q': GameUI.exit_game,
    'c': GameUI.create_character,
    'p': GameUI.play
}