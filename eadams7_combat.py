import random
import eadams7_tbc

def main():
    hero = eadams7_tbc.character()
    hero.name = "Hero"
    hero.hitPoints = 15
    hero.hitChance = random.randint(1, 100)
    hero.maxDamage = 5
    hero.armor = 3

    monster = eadams7_tbc.character()
    monster.name = "Monster"
    monster.hitPoints = 30
    monster.hitChance = random.randint(1, 100)
    monster.maxDamage = 5
    monster.armor = 0
    
    hero.printStats()
    monster.printStats()

    eadams7_tbc.fight(hero, monster)

if __name__ == "__main__":
    main()