# Emily Adams
# Turn Based Combat Module
# Does heavy lifting for the tbc game.
# Created 10/15/2025
import random
class character(object):
    def __init__(self, name = "default", hitPoints = 1, hitChance = 1, maxDamage = 1, armor = 1):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def hitPoints(self):
        return self.__hitPoints
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            self.__hitPoints = value
        else:
            print("must be an int")
    @property
    def hitChance(self):
        return self.__hitChance
    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                if value <= 100:
                    self.__hitChance = value
                else:
                    print("too large")
            else:
                print("too small")
        else:
            print("must be an int")
    @property
    def maxDamage(self):
        return self.__maxDamage
    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value >= 0:
                if value <= 100:
                    self.__maxDamage = value
                else:
                    print("too large")
            else:
                print("too small")
        else:
            print("must be an int")       
    @property
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                if value <= 100:
                    self.__armor = value
                else:
                    print("too large")
            else:
                print("too small")
        else:
            print("must be an int")
    def printStats(self):
        print(f"""
              Name: {self.name}
              ===========================
              Hit Points: {self.hitPoints}
              Hit Chance: {self.hitChance}
              Max Damage: {self.maxDamage}
              Armor: {self.armor}""")
    def hit(self, monster):
        hitRoll = random.randint(1, 100)
        if hitRoll < self.hitChance:
            print(f"{self.name} hits {monster.name}...")
            damage = random.randint(1, self.maxDamage)
            print(f"for {damage} hit points...")
            damage -= monster.armor
            if damage < 0:
                damage = 0
            if monster.armor > 0:
                print(f"but {monster.name}'s armor absorbs {monster.armor} points of the hit.")
            monster.hitPoints -= damage
        else:
            print(f"{self.name} misses {monster.name}. Yikes.")

def fight(hero, monster):
    keepGoing = True
    while keepGoing:
        hero.hit(monster)
        monster.hit(hero)
        print(f"{hero.name} HP: {hero.hitPoints}")
        print(f"{monster.name} HP: {monster.hitPoints}")
        print("")
        if hero.hitPoints <= 0:
            print(f"{hero.name} loses")
            keepGoing = False
        elif monster.hitPoints <= 0:
            print(f"{monster.name} loses")
            keepGoing = False
        goAgain = int(input("go again? 1. yes 2. no: "))
        if goAgain == 2:
            keepGoing = False

__name__ == "__main__"