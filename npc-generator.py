# This actually shouldn't be in this project, this should be in its own.
# Maybe I should rename this to pf2e-tools...

from enum import Enum
from randtable import RandTable

class Ancestry(Enum):
    ANDROID = "Android"
    AUTOMATON = "Automaton"
    AZARKETI = "Azarketi"
    CATFOLK = "Catfolk"
    CONRASU = "Conrasu"
    DWARF = "Dwarf"
    ELF = "Elf"
    FETCHLING = "Fetchling"
    FLESHWARP = "Fleshwarp"
    GHORIAN = "Ghorian"
    GNOLL = "Gnoll"
    GNOME = "Gnome"
    GOBLIN = "Goblin"
    GOLOMA = "Goloma"
    GRIPPLI = "Grippli"
    HALFLING = "Halfling"
    HOBGOBLIN = "Hobgoblin"
    HUMAN = "Human"
    KASHRISHI = "Kashrishi"
    KITSUNE = "Kitsune"
    KOBOLD = "Kobold"
    LESHY = "Leshy"
    LIZARDFOLK = "Lizardfolk"
    NAGAJI = "Nagaji"
    ORC = "Orc"
    POPPET = "Poppet"
    RATFOLK = "Ratfolk"
    SHISK = "Shisk"
    SHOOMY = "Shoomy"
    SKELETON = "Skeleton"
    SPRITE = "Sprite"
    STRIX = "Strix"
    TENGU = "Tengu"
    VANARA = "Vanara"
    VISHKANYA = "Vishkanya"

    @staticmethod
    def choose_random():
        """My setting demographics
        
Ancestry | Percentage | d100 roll
--- | :---: | :---:
Android | < 0.1% | 00, d20=1
Automation | < 0.1% | 00, d20=2
Azarketi | 2% | 01-02
Catfolk | 5% | 03-07
Conrasu | <0.1% | 00, d20=3
Dwarf | 20% | 08-27
Elf | 10% | 28-37
Fetchling | 2% | 38-39
Fleshwarp | 0.3% | 00, d20=4-7
Ghorian | 0.5% | 00, d20=8-14
Gnoll | 3.5% | 40-43
Gnome | 2.5% | 44-45
Goblin | 1.5% | 46-47
Goloma | 1.5% | 48
Grippli | 6% | 49-54
Halfling | 6% | 55-60
Hobgoblin | 1.5% | 61
Human | 15% | 62-76
Kashrishi | 0.5% | 00, d20=15-20
Kitsune | 1% | 77
Kobolds | 1.5% | 78-79
Leshy | 2.5% | 80-82
Lizardfolk | 1.5% | 83
Nagaji | 2.5% | 84-85
Orcs | 1.1% | 86
Poppet | 1.1% | 87
Ratfolk | 3.5% | 88-90
Shisk | 1.1% | 91
Shoomy | 1.5% | 92
Skeleton | 1.1% | 93
Sprite | 2.5% | 94-95
Strix | 1.5% | 96
Tengu | 1.5% | 97
Vanara | 1.5% | 98
Vishkanya | 1% | 99
        """
        table_rare = RandTable()
        table_rare.add_entry(Ancestry.ANDROID, 1)
        table_rare.add_entry(Ancestry.AUTOMATON, 1)
        table_rare.add_entry(Ancestry.CONRASU, 1)
        table_rare.add_entry(Ancestry.FLESHWARP, 4)
        table_rare.add_entry(Ancestry.GHORIAN, 7)
        table_rare.add_entry(Ancestry.KASHRISHI, 6)

        table_rest = RandTable()
        table_rest.add_entry(table_rare, 1)
        table_rest.add_entry(Ancestry.AZARKETI, 2)
        table_rest.add_entry(Ancestry.CATFOLK, 5)
        table_rest.add_entry(Ancestry.DWARF, 20)
        table_rest.add_entry(Ancestry.ELF, 10)
        table_rest.add_entry(Ancestry.FETCHLING, 2)
        table_rest.add_entry(Ancestry.GNOLL, 4)
        table_rest.add_entry(Ancestry.GNOME, 2)
        table_rest.add_entry(Ancestry.GOBLIN, 2)
        table_rest.add_entry(Ancestry.GOLOMA, 1)
        table_rest.add_entry(Ancestry.GRIPPLI, 6)
        table_rest.add_entry(Ancestry.HALFLING, 6)
        table_rest.add_entry(Ancestry.HOBGOBLIN, 1)
        table_rest.add_entry(Ancestry.HUMAN, 15)
        table_rest.add_entry(Ancestry.KITSUNE, 1)
        table_rest.add_entry(Ancestry.KOBOLD, 2)
        table_rest.add_entry(Ancestry.LESHY, 3)
        table_rest.add_entry(Ancestry.LIZARDFOLK, 1)
        table_rest.add_entry(Ancestry.NAGAJI, 2)
        table_rest.add_entry(Ancestry.ORC, 1)
        table_rest.add_entry(Ancestry.POPPET, 1)
        table_rest.add_entry(Ancestry.RATFOLK, 3)
        table_rest.add_entry(Ancestry.SHISK, 1)
        table_rest.add_entry(Ancestry.SHOOMY, 1)
        table_rest.add_entry(Ancestry.SKELETON, 1)
        table_rest.add_entry(Ancestry.SPRITE, 2)
        table_rest.add_entry(Ancestry.TENGU, 1)
        table_rest.add_entry(Ancestry.VANARA, 1)
        table_rest.add_entry(Ancestry.VISHKANYA, 1)
        return table_rest.choose_random()


