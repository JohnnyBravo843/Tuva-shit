import random as r

class Karakter:
    def __init__(self, navn, level = 1, health = 100, mana=100, attack=10, defence = 10):
        self.level = level
        self.name = navn
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defence = defence
        self.inventory = {"weapons":["sverd","spyd"]}

    def __str__(self):
        return f"=========\n> Navn {self.name}\n> Health {self.health}\n> Mana {self.mana}\n> Attack {self.attack}"
    

    def get_inventory(self):
        utskrift = f""
        for i in self.inventory:
            utskrift += f">{i}\n"
            for i in self.inventory[i]:
                utskrift += f" -{i}\n"   
        return utskrift
    
    def hit(self, damage):
        self.health -=  int((1-self.defence/100) * damage)
    
 
    
    def get_name(self):
        return self.name
    def get_hp(self):
        return self.health
    def get_mp(self):
        return self.mana
    
    def set_name(self, newname):
        self.name = newname
    def set_hp(self, amount):
        self.health = amount
    def set_mp(self, amount):
        self.mana = amount
    
    def cast_spell(self, target, cost = 20, damage = 5):
        self.mana -= cost
        target.set_hp(target.get_hp()-damage)
    
    def melee_attack(self,target):
        return "jalla"
    

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

# Klasser
class Mage(Karakter):
    def __init__(self, navn, level = 1, health=75, mana=150, attack=10,defence =5):
        super().__init__(navn, level, health, mana, attack, defence)
    
    # Egenskaper
    def cast_spell(self, target, cost=10, damage=10):
        return super().cast_spell(target, cost, damage)

class Ranger(Karakter):
    def __init__(self, navn, level=1, health=100, mana=100, attack=10, defence=10, agility=10):
        super().__init__(navn, level, health, mana, attack, defence, agility)
    
    def hit(self, damage):
        dodge_chance = self.agility / 100
        if r.random() < dodge_chance:
            return f"{self.name} dodged the attack!"
        else:
            return super().hit(damage)

class Barbarian(Karakter):
    def __init__(self, navn, level=1, health=125, mana=50, attack=15, defence=20):
        super().__init__(navn, level, health, mana, attack, defence)

class Priest(Karakter):
    def __init__(self, navn, level=1, health=100, mana=120, attack=15, defence=15):
        super().__init__(navn, level, health, mana, attack, defence)

class Potionmaster(Karakter):
    def __init__(self, navn, level=1, health=100, mana=100, attack=10, defence=10):
        super().__init__(navn, level, health, mana, attack, defence)


fiende = Karakter("Mohg")

# Her starter spillet
def main():
    print("Welkommen til placeholder")
    
    navnInp = input("Hva Vil du hete?\n")  
    
    rolleInp = input("Hvilke rolle vil du spille?\n(1) Mage\n(2) Barbarian\n(3) Ranger\n(4) Priest\n")
    if rolleInp == "1":
        spiller = Mage(navnInp)
    elif rolleInp == "2":
        spiller = Barbarian(navnInp)
    elif rolleInp == "3":
        spiller = Ranger(navnInp)
    elif rolleInp == "4":
        spiller = Priest(navnInp)
    
    



    while spiller.is_alive() and fiende.is_alive():
        print(f"{spiller}\n{fiende}")


        inp = input("vil du angripe? ja/nei\n")
        if inp == "ja":
            spiller.cast_spell(fiende)
        elif inp == "kys":
            spiller.set_hp(0)


main()