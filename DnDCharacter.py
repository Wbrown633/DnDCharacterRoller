# Randomly Generates a DnD character based on Inputs and 5e Rules
# Then produces the PDF character sheet based on the results


import unittest
import random

RACES = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
CLASSES = ['Barbarian', 'Bard', 'Clearic', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
           'Sorcerer', 'Warlock', 'Wizard']
LISTOFSTATS = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']


def ChooseRace():
    CharacterRace = random.choice(RACES)
    return CharacterRace

def ChooseClass():
    CharacterClass = random.choice(CLASSES)
    return CharacterClass

def RollSingleStat():
    rolls = []
    for i in range(4):
        rolls.append(random.randint(1, 6))

    rolls.sort()
    rolls.remove(rolls[0])
    return sum(rolls)

def CompileStats():
    List_of_rolls = []
    for roll in range(6):
        List_of_rolls.append(RollSingleStat())
    Stats = dict(zip(LISTOFSTATS, List_of_rolls))
    return Stats

class MyTest(unittest.TestCase):
    def test_ChooseRace(self):
        self.assertIn(ChooseRace(), RACES, "ERROR: Invalid Race")

    def test_ChooseClass(self):
        self.assertIn(ChooseClass(), CLASSES, "ERROR: Invalid Class")

    def test_RollSingleStat(self):
        self.assertIn(RollSingleStat(), range(3, 18), "ERROR: Invalid Roll")

    def test_RolledStats(self):
        for k, v in CompileStats().items():
            self.assertIn(k, LISTOFSTATS, "ERROR: Invalid Stat Type Entry")
            self.assertIn(v, range(21), "ERROR: Invalid Stat Value Entry ")

if __name__ == '__main__':
    unittest.main()

