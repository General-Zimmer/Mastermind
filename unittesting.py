import Mastermind_Data as Da
import Mastermind_Logic as log
import unittest


class DataTests(unittest.TestCase):
    def setUp(self):
        self.dat = Da.data()

    def test_save_get(self):
        self.dat.gemStart(["blå", "grøn", "rød", "blå"])
        self.assertEqual(["blå", "grøn", "rød", "blå"], self.dat.getStart())

    def tearDown(self):
        pass


class LogicTests(unittest.TestCase):
    def setUp(self):
        self.lo = log.dinLogik()

    def test_save_tjekfarve(self):
        self.lo.huskStart(["grøn", "blå", "hvid", "gul", "lilla"])
        self.assertEqual([1, 1], self.lo.tjekFarve(["grøn", "null", "blå", "null", "null"]))

    def tearDown(self):
        pass
