import Mastermind_Data as Da
import unittest




class DataTests(unittest.TestCase):
    def setUp(self):
        dat = Da.data()

    def test_save(self):
        self.assertEqual(dat.gemStart(), (2000, 12, 20))

    def tearDown(self):
        pass