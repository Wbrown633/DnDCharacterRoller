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