# Its possible to generate an orc half-orc or an elf half-elf, don't worry about it.
class Heritage(Enum):
    STANDARD = "Standard Heritage"
    HALF_ELF = "Half elf"
    HALF_ORC = "Half orc"
    AASIMAR = "Aasimar"
    APHROITE = "Aphorite"
    ARDANDE = "Ardande"
    BEASTKIN = "Beastkin"
    CHANGELING = "Changeling"
    DHAMPIR = "Dhampir"
    DUSKWALKER = "Duskwalker"
    GANZI = "Ganzi"
    NAARI = "Naari (Ifrit)"
    OREAD = "Oread"
    REFLECTION = "Reflection"
    SULI = "Suli"
    SYLPH = "Sylph"
    TALOS = "Talos"
    TIEFLING = "Tiefling"

    @staticmethod
    def choose_random():
        table_versatile = RandTable()
        # Uncommon gets 2 entries
        # rare get 1
        table_versatile.add_entry(Heritage.AASIMAR, 2)
        table_versatile.add_entry(Heritage.APHROITE, 2)
        table_versatile.add_entry(Heritage.ARDANDE, 2)
        table_versatile.add_entry(Heritage.BEASTKIN, 1)
        table_versatile.add_entry(Heritage.CHANGELING, 2)
        table_versatile.add_entry(Heritage.DHAMPIR, 2)
        table_versatile.add_entry(Heritage.DUSKWALKER, 2)
        table_versatile.add_entry(Heritage.GANZI, 2)
        table_versatile.add_entry(Heritage.NAARI, 2)
        table_versatile.add_entry(Heritage.OREAD, 2)
        table_versatile.add_entry(Heritage.REFLECTION, 1)
        table_versatile.add_entry(Heritage.SULI, 2)
        table_versatile.add_entry(Heritage.SYLPH, 2)
        table_versatile.add_entry(Heritage.TALOS, 2)
        table_versatile.add_entry(Heritage.TIEFLING, 2)
        
        table = RandTable()
        table.add_entry(Heritage.STANDARD, 55)
        table.add_entry(Heritage.HALF_ELF, 2)
        table.add_entry(Heritage.HALF_ORC, 2)
        table.add_entry(table_versatile, 41)
        return table.choose_random()

