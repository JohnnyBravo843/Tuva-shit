import keyboard

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

def main():
    print("Terminal table tennis (Press ESC to exit)")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                print("Exiting...")
                break
            else:
                pass
        except:
            break
    print("Exited")
main()

def test():
    levelEn = Opponent("Greg",1)
    print(levelEn)

