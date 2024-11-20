from environment import *
from organism import *
class Producer(Organism):
    environment: Environment
    def __init__(self, name: str, env:Environment, pop: float):
        self.name = name
        self.population = pop
        self.environment = env
    
    def grow(self, amount):
        env = self.environment
        self.population = min(env.plantCap, int(self.population + amount))
    
    