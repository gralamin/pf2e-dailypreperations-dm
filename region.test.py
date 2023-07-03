import unittest

import encounter
import region


class TestRegion(unittest.TestCase):
    def setUp(self) -> None:
        self.i = 0

        self.fairmark = region.Region("Fairmark Forest", 3, choicer=self.choicer)
        self.fairmark.add_encounter(encounter.ENCOUNTER_TRIVIAL_3_FIVE_PLAYERS, 5)
        self.fairmark.add_encounter(encounter.ENCOUNTER_LOW_3_FIVE_PLAYERS_FROG, 3)
        self.fairmark.add_encounter(encounter.ENCOUNTER_LOW_3_FIVE_PLAYERS_WOLF, 3)
        self.fairmark.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLF, 2)
        self.fairmark.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLV, 2)
        self.fairmark.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_HIPPO, 2)
        self.fairmark.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_SWARM, 2)
        self.fairmark.add_encounter(encounter.ENCOUNTER_SEV_3_FIVE_PLAYERS, 1)

        self.barrial = region.Region("Barrial Steppe", 4, choicer=self.choicer)
        self.barrial.add_previous_region_encounters(self.fairmark, 5)
        self.barrial.add_encounter(encounter.ENCOUNTER_LOW_4_BADGER, 3)
        self.barrial.add_encounter(encounter.ENCOUNTER_LOW_4_LOBLOBI, 3)
        self.barrial.add_encounter(encounter.ENCOUNTER_MOD_4_RIDERS, 2)
        self.barrial.add_encounter(encounter.ENCOUNTER_MOD_4_BANDITS, 2)
        self.barrial.add_encounter(encounter.ENCOUNTER_MOD_4_ZEBUB, 2)
        self.barrial.add_encounter(encounter.ENCOUNTER_MOD_4_ZRUKBAT, 2)
        self.barrial.add_encounter(encounter.ENCOUNTER_SEV_4_FIEND, 1)
        return super().setUp()

    def choicer(self, choices):
        ri = self.i % len(choices)
        result = choices[ri]
        self.i += 1
        return result

    def testHitAllFairmark(self):
        for _ in range(5):
            self.assertEqual(
                self.fairmark.choose_encounter(),
                encounter.ENCOUNTER_TRIVIAL_3_FIVE_PLAYERS,
            )
        for _ in range(3):
            self.assertEqual(
                self.fairmark.choose_encounter(),
                encounter.ENCOUNTER_LOW_3_FIVE_PLAYERS_FROG,
            )
        for _ in range(3):
            self.assertEqual(
                self.fairmark.choose_encounter(),
                encounter.ENCOUNTER_LOW_3_FIVE_PLAYERS_WOLF,
            )
        for _ in range(2):
            self.assertEqual(
                self.fairmark.choose_encounter(),
                encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLF,
            )
        for _ in range(2):
            self.assertEqual(
                self.fairmark.choose_encounter(),
                encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLV,
            )
        for _ in range(2):
            self.assertEqual(
                self.fairmark.choose_encounter(),
                encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_HIPPO,
            )
        for _ in range(2):
            self.assertEqual(
                self.fairmark.choose_encounter(),
                encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_SWARM,
            )
        self.assertEqual(
            self.fairmark.choose_encounter(), encounter.ENCOUNTER_SEV_3_FIVE_PLAYERS
        )

    def testHitAllBarrial(self):
        # First two times, goes to trivial 3 on fairmark
        for _ in range(2):
            self.assertEqual(
                self.barrial.choose_encounter(),
                encounter.ENCOUNTER_TRIVIAL_3_FIVE_PLAYERS,
            )
        # Now low fairmark
        self.assertEqual(
            self.barrial.choose_encounter(), encounter.ENCOUNTER_LOW_3_FIVE_PLAYERS_FROG
        )
        # now each goes down this list, minus one used roll
        for _ in range(2):
            self.assertEqual(
                self.barrial.choose_encounter(), encounter.ENCOUNTER_LOW_4_BADGER
            )
        for _ in range(3):
            self.assertEqual(
                self.barrial.choose_encounter(), encounter.ENCOUNTER_LOW_4_LOBLOBI
            )
        for _ in range(2):
            self.assertEqual(
                self.barrial.choose_encounter(), encounter.ENCOUNTER_MOD_4_RIDERS
            )
        for _ in range(2):
            self.assertEqual(
                self.barrial.choose_encounter(), encounter.ENCOUNTER_MOD_4_BANDITS
            )
        for _ in range(2):
            self.assertEqual(
                self.barrial.choose_encounter(), encounter.ENCOUNTER_MOD_4_ZEBUB
            )
        for _ in range(2):
            self.assertEqual(
                self.barrial.choose_encounter(), encounter.ENCOUNTER_MOD_4_ZRUKBAT
            )
        self.assertEqual(
            self.barrial.choose_encounter(), encounter.ENCOUNTER_SEV_4_FIEND
        )


if __name__ == "__main__":
    unittest.main()
