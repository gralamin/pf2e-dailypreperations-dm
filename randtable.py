import random


class RandTable:
    def __init__(self, choicer=random.choice) -> None:
        self.table = []
        self.choicer = choicer

    def add_entry(self, entry, weight):
        for _ in range(weight):
            self.table.append(entry)

    def choose_random(self):
        result = self.choicer(self.table)
        try:
            return result.choose_random()
        except:
            return result
