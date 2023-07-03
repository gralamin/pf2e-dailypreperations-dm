import unittest
import encounter

BASE_LEVEL = 6


class TestMonster(unittest.TestCase):
    def setUp(self) -> None:
        self.m = encounter.Enemy("Test", BASE_LEVEL)
        return super().setUp()

    def test_get_xp_level_minus_5(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL + 5), 0)

    def test_get_xp_level_minus_4(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL + 4), 10)

    def test_get_xp_level_minus_3(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL + 3), 15)

    def test_get_xp_level_minus_2(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL + 2), 20)

    def test_get_xp_level_minus_1(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL + 1), 30)

    def test_get_xp_level(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL), 40)

    def test_get_xp_level_plus_1(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL - 1), 60)

    def test_get_xp_level_plus_2(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL - 2), 80)

    def test_get_xp_level_plus_3(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL - 3), 120)

    def test_get_xp_level_plus_4(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL - 4), 160)

    def test_get_xp_level_plus_5(self):
        self.assertEqual(self.m.get_xp(BASE_LEVEL - 5), 9999)


class TestHazard(unittest.TestCase):
    def setUp(self) -> None:
        self.c = encounter.Hazard("Test", BASE_LEVEL, False)
        self.s = encounter.Hazard("Test", BASE_LEVEL, True)
        return super().setUp()

    def test_get_xp_level_minus_5(self):
        adjustment = 5
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 0)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 0)

    def test_get_xp_level_minus_4(self):
        adjustment = 4
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 10)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 2)

    def test_get_xp_level_minus_3(self):
        adjustment = 3
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 15)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 3)

    def test_get_xp_level_minus_2(self):
        adjustment = 2
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 20)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 4)

    def test_get_xp_level_minus_1(self):
        adjustment = 1
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 30)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 6)

    def test_get_xp_level(self):
        adjustment = 0
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 40)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 8)

    def test_get_xp_level_plus_1(self):
        adjustment = -1
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 60)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 12)

    def test_get_xp_level_plus_2(self):
        adjustment = -2
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 80)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 16)

    def test_get_xp_level_plus_3(self):
        adjustment = -3
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 120)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 24)

    def test_get_xp_level_plus_4(self):
        adjustment = -4
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 160)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 32)

    def test_get_xp_level_plus_5(self):
        adjustment = -5
        self.assertEqual(self.c.get_xp(BASE_LEVEL + adjustment), 9999)
        self.assertEqual(self.s.get_xp(BASE_LEVEL + adjustment), 9999 / 5)


class TestEncounter(unittest.TestCase):
    def setUp(self) -> None:
        m = encounter.Enemy("ETest", BASE_LEVEL - 2)
        c = encounter.Hazard("CHTest", BASE_LEVEL - 2, False)
        s = encounter.Hazard("SHTest", BASE_LEVEL - 2, True)
        self.e = encounter.Encounter(m, m, c, c, s, s, s, s, s)
        return super().setUp()

    def test_description(self):
        self.assertEqual(self.e.description(), "2x ETest, 2x CHTest, 5x SHTest")

    def test_get_encounter_difficulty_five_chars_mod_6_level_11(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL + 5, 5)
        self.assertEqual(difficulty, encounter.Difficulty.TRIVIAL)

    def test_get_encounter_difficulty_five_chars_mod_6_level_10(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL + 4, 5)
        self.assertEqual(difficulty, encounter.Difficulty.TRIVIAL)

    def test_get_encounter_difficulty_five_chars_mod_6_level_9(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL + 3, 5)
        self.assertEqual(difficulty, encounter.Difficulty.TRIVIAL)

    def test_get_encounter_difficulty_five_chars_mod_6_level_8(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL + 2, 5)
        self.assertEqual(difficulty, encounter.Difficulty.TRIVIAL)

    def test_get_encounter_difficulty_five_chars_mod_6_level_7(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL + 1, 5)
        self.assertEqual(difficulty, encounter.Difficulty.LOW)

    def test_get_encounter_difficulty_five_chars_mod_6_level_6(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL + 0, 5)
        self.assertEqual(difficulty, encounter.Difficulty.MODERATE)

    def test_get_encounter_difficulty_five_chars_mod_6_level_5(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL - 1, 5)
        self.assertEqual(difficulty, encounter.Difficulty.SEVERE)

    def test_get_encounter_difficulty_five_chars_mod_6_level_4(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL - 2, 5)
        self.assertEqual(difficulty, encounter.Difficulty.EXTREME)

    def test_get_encounter_difficulty_five_chars_mod_6_level_3(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL - 3, 5)
        self.assertEqual(difficulty, encounter.Difficulty.EXTREME)

    def test_get_encounter_difficulty_five_chars_mod_6_level_2(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL - 4, 5)
        self.assertEqual(difficulty, encounter.Difficulty.IMPOSSIBLE)

    def test_get_encounter_difficulty_five_chars_mod_6_level_1(self):
        difficulty = self.e.get_encounter_difficulty(BASE_LEVEL - 5, 5)
        self.assertEqual(difficulty, encounter.Difficulty.IMPOSSIBLE)


if __name__ == "__main__":
    unittest.main()
