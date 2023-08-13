from enum import Enum


class Enemy:
    def __init__(self, name, level) -> None:
        self.name = name
        self.level = level

    def get_xp(self, reference_level) -> int:
        computed_level = self.level - reference_level
        if computed_level < -4:
            return 0
        if computed_level < -1:
            return (
                computed_level + 6
            ) * 5  # -4 -> 2 -> 10. -3 -> 3 -> 15. -2 -> 4 -> 20
        if computed_level < 1:
            return (computed_level + 4) * 10  # -1 -> 3 -> 30. 0 -> 4 -> 40
        if computed_level < 3:
            return (computed_level + 2) * 20  # 1 -> 3 -> 60. 2 -> 4 -> 80
        if computed_level == 3:
            return 120
        if computed_level == 4:
            return 160
        if computed_level > 4:
            # Too high, return a very high number to cause a warning
            return 9999

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.level == __value.level


class Hazard:
    def __init__(self, name, level, is_simple=False) -> None:
        self.name = name
        self.level = level
        self.complex = not is_simple

    def get_xp(self, reference_level) -> int:
        enemy_value = Enemy("temp", self.level).get_xp(reference_level)
        if self.complex:
            return enemy_value
        return enemy_value / 5

    def __eq__(self, __value: object) -> bool:
        return (
            self.name == __value.name
            and self.level == __value.level
            and self.complex == __value.complex
        )


class Difficulty(Enum):
    TRIVIAL = "Trivial"
    LOW = "Low"
    MODERATE = "Moderate"
    SEVERE = "Severe"
    EXTREME = "Extreme"
    IMPOSSIBLE = "IMPOSSIBLE"


class Encounter:
    def __init__(self, *enemy_or_hazards) -> None:
        self.creatures = [x for x in enemy_or_hazards]

    def get_encounter_difficulty(self, level, num_characters) -> Difficulty:
        total_xp = sum(x.get_xp(level) for x in self.creatures)
        xp_budgets = {
            Difficulty.TRIVIAL: 10 * num_characters,
            Difficulty.LOW: 15 * num_characters,
            Difficulty.MODERATE: 20 * num_characters,
            Difficulty.SEVERE: 30 * num_characters,
            Difficulty.EXTREME: 40 * num_characters,
        }
        if total_xp <= xp_budgets[Difficulty.TRIVIAL]:
            return Difficulty.TRIVIAL
        if total_xp >= xp_budgets[Difficulty.EXTREME] * 2:
            return Difficulty.IMPOSSIBLE
        if (
            total_xp >= xp_budgets[Difficulty.TRIVIAL]
            and total_xp <= xp_budgets[Difficulty.LOW]
        ):
            ## Judgement call, if 75% or more to low, will call LOW.
            fifty_percent_point = (
                xp_budgets[Difficulty.TRIVIAL] + xp_budgets[Difficulty.LOW]
            ) / 2
            seventy_five_percent_point = (
                fifty_percent_point + xp_budgets[Difficulty.LOW]
            ) / 2
            if total_xp >= seventy_five_percent_point:
                return Difficulty.LOW
            return Difficulty.TRIVIAL
        elif (
            total_xp >= xp_budgets[Difficulty.LOW]
            and total_xp <= xp_budgets[Difficulty.MODERATE]
        ):
            fifty_percent_point = (
                xp_budgets[Difficulty.LOW] + xp_budgets[Difficulty.MODERATE]
            ) / 2
            seventy_five_percent_point = (
                fifty_percent_point + xp_budgets[Difficulty.MODERATE]
            ) / 2
            if total_xp >= seventy_five_percent_point:
                return Difficulty.MODERATE
            return Difficulty.LOW
        elif (
            total_xp >= xp_budgets[Difficulty.MODERATE]
            and total_xp <= xp_budgets[Difficulty.SEVERE]
        ):
            fifty_percent_point = (
                xp_budgets[Difficulty.MODERATE] + xp_budgets[Difficulty.SEVERE]
            ) / 2
            seventy_five_percent_point = (
                fifty_percent_point + xp_budgets[Difficulty.SEVERE]
            ) / 2
            if total_xp >= seventy_five_percent_point:
                return Difficulty.SEVERE
            return Difficulty.MODERATE
        elif (
            total_xp >= xp_budgets[Difficulty.SEVERE]
            and total_xp <= xp_budgets[Difficulty.EXTREME]
        ):
            fifty_percent_point = (
                xp_budgets[Difficulty.SEVERE] + xp_budgets[Difficulty.EXTREME]
            ) / 2
            seventy_five_percent_point = (
                fifty_percent_point + xp_budgets[Difficulty.EXTREME]
            ) / 2
            if total_xp >= seventy_five_percent_point:
                return Difficulty.EXTREME
            return Difficulty.SEVERE
        # Final case, must be extreme
        return Difficulty.EXTREME

    def description(self) -> str:
        counts = {}
        for x in self.creatures:
            counts[x.name] = counts.setdefault(x.name, 0) + 1
        str_parts = []
        for x in counts:
            str_parts.append(f"{counts[x]}x {x}")
        return ", ".join(str_parts)

    def __eq__(self, __value: object) -> bool:
        return self.creatures == __value.creatures


