import Mastermind_Data as Da
import Mastermind_Logic as log
import unittest


class DataTests(unittest.TestCase):
    def setUp(self):
        self.dat = Da.data()

    def test_save_get(self):
        self.dat.gemStart(["blå", "grøn", "rød", "blå"])
        self.assertEqual(self.dat.getStart(), ["blå", "grøn", "rød", "blå"])

    def tearDown(self):
        pass


class LogicTests(unittest.TestCase):
    def setUp(self):
        lo = log.dinLogik

    def test_save(self):
        pass

    def tearDown(self):
        pass
