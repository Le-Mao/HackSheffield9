class Organism:
    population: int = 0
    name:str
    
    def cull(self, ratio:float):
        self.die(ratio * self.population)
        
    def die(self, amount:int):
        self.population = max(0, int(self.population - amount))