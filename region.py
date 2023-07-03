from randtable import RandTable
import encounter


class Region:
    def __init__(self, name, level, choicer=None) -> None:
        self.name = name
        self.level = level
        if not choicer:
            self.random_encounters = RandTable()
        else:
            self.random_encounters = RandTable(choicer=choicer)

    def add_encounter(self, enc, weight) -> None:
        self.random_encounters.add_entry(enc, weight)

    def add_previous_region_encounters(self, region, weight) -> None:
        self.random_encounters.add_entry(region.random_encounters, weight)

    def choose_encounter(self) -> encounter.Encounter:
        return self.random_encounters.choose_random()


# -- Region Data --
# TODO, turn into yaml or json file
FAIRMARK = Region("Fairmark Forest", 3)
FAIRMARK.add_encounter(encounter.ENCOUNTER_TRIVIAL_3_FIVE_PLAYERS, 5)
FAIRMARK.add_encounter(encounter.ENCOUNTER_LOW_3_FIVE_PLAYERS_FROG, 3)
FAIRMARK.add_encounter(encounter.ENCOUNTER_LOW_3_FIVE_PLAYERS_WOLF, 3)
FAIRMARK.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLF, 2)
FAIRMARK.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLV, 2)
FAIRMARK.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_HIPPO, 2)
FAIRMARK.add_encounter(encounter.ENCOUNTER_MOD_3_FIVE_PLAYERS_SWARM, 2)
FAIRMARK.add_encounter(encounter.ENCOUNTER_SEV_3_FIVE_PLAYERS, 1)

BARRIAL = Region("Barrial Steppe", 4)
BARRIAL.add_previous_region_encounters(FAIRMARK, 5)
BARRIAL.add_encounter(encounter.ENCOUNTER_LOW_4_BADGER, 3)
BARRIAL.add_encounter(encounter.ENCOUNTER_LOW_4_LOBLOBI, 3)
BARRIAL.add_encounter(encounter.ENCOUNTER_MOD_4_RIDERS, 2)
BARRIAL.add_encounter(encounter.ENCOUNTER_MOD_4_BANDITS, 2)
BARRIAL.add_encounter(encounter.ENCOUNTER_MOD_4_ZEBUB, 2)
BARRIAL.add_encounter(encounter.ENCOUNTER_MOD_4_ZRUKBAT, 2)
BARRIAL.add_encounter(encounter.ENCOUNTER_SEV_4_FIEND, 1)

REGION_LOOKUP = {3: FAIRMARK, 4: BARRIAL}

REGION_CHOICES = REGION_LOOKUP.keys()
