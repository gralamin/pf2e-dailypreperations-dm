from enum import Enum
import randtable
import random
from dice import roll


class Season(Enum):
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"
    WINTER = "Winter"


class WeatherEvent:
    def __init__(self, name, possible_levels) -> None:
        self.name = name
        self.levels = possible_levels

    def okay_for_level(self, level) -> bool:
        if min(self.levels) > level + 4:
            return False
        return True


def random_weather(
    season: Season, extreme_month: bool, level: int, roller=random.randint
):
    # First check for WEATHER EVENTS
    weather_event, did_pass = roll(
        "Weather Event (on 20 maybe two)", 17, True, roller=roller
    )
    if did_pass:
        num_events = 1
        if weather_event == 20:
            _, two_pass = roll("Second Event", 17, False, roller=roller)
            num_events = 2 if two_pass else 1
        for _ in range(num_events):
            generate_weather_event(level)

    print(f"--Rest of day")
    random_temp(season, extreme_month)
    random_precipitation(season)


def generate_weather_event(level):
    event = WEATHER_EVENTS.choose_random()
    while not event.okay_for_level(level):
        event = WEATHER_EVENTS.choose_random()
    print(f"Weather Event: {event.name} - {event.levels}")


def random_temp(season: Season, extreme_month: bool, roller=random.randint):
    if season in [Season.SUMMER, Season.WINTER]:
        dc = 16 if extreme_month else 18
        check_for = "heat" if season == Season.SUMMER else "cold"
        _, did_pass = roll(
            f"{season.value}: Check for {check_for}", dc, False, roller=roller
        )
        if did_pass:
            if Season.SUMMER:
                print("Temp: Mild Heat")
                return
            else:
                print("Temp: Mild Cold")
                return
    print("Temp: Normal")


def random_precipitation(season: Season, roller=random.randint):
    dc = 15
    if season == Season.WINTER:
        dc = 8
    elif season == Season.SUMMER:
        dc = 20
    _, did_pass = roll(
        f"Check for precipitation for {season.value}", dc, False, roller=roller
    )
    if did_pass:
        print("Precipitation: Light")
    else:
        print("Precipitation: None")


# -- Generated Data --
# TODO: Move to a YAML / json file
WEATHER_FOG = WeatherEvent("Fog", [0])
WEATHER_HEAVY_DOWNPOUR = WeatherEvent("Heavy Downpour", [0])
WEATHER_COLD_SNAP = WeatherEvent("Cold Snap", [1])
WEATHER_WINDSTORM = WeatherEvent("Windstorm", [1])
WEATHER_HAILSTORM = WeatherEvent("Severe Hailstorm", [2])
WEATHER_BLIZZARD = WeatherEvent("Blizzard", [6])
WEATHER_SUPERNATURAL_STORM = WeatherEvent("Supernatural Storm", [6])
WEATHER_FLASH_FLOOD = WeatherEvent("Flash Flood", [7])
WEATHER_WILDFIRE = WeatherEvent("Wildfire", [4, 10])
WEATHER_SUBSIDENCE = WeatherEvent("Subsidence", [5, 12])
WEATHER_THUNDERSTORM = WeatherEvent("Thunderstorm", [7, 13])
WEATHER_TORNADO = WeatherEvent("Tornado", [12, 17])

WEATHER_EVENTS = randtable.RandTable()
WEATHER_EVENTS.add_entry(WEATHER_FOG, 3)
WEATHER_EVENTS.add_entry(WEATHER_HEAVY_DOWNPOUR, 4)
WEATHER_EVENTS.add_entry(WEATHER_COLD_SNAP, 2)
WEATHER_EVENTS.add_entry(WEATHER_WINDSTORM, 3)
WEATHER_EVENTS.add_entry(WEATHER_HAILSTORM, 1)
WEATHER_EVENTS.add_entry(WEATHER_BLIZZARD, 1)
WEATHER_EVENTS.add_entry(WEATHER_SUPERNATURAL_STORM, 1)
WEATHER_EVENTS.add_entry(WEATHER_FLASH_FLOOD, 1)
WEATHER_EVENTS.add_entry(WEATHER_WILDFIRE, 1)
WEATHER_EVENTS.add_entry(WEATHER_SUBSIDENCE, 1)
WEATHER_EVENTS.add_entry(WEATHER_THUNDERSTORM, 1)
WEATHER_EVENTS.add_entry(WEATHER_TORNADO, 1)