# ---- My random encounters ----
# TODO: Make this a json or yaml file to parse instead
MONSTER_BADGER = Enemy("Badger", 0)
MONSTER_GIANT_FROG = Enemy("Giant Frog", 1)
MONSTER_DIRE_WOLF = Enemy("Dire Wolf", 3)
MONSTER_WOLF = Enemy("Wolf", 1)
MONSTER_GIANT_WOLVERINE = Enemy("Giant Wolverine", 4)
MONSTER_HIPPO_WEAK = Enemy("Weak Hippopotamus", 4)
MONSTER_RAVEN_SWARM = Enemy("Raven Swarm", 3)
MONSTER_RAT_SWARM = Enemy("Rat Swarm", 1)
MONSTER_TIGER = Enemy("Tiger", 4)
MONSTER_LION = Enemy("Lion", 3)

MONSTER_ELITE_BADGER = Enemy("Elite Badger", 1)
MONSTER_LOBLOBI = Enemy("Loblobi", 1)
MONSTER_BOAR = Enemy("Boar", 2)
MONSTER_BANDIT = Enemy("Bandit", 2)
MONSTER_ELITE_BANDITS = Enemy("Elite Bandit", 3)
MONSTER_ZRUKBAT = Enemy("Zrukbat", 2)
MONSTER_WEAK_ZEBUB = Enemy("Weak Zebub", 2)
MONSTER_BARBAZU = Enemy("Barbazu", 5)
MONSTER_IMP = Enemy("Imp", 1)

MONSTER_HIERACOSPHINX = Enemy("Hieracosphinx", 5)
MONSTER_HYDRA = Enemy("Hydra", 6)
MONSTER_DRETCH = Enemy("Dretch", 2)
MONSTER_WORM_DEMON = Enemy("Vermlek - Worm Demon (In Bandit body)", 3)
MONSTER_ABRIKANDILU = Enemy("Abrikandilu", 4)
MONSTER_MANTICORE_WEAK = Enemy("Weak Manticore", 5)
MONSTER_PERYTON = Enemy("Peryton", 4)

