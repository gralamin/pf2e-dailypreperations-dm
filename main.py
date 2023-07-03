import region
import weather
import random
import encounter
from enum import Enum
import argparse
import sys
from colors import bcolors
from dice import roll


class TerrainType(Enum):
    AQUATIC = "Aquatic"
    ARCTIC = "Arctic"
    DESERT = "Desert"
    MOUNTAIN = "Mountain"
    FOREST = "Forest"
    SWAMP = "Swamp"
    PLAINS = "Plains"

    @staticmethod
    def choices() -> List[str]:
        return [
            TerrainType.AQUATIC.value,
            TerrainType.ARCTIC.value,
            TerrainType.DESERT.value,
            TerrainType.MOUNTAIN.value,
            TerrainType.FOREST.value,
            TerrainType.SWAMP.value,
            TerrainType.PLAINS.value,
        ]


def check_random_encounter(terrain_type, road=False, river=False, flying=False) -> bool:
    dc = 20
    if terrain_type in [TerrainType.AQUATIC, TerrainType.ARCTIC, TerrainType.DESERT]:
        dc = 17
    if terrain_type in [TerrainType.MOUNTAIN]:
        dc = 16
    if terrain_type in [TerrainType.FOREST, TerrainType.SWAMP]:
        dc = 14
    if terrain_type in [TerrainType.PLAINS]:
        dc = 12
    if road or river:
        dc -= 2
    if flying:
        dc += 3
    _, did_pass = roll("Random Encounter", dc, False)
    return did_pass


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--level", type=int, required=True)
    parser.add_argument(
        "-t", "--terrain", type=str, choices=TerrainType.choices(), required=True
    )
    parser.add_argument("-o", "--road", action="store_true", help="Add if on a road")
    parser.add_argument("-i", "--river", action="store_true", help="Add if on a river")
    parser.add_argument("-f", "--flying", action="store_true", help="Add if flying")
    parser.add_argument(
        "-n", "--numchars", type=int, required=True, help="Number of characters"
    )
    parser.add_argument("-s", "--seed", type=int, default=None)
    parser.add_argument(
        "-r", "--region", type=int, choices=region.REGION_CHOICES, required=True
    )
    parser.add_argument(
        "-e",
        "--season",
        type=str,
        choices=["Spring", "Summer", "Fall", "Winter"],
        required=True,
    )
    parser.add_argument(
        "-m",
        "--extrememonth",
        action="store_true",
        help="Set if coldest / warmest month",
    )

    args = parser.parse_args()
    level = args.level
    num_characters = args.numchars
    terrain = TerrainType(args.terrain)
    reg = region.REGION_LOOKUP[args.region]
    seed = random.randrange(sys.maxsize) if not args.seed else args.seed
    season = weather.Season(args.season)
    random.seed(seed)

    print(f"seed: {seed}\n")
    print(f"--- Random Encounter ---")
    if check_random_encounter(
        terrain, road=args.road, river=args.river, flying=args.flying
    ):
        enc = reg.choose_encounter()
        difficulty = enc.get_encounter_difficulty(level, num_characters)
        skip_str = (
            f" {bcolors.FAIL}SKIP{bcolors.ENDC}"
            if difficulty == encounter.Difficulty.TRIVIAL
            else ""
        )
        print(f"Encounter: {enc.description()}")
        print(f"Difficulty: {difficulty.value} {level}{skip_str}")

    print(f"\n--- Random Weather ---")
    weather.random_weather(season, args.extrememonth, level)


if __name__ == "__main__":
    main()
