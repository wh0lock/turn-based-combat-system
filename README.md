# turn-based-combat-system
Outlines the turn based combat system and object-oriented programming.

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
            if value bigger than or equal to zero:
                if value smaller than or equal to one hundred:
                    self.__hitPoints = value
        otherwise: print "too large", "too small" or "must be an int" depending on error
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
        - parameters: self
        - create var "hitRoll"; "hitRoll" gets "random.randint(1,100)"
        if hitRoll bigger than or equal to self.hitChance, 
            create var "damageRoll"; "damageRoll" gets "random.randint(1, self.maxDamage)"
            create var "damageDone"; "damageDone" gets "damageRoll - self.armor"
            if damageDone smaller than or equal to 0, print {self.name} loses.
        - create var "postHitPoints"; "postHitPoints" gets "self.hitPoints - damageDone"
    define function: fight()
        - parameters: hero, monster
        create var "goAgain"; "goAgain" gets prompt: go another round? 1. yes 2. no
        keepGoing = True
        while keepGoing: 
            character.hit(hero)
            print(f"""
            {hero} hits {monster} for {damageDone} hit points. 
            {monster}'s armor absorbs {monster.armor} points of damage.
            """)
            monster.hitPoints = postHitPoints
            print(f"""
            hero: {hero.hitPoints}
            monster: {monster.hitPoints}
            """)
            hit(monster)
            print(f"""
            {monster} hits {hero} for {damageDone} hit points.
            {hero}'s armor absorbs {hero.armor} points of damage.
            """)
            hero.hitPoints = postHitPoints
            print(f"""
            hero: {hero.hitPoints}
            monster: {monster.hitPoints}
            """)
            if goAgain == 2, 
                keepGoing = False
    __name__ gets "__main__" to establish as module           

