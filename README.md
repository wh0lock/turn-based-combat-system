# turn-based-combat-system
Outlines the turn based combat system and object-oriented programming.
```
eadams7_tbc.py
This module does the heavy lifting for eadams7_combat.py. "character" class helps to create a character. "fight()" function takes two names and pits them against each other.
    - imports random (referenced later)
- create's class "character" in style of "object" 
    - define function: initialize class
        - attributes: self, name, hitPoints, hitChance, maxDamage, armor
            - set default ints to 1
            - set default name to "default"
        assign variables
    PROPERTIES
    tag: @property (of character class)
    define method: name() (IE: getter)
        - attributes: self
        - return self.__name
    tag: @name.setter 
    define method: name()
        - attributes: self, value
        - self.__name = value
        - limitations/type: none/str
    tag: @property
    define method: hitPoints()
        - attributes: self
        - return self.__hitPoints
    tag: @hitPoints.setter
    define method: hitPoints()
        - attributes: self, value
        - limitations/type: see below/int
        if type(value) is int:
            self.__hitPoints = value
        otherwise: "must be an int" 
    tag: @property
    define method: hitChance()
        - attributes: self
        - return self.__hitChance
    tag: @hitChance.setter
    define method: hitChance()
        - attributes: self, value
        - limitations/type: see below/randint
        if type(value) is int:
            if value bigger than or equal to zero:
                if value smaller than or equal to one hundred:
                    self.__hitChance = value
        otherwise: print "too large", "too small" or "must be an int" depending on error
    tag: @property
    define method: maxDamage()
        - attributes: self
        - return self.__maxDamage
    tag: @maxDamage.setter
    define method: maxDamage()
        - attributes: self, value
        - limitations/type: see below/int
        if type(value) is int:
            if value bigger than or equal to zero:
                if value smaller than or equal to one hundred:
                    self.__maxDamage = value
        otherwise: print "too large", "too small" or "must be an int" depending on error
    tag: @property
    define method: armor()
        - attributes: self
        - return self.__armor
    tag: @armor.setter
        - attributes: self, value
        - limitations/type: see below/int
        if type(value) is int:
            if value bigger than or equal to zero:
                if value smaller than or equal to one hundred:
                    self.__armor = value
        otherwise: print "too large", "too small" or "must be an int" depending on error
    define function: printStats()
        - parameters: self
        - print(f"""name: {self.name} etc.
        """)
    define function: hit()
        - parameters: self, monster
        - create var "hitRoll"; "hitRoll" gets random.randint(1, 100)
        if hitRoll < self.hitChance: 
            print(f"{self.name} hits {monster.name}...")
            create var "damage"; "damage" gets "random.randint(1, self.maxDamage)"
            print(f"for {damage} hit points...")
            damage -= monster.armor
            if damage < 0:
                damage gets 0
            if monster.armor > 0:
                print(f" but {monster.name}'s armor absorbs monster.armor points of the hit.")
            monster.hitPoints -= damage
        else:
            print(f"{self.name} misses {monster.name}. Yikes.")

define function: fight()
    - parameters: hero, monster
    create var "goAgain"; "goAgain" gets prompt: go another round? 1. yes 2. no
    keepGoing = True
        while keepGoing: 
            hero.hit(monster)
            monster.hit(hero)
            print(f"{hero.name} HP: {hero.hitPoints}")
            print(f"{monster.name} HP: {monster.hitPoints}")
            print("")
            if hero.hitPoints <= 0:
                print "hero loses"
                keepGoing = False
            elif monster.hitPoints <= 0:
                print "monster loses"
                keepGoing = False
            create var "goAgain"; "goAgain" gets input prompt: go again? 1. yes 2. no: 
            if goAgain == 2, 
                keepGoing = False
    
__name__ gets "__main__" to establish as module          
```
