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
            if value >= 0:
                if value <= 100:
                    self.__hitPoints = value
                else:
                    print("too large")
            else:
                print("too small")
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
    def hit(self):
        hitRoll = random.randint(1, 100)
        if hitRoll >= self.hitChance:
            damageRoll = random.randint(1, self.maxDamage)
            damageDone = damageRoll - self.armor
            if damageDone <= 0:
                print(f"{self.name} loses.")
        postHitPoints = self.hitPoints - damageDone
 
__name__ == "__main__"