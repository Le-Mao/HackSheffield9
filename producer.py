from environment import *
class Producer:
    population: int = 0
    environment: Environment
    name: str
    def __init__(self, name: str, env:Environment, pop: float):
        self.name = name
        self.population = pop
        self.environment = env
    
    def grow(self, amount):
        env = self.environment
        self.population = min(env.plantCap, int(self.population + amount))
    
    def cull(self, ratio:float):
        self.die(ratio * self.population)
        
    def die(self, amount:int):
        self.population = max(0, int(self.population - amount))