Do daily random encounter / weather checks for PF2e based on Kingmaker rules.

Example command:
```
$ python3 main.py -l 4 -t Plains -n 5 -s 8268022766967418823 -r 4 -e Spring
seed: 8268022766967418823

--- Random Encounter ---
Random Encounter - 16 vs DC 12: Pass
Encounter: 5x Elite Badger
Difficulty: Low 4

--- Random Weather ---
Weather Event (on 20 maybe two) - 20 vs DC 17: _Pass_
Second Event - 17 vs DC 17: Pass
Weather Event: Heavy Downpour - [0]
Weather Event: Heavy Downpour - [0]
--Rest of day
Temp: Normal
Check for precipitation for Spring - 8 vs DC 15: Fail
Precipitation: None
```
This saids we have 5 characters of level 4, on the plains, in region #4, During Spring, with a specific seed.

## TODO
* Move data into files that get parsed.