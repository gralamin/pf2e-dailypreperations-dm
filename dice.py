import random
from typing import Tuple

from colors import bcolors


def rollD20(roller=random.randint) -> int:
    return roller(1, 20)


def roll(
    description, dc, nat_twenty_matters, roller=random.randint
) -> Tuple[int, bool]:
    result = rollD20(roller=roller)
    did_pass = result >= dc
    pass_str = ""
    if did_pass:
        if nat_twenty_matters and result == 20:
            pass_str = f"{bcolors.UNDERLINE}{bcolors.OKGREEN}Pass{bcolors.ENDC}"
        else:
            pass_str = f"{bcolors.OKGREEN}Pass{bcolors.ENDC}"
    else:
        pass_str = f"{bcolors.FAIL}Fail{bcolors.ENDC}"
    print(f"{description} - {result} vs DC {dc}: {pass_str}")
    return result, did_pass
