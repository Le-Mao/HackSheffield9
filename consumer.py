import random
from organism import *
class Consumer(Organism):
    feedstock_utilisation:float = 1
    food_demand:float = 0.5
    food_sources:list = []
    growthRate: float

    def __init__(self, name : str, initial_pop : int, food_demand: float, feedstock_utilisation: float, growthRate: float):
        self.population = initial_pop
        self.food_sources
        self.name = name
        self.food_demand = food_demand
        self.feedstock_utilisation = feedstock_utilisation
        self.growthRate = growthRate

    def eat(self, amount):
        # food weight is the amount of the food source that gets eaten
        foodWeight = amount / len(self.food_sources)
        for food in self.food_sources:
            food.die(foodWeight)
        #self.food_sources[0].die(amount)
        
    def getDemand(self):
        return self.food_demand * self.population
   
    