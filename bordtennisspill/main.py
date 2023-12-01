# Author: Mikkel Bergmann & John Arne Grung Hestenes
# Last updated: 2023-30-23

# Importing modules
import keyboard
import random
import time
import os

# Player class
class Player:
    def __init__(self, name, high_score=0):
        self.name = name
        self.high_score = high_score
        
    def inc_score(self):
        self.high_score += 1
    def show_info(self):
        print(f"\nNAME:  {self.name}\nSCORE:  {self.high_score}")

# Opponent class
class Contender:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.misschance = 100 - difficulty
    
    def get_name(self):
        return self.name
    def get_difficulty(self):
        return self.difficulty
    
    # Function to return time window for different opponents
    def time_window(self):
        if self.difficulty == 5:
            return 1.7
        elif self.difficulty == 2:
            return 1.2
        elif self.difficulty == 1:
            return 0.9
        elif self.difficulty == 0:
            return 0.6
    
    # function that decides which side the opoonent will shoot the ball on
    def incomingShot(self):
        if random.randint(0,100) > self.misschance:
            return "miss"
        return random.randint(0,1)

# Function to wait for click
def check_clicked_key(keyEn,KeyTo):
    while True:
        if keyboard.is_pressed(keyEn):
            return keyEn
        if keyboard.is_pressed(KeyTo):
            return KeyTo
        time.sleep(0.05) 

# Dynamic variable to set time window for player to press key
timeWindow = 0

# Creating player object
#os.system("cls")
player = Player(input("=================================\nWelcome to Terminal Table Tennis! \n=================================\nChoose a name: "))

# The game function
def game():
    os.system("cls")
    print("\nChoose your opponent:")
    print("1. Greg  (Easy)")
    print("2. Bob   (Medium)")
    print("3. Dylan (Hard)")
    print("4. Wheat (Impossible)")

    opponent_choice = None

    def on_key_event(e):
        nonlocal opponent_choice
        if e.event_type == keyboard.KEY_DOWN:
            if e.name in ['1', '2', '3', '4']:
                opponent_choice = e.name
                keyboard.unhook_all()

    keyboard.hook(on_key_event)

    while opponent_choice is None:
        pass

    if opponent_choice == "1":
        opponent = Contender("Greg", 5)
    elif opponent_choice == "2":
        opponent = Contender("Bob", 2)
    elif opponent_choice == "3":
        opponent = Contender("Dylan", 1)
    elif opponent_choice == "4":
        opponent = Contender("Wheat", 0)

    print(f"\nYou selected {opponent.get_name()} as your opponent, good luck!")
    
    # Dynamic variable to change time window to shoot back based on difficulty
    timeWindow = opponent.time_window()

    # Game instructions
    print("\nThe game is quite simple. When the game starts, there'll be a visual representation of a table tennis table.\nThe opponent will shoot the ball to either the left or right side of the table.\nYou have to press the corresponding key to hit the ball back.\nIf you hit the ball back, you get a point. If you miss, you lose.\nIf the opponent misses, you win. Good luck!\n(Use A and D to hit the ball back.)")
    print("\nPress SPACE to start or ESC to quit")
    
    # Checks if player wanna start game or quit
    if check_clicked_key("esc","space") == "esc":
        return "Player quit"
    else:
        os.system("cls")
        print("3...")
        time.sleep(0.5)
        print("2..")
        time.sleep(0.5)
        print("1.")
        time.sleep(0.5)

        # Loop to keep player in-game until they win/lose
        playing = True
        while playing:
            shot = opponent.incomingShot()
            start = time.time()
            os.system("cls")

            # Logic if opponent shoots left
            if shot == 0:
                print(f"| | |\n-----\n|o| |")
                time.sleep(0.3)

                # While loop to wait for keypress
                while time.time() - start < timeWindow:
                    if keyboard.is_pressed("a"):
                        player.inc_score()
                        break
                    if keyboard.is_pressed("d"):
                        os.system("cls")
                        playing = False
                        print("You missed the ball!")
                        player.show_info()
                        break
                    time.sleep(0.01)
                
                # If player doesn't press key in time, they lose
                else:
                    os.system("cls")
                    print("Du brukte for lang tid!")
                    player.show_info()
                    break
                
            # Logic if opponent shoots right
            elif shot == 1:
                print("| | |\n-----\n| |o|")
                time.sleep(0.3)

                # While loop to wait for keypress
                while time.time()-start < timeWindow:
                    if keyboard.is_pressed("a"):
                        os.system("cls")
                        playing = False
                        print("You missed the ball!")
                        player.show_info()
                        break
                    if keyboard.is_pressed("d"):
                        player.inc_score()
                        break
                    time.sleep(0.01)
                
                # If player doesn't press key in time, they lose
                else:
                    os.system("cls")

                    print("Du brukte for lang tid!")
                    player.show_info()
                    break
            
            # Logic if opponent misses
            elif shot == "miss":
                print(f"{opponent.get_name()} missed the ball, you win!")
                player.show_info()
                playing = False

# Start game
game()

# Loop to keep game going until player quits
gameContinue = True
while gameContinue:
    
    print("\nWanna continue playing? (y/n): ")
    answer = check_clicked_key("y","n")
    if answer == "y":
        game()
    elif answer == "n":
        os.system("cls")
        print("Thanks for playing!")
        gameContinue = False