# Vast simplification
class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    TRANSMASC = "Trans (male)"
    TRANSFEM = "Trans (female)"
    NONBIN = "Nonbinary"

    @staticmethod
    def choose_random():
        table = RandTable()
        table.add_entry(Gender.MALE, 4825)
        table.add_entry(Gender.FEMALE, 4925)
        table.add_entry(Gender.TRANSFEM, 100)
        table.add_entry(Gender.TRANSMASC, 100)
        table.add_entry(Gender.NONBIN, 50)
        return table.choose_random()

# Vast simplification
class Sexuality(Enum):
    ASEXUAL = "Asexual"
    XHETRO = "Hetrosexual (exclusive)"
    HETRO = "Hetrosexual mostly"
    BI = "Bisexual (no clear preference)"
    XHOMO = "Homosexual (exclusive)"
    HOMO = "Homosexual mostly"

    @staticmethod
    def choose_random():
        table = RandTable()
        table.add_entry(Sexuality.ASEXUAL, 100)
        table.add_entry(Sexuality.BI, 100)
        table.add_entry(Sexuality.XHETRO, 8900)
        table.add_entry(Sexuality.XHOMO, 100)
        table.add_entry(Sexuality.HOMO, 200)
        table.add_entry(Sexuality.HETRO, 500)
        return table.choose_random()

class Ethnicity(Enum):
    # Based on https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=1310929
    NORTH_AM_INDIGENOUS = "North American Indigenous (202)"
    # Skipping other north american,  because its mostly provinical
    EUROPE_BRITISH = "British Isles (202)"
    EUROPE_FRENCH = "French (203)"
    EUROPE_WEST = "Western European (EG german, dutch) (204)"
    EUROPE_NORTH = "Northern European (EG Finnish, Icelandic) (205)"
    EUROPE_SOUTH = "Southern European (EG Greek, Spanish) (206)"
    EUROPE_SOUTHEAST = "Southeast European (EG Serbia) (207)"
    EUROPE_EAST = "East European (208)"
    EUROPE_OTHER = "Other European (eg Roma) (209)"
    CARRIBEAN = "Carribean (3)"
    LATIN_CENTRAL_AM = "Latin, central and south american (4)"
    AFRICAN_CENTRAL = "Central / West African (eg Chadian) (502)"
    AFRICAN_NORTH = "North Affrician (eg Egypt) (503)"
    AFRICAN_SOUTH = "South / East African (eg Nubian) (504)"
    ASIAN_WEST = "West / Central Asian and middle east (EG Iranian) (602)"
    ASIAN_SOUTH = "South Asian (EG India, Sri Lanka) (603)"
    ASIAN_EAST = "East / southeast Asian (EG Chinese, Malaysian) (604)"
    OCEANIANIC_PACIFIC = "Pacific Islander (eg Hawaiian) (702)"
    OCEANIANIC_OTHER = "Other Oceanic (eg Maori) (703)"
    # SKipping OTHER_OTHER because its mostly religious in nature. This does miss some people.

    @staticmethod
    def choose_random():
        # for my current needs, bias towards North European area
        # Bias that way, but make sure everyone can show up.
        # Its impossible to judge what population would be in medieval times accurately, so these are my basic amounts for all world:
        # Base Total europe should be about 15%
        # Base total NA should be about 5%
        # Base total Carribean should be about 3%
        # Base total Asia should be about 40%
        # Base Latin Am should be about 9%
        # Base Africa should be about 23%
        # Base oceanic shoulld be about 5%
        north_table = RandTable()
        north_table.add_entry(Ethnicity.NORTH_AM_INDIGENOUS, 1)

        # Within Europe, we want higher north europen, and surrounding area, fall off from there.
        # So going to use a weight of 3, 2, 1 by closeness.
        europe_table = RandTable()
        europe_table.add_entry(Ethnicity.EUROPE_BRITISH, 2)
        europe_table.add_entry(Ethnicity.EUROPE_FRENCH, 1)
        europe_table.add_entry(Ethnicity.EUROPE_WEST, 2)
        europe_table.add_entry(Ethnicity.EUROPE_NORTH, 3)
        europe_table.add_entry(Ethnicity.EUROPE_SOUTH, 1)
        europe_table.add_entry(Ethnicity.EUROPE_SOUTHEAST, 1)
        europe_table.add_entry(Ethnicity.EUROPE_EAST, 2)
        europe_table.add_entry(Ethnicity.EUROPE_OTHER, 1)

        carribean_table = RandTable()
        carribean_table.add_entry(Ethnicity.CARRIBEAN, 1)

        latin_table = RandTable()
        latin_table.add_entry(Ethnicity.LATIN_CENTRAL_AM, 1)

        # I have no idea the relative sizes here, so just uniform
        african_table = RandTable()
        african_table.add_entry(Ethnicity.AFRICAN_CENTRAL, 1)
        african_table.add_entry(Ethnicity.AFRICAN_NORTH, 1)
        african_table.add_entry(Ethnicity.AFRICAN_SOUTH, 1)

        oceanic_table = RandTable()
        oceanic_table.add_entry(Ethnicity.OCEANIANIC_OTHER, 1)
        oceanic_table.add_entry(Ethnicity.OCEANIANIC_PACIFIC, 1)

        # India and china so outpopulate everything else they decide the sizes here.
        asian_table = RandTable()
        asian_table.add_entry(Ethnicity.ASIAN_WEST, 1)
        asian_table.add_entry(Ethnicity.ASIAN_SOUTH, 3)
        asian_table.add_entry(Ethnicity.ASIAN_EAST, 3)

        # This over represents some areas.
        # Here, due to bias, we are going to shrink everything by 25% evenly and add to europe
        final_table = RandTable()
        final_table.add_entry(north_table, 375)
        final_table.add_entry(carribean_table, 225)
        final_table.add_entry(latin_table, 675)
        final_table.add_entry(african_table, 1725)
        final_table.add_entry(oceanic_table, 375)
        final_table.add_entry(asian_table, 3000)
        final_table.add_entry(europe_table, 3625)

        return final_table.choose_random()
        

