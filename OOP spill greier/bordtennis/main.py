import keyboard
import random
import time

class Opponent:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def __str__(self):
        return f"> NAME:  {self.name}\n> DIFFICULTY:  {self.difficulty}"

    def set_name(self, newname):
        self.name = newname
    def set_difficulty(self,newdifficulty):
        self.difficulty = newdifficulty
    
    def get_name(self):
        return self.name
    def get_difficulty(self):
        return self.difficulty
    
    # function that decides which side the opoonent will shoot the ball on
    def incomingShot(self):
        return random.randint(0,1)


def main():
    print("Terminal table tennis (Press ESC to exit)")
    player_name = input("Enter your name: ")
    print("If ball comes left, click A, if ball comes right, click D")
    print("Press SPACE to start")
    keyboard.wait("space")
    levelEn = Opponent("Greg", 1)
    print("Game starts in \n3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    while True:
        if keyboard.is_pressed("esc"):
            break

        shoot = levelEn.incomingShot()
        
        if shoot == 0:
            print("Ball is coming left")
            while True:
                if keyboard.is_pressed("a"):
                    print("You hit the ball!")
                    break
                if keyboard.is_pressed("d"):
                    print("You missed the ball!")
                    break
        else:
            print("Ball is coming right")
            while True:
                if keyboard.is_pressed("d"):
                    print("You hit the ball!")
                    continue
                if keyboard.is_pressed("a"):
                    print("You missed the ball!")
                    break
    

main()

def test():
    levelEn = Opponent("whete",2)
    shoot = levelEn.incomingShot()
    print(shoot)
#test()