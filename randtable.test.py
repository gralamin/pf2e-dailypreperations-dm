import unittest
import randtable


class TestRandTable(unittest.TestCase):
    def setUp(self) -> None:
        self.i = 0
        self.randtable1 = randtable.RandTable(choicer=self.choicer)
        self.randtable1.add_entry("A", 2)
        self.randtable1.add_entry("B", 1)
        self.randtable2 = randtable.RandTable(choicer=self.choicer)
        self.randtable2.add_entry(self.randtable1, 2)
        self.randtable2.add_entry("C", 1)
        return super().setUp()

    def choicer(self, choices):
        ri = self.i % len(choices)
        result = choices[ri]
        self.i += 1
        return result

    def testHitAllTable1(self):
        self.assertEqual(self.randtable1.choose_random(), "A")
        self.assertEqual(self.randtable1.choose_random(), "A")
        self.assertEqual(self.randtable1.choose_random(), "B")
        self.assertEqual(self.randtable1.choose_random(), "A")

    def testHitAllTable2(self):
        # Hit table 1 on i = 0, then hit A on i = 1
        self.assertEqual(self.randtable2.choose_random(), "A")
        # i is now 2, hit C
        self.assertEqual(self.randtable2.choose_random(), "C")
        self.assertEqual(self.randtable2.choose_random(), "A")
        self.assertEqual(self.randtable2.choose_random(), "C")


if __name__ == "__main__":
    unittest.main()