class Alignment(Enum):
    LG = "Lawful Good"
    NG = "Neutral Good"
    CG = "Chaotic Good"
    LN = "Lawful Neutral"
    N = "Neutral"
    CN = "Chaotic Neutral"
    LE = "Lawful Evil"
    NE = "Neutral Evil"
    CE = "Chaotic Evil"
    
    @staticmethod
    def choose_random():
        # currently equally likely
        table = RandTable()
        for x in list(Alignment):
            table.add_entry(x, 1)
        return table.choose_random()


class CharacterClass(Enum):
    ALCHEMIST = "Alchemist"
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CHAMPION = "Champion"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    INVESTIGATOR = "Investigator"
    KINETICIST = "Kineticist"
    MAGUS = "Magus"
    MONK = "Monk"
    ORACLE = "Oracle"
    PSYCHIC = "Psychic"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    SUMMONER = "Summoner"
    SWASHBUCKLER = "Swashbuckler"
    THAUMATURGE = "Thaumaturge"
    WITCH = "Witch"
    WIZARD = "Wizard"
    GUNSLINGER = "Gunslinger"
    INVENTOR = "Inventor"

    @staticmethod
    def choose_random():
        # currently equally likely
        table = RandTable()
        for x in list(CharacterClass):
            table.add_entry(x, 1)
        return table.choose_random()

if __name__ == "__main__":
    print(Ancestry.choose_random().value)
    print(Heritage.choose_random().value)
    print(Gender.choose_random().value)
    print(Sexuality.choose_random().value)
    print(Ethnicity.choose_random().value)
    print(Alignment.choose_random().value)
    print(CharacterClass.choose_random().value)