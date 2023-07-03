import unittest
import dice


class TestDice(unittest.TestCase):
    def testFail(self):
        def mockRoller(min, max):
            return 5

        dc = 22
        result, did_pass = dice.roll("Test roll", dc, False, roller=mockRoller)
        self.assertEqual(result, 5)
        self.assertEqual(did_pass, False)

    def testPass(self):
        def mockRoller(min, max):
            return 5

        dc = 2
        result, did_pass = dice.roll("Test roll", dc, False, roller=mockRoller)
        self.assertEqual(result, 5)
        self.assertEqual(did_pass, True)

    def testPassNat20(self):
        def mockRoller(min, max):
            return 20

        dc = 10
        result, did_pass = dice.roll("Test roll", dc, True, roller=mockRoller)
        self.assertEqual(result, 20)
        self.assertEqual(did_pass, True)


if __name__ == "__main__":
    unittest.main()
