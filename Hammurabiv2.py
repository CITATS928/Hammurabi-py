import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def plagueDeaths(self, population):
        if self.rand.randint(0, 99) < 15:  # 15% chance
            return population // 2
        return 0

    def starvationDeaths(self, population, bushelsFed):
        people_fed = bushelsFed // 20
        return max(0, population - people_fed)

    def uprising(self, population, starved):
        return starved > 0.45 * population

    def immigrants(self, population, acresOwned, grainInStorage):
        if population > 0:
            return (20 * acresOwned + grainInStorage) // (100 * population) + 1
        return 0

    def harvest(self, acres):
        return acres * self.rand.randint(1, 6)

    def grainEatenByRats(self, bushels):
        if self.rand.randint(0, 99) < 40:  # 40% chance
            return (self.rand.randint(10, 30) * bushels) // 100
        return 0

    def newCostOfLand(self):
        return self.rand.randint(17, 23)

hammurabi_info = {
    "key": "value",
    "people": 95,
    "entered_people": 5,
    "bushels": 2800,
    "acres": 1000,
    "landValue": 19,
    "Year_Counter": 1
}

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.rungame()
