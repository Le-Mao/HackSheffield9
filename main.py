from environment import *
from animal import *
from producer import *
from plot import *

def initialise():
    env = Environment(1.2, 300)
    plant = Producer("plant", env, 100)
    moose = Animal("moose", 100, 1, 0.7, 2)
    wolves = Animal("wolf", 100, 0.3, 0.3, 1.5)
    humans = Animal("human", 10, 0.25, 0.1, 1.3)
    moose.food_sources = [plant]
    wolves.food_sources = [moose]
    humans.food_sources = [plant, moose, wolves]
    animals = [moose, wolves, humans]
    plants = [plant]
    return ({}, env, plants, animals)






NUM_ITERATIONS = 30
DEATH_RATE = 0.9

def main():
    for i in range(NUM_ITERATIONS):
        # only print time to console, x axis reps time in the graphs
        print("Iteration t =", i) 
        do_iteration()
    return toFrame(data)

def do_iteration():
        for plant in plants:
            output("Plant population", plant.population, data)
        for animal in animals:
            output(animal.name + " population", animal.population, data)

        for plnt in plants:
            plnt.grow(env.plantGrowthRate * plnt.population)
        
        for animal in animals:
            demand = animal.getDemand()
            total_food = 0
            for food in animal.food_sources:
                total_food += food.population
            available = total_food * animal.feedstock_utilisation

            if available > demand:
                excess = available - demand
                # grow based on how much excess food there is
                animal.grow(animal.population*(animal.growthRate-1))
                # eat based on new damand
                animal.eat(min(available, demand*animal.growthRate))
            
            if available < demand:
                # kill amount based on amount missing per demand
                animal.cull(DEATH_RATE * (demand-available)/demand)

(data, env, plants, animals) = initialise()
main()