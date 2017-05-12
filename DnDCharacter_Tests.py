import unittest
from DnDCharacter import*


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