ENCOUNTER_TRIVIAL_3_FIVE_PLAYERS = Encounter(
    MONSTER_BADGER, MONSTER_BADGER, MONSTER_BADGER
)
ENCOUNTER_LOW_3_FIVE_PLAYERS_FROG = Encounter(
    MONSTER_GIANT_FROG, MONSTER_GIANT_FROG, MONSTER_GIANT_FROG, MONSTER_GIANT_FROG
)
ENCOUNTER_LOW_3_FIVE_PLAYERS_WOLF = Encounter(MONSTER_DIRE_WOLF, MONSTER_DIRE_WOLF)
ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLF = Encounter(
    MONSTER_WOLF, MONSTER_WOLF, MONSTER_WOLF, MONSTER_WOLF, MONSTER_WOLF
)
ENCOUNTER_MOD_3_FIVE_PLAYERS_WOLV = Encounter(
    MONSTER_GIANT_WOLVERINE, MONSTER_GIANT_WOLVERINE
)
ENCOUNTER_MOD_3_FIVE_PLAYERS_HIPPO = Encounter(MONSTER_HIPPO_WEAK, MONSTER_HIPPO_WEAK)
ENCOUNTER_MOD_3_FIVE_PLAYERS_SWARM = Encounter(
    MONSTER_RAVEN_SWARM, MONSTER_RAVEN_SWARM, MONSTER_RAT_SWARM
)
ENCOUNTER_SEV_3_FIVE_PLAYERS = Encounter(MONSTER_TIGER, MONSTER_TIGER, MONSTER_LION)

ENCOUNTER_LOW_4_BADGER = Encounter(
    MONSTER_ELITE_BADGER,
    MONSTER_ELITE_BADGER,
    MONSTER_ELITE_BADGER,
    MONSTER_ELITE_BADGER,
    MONSTER_ELITE_BADGER,
)
ENCOUNTER_LOW_4_LOBLOBI = Encounter(
    MONSTER_LOBLOBI, MONSTER_LOBLOBI, MONSTER_LOBLOBI, MONSTER_LOBLOBI, MONSTER_LOBLOBI
)
ENCOUNTER_MOD_4_RIDERS = Encounter(
    MONSTER_BOAR, MONSTER_BOAR, MONSTER_ELITE_BANDITS, MONSTER_ELITE_BANDITS
)
ENCOUNTER_MOD_4_BANDITS = Encounter(
    MONSTER_BOAR, MONSTER_ELITE_BANDITS, MONSTER_BANDIT, MONSTER_BANDIT, MONSTER_BANDIT
)
ENCOUNTER_MOD_4_ZRUKBAT = Encounter(
    MONSTER_ZRUKBAT, MONSTER_ZRUKBAT, MONSTER_ZRUKBAT, MONSTER_ZRUKBAT, MONSTER_ZRUKBAT
)
ENCOUNTER_MOD_4_ZEBUB = Encounter(
    MONSTER_WEAK_ZEBUB,
    MONSTER_WEAK_ZEBUB,
    MONSTER_WEAK_ZEBUB,
    MONSTER_WEAK_ZEBUB,
    MONSTER_WEAK_ZEBUB,
)
ENCOUNTER_SEV_4_FIEND = Encounter(
    MONSTER_BARBAZU, MONSTER_BARBAZU, MONSTER_IMP, MONSTER_IMP
)

ENCOUNTER_LOW_5_HIERA = Encounter(MONSTER_HIERACOSPHINX, MONSTER_HIERACOSPHINX)
ENCOUNTER_LOW_5_BANDIT = Encounter(MONSTER_BANDIT, MONSTER_BANDIT, MONSTER_BANDIT, MONSTER_BANDIT, MONSTER_BANDIT)
ENCOUNTER_MOD_5_HYDRA = Encounter(MONSTER_HYDRA, MONSTER_HIERACOSPHINX)
ENCOUNTER_MOD_5_DRETCH = Encounter(MONSTER_DRETCH, MONSTER_DRETCH, MONSTER_WORM_DEMON, MONSTER_WORM_DEMON, MONSTER_ABRIKANDILU)
ENCOUNTER_MOD_5_MANTICORE = Encounter(MONSTER_MANTICORE_WEAK, MONSTER_MANTICORE_WEAK, MONSTER_MANTICORE_WEAK)
ENCOUNTER_MOD_5_BANDITS = Encounter(MONSTER_BOAR, MONSTER_BOAR, MONSTER_BOAR, MONSTER_ELITE_BANDITS, MONSTER_ELITE_BANDITS, MONSTER_ELITE_BANDITS)
ENCOUNTER_MOD_5_PERYTON = Encounter(MONSTER_PERYTON, MONSTER_PERYTON, MONSTER_PERYTON, MONSTER_PERYTON, MONSTER_PERYTON)