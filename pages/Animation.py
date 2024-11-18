import streamlit as st
import pandas as pd
import numpy as np
import time
import random
from math import sin, cos, pi
import main

from environment import *
from herbivore import *

MAX_SHOWN_ON_MAP = 500


def get_random_positions_in_sheffield(n, max):
    numpreysToDisplay = int(min(n, max))
    positions = np.random.randn(numpreysToDisplay, 2) / [50,50] + [53.38, -1.4786]
    return positions

def displayRandomOnMap(prey_population, title, size, colour):
    df = pd.DataFrame(
        get_random_positions_in_sheffield(prey_population, MAX_SHOWN_ON_MAP), columns = ["lat", "lon"]
    )
    st.write(title)
    st.map(df, zoom=11, size=size, color=colour)

def displayOnMap(prey_positions, size, colour):
    df = pd.DataFrame(
        prey_positions, columns = ["lat", "lon"]
    )
    return st.map(df, zoom=11, size=size, color=colour)

def get_offset_positions(prey_positions, predator_population):
    n = min(prey_positions.shape[0], predator_population)
    pairs = []
    for i in range(n):
        angle = random.random() * 2 * pi 
        pairs.append(
            [cos(angle)*0.0001 + prey_positions[i][0], sin(angle)*0.0001 + prey_positions[i][1]])
    return pairs


def eatpreysOnMap(prey_population, predator_population, prey_size, prey_colour, predator_colour, prey_name, predator_name):
    st.write(f"## {MAX_SHOWN_ON_MAP if prey_population > MAX_SHOWN_ON_MAP else prey_population} wild {prey_name}s are roaming Sheffield.")
    prey_positions = get_random_positions_in_sheffield(prey_population, MAX_SHOWN_ON_MAP)
    map = displayOnMap(prey_positions, prey_size, prey_colour)

    time.sleep(5)

    predator_positions = get_offset_positions(prey_positions, predator_population)

    map.empty()

    
    
    print("Prey Positions : ", prey_positions, "length = ", len(prey_positions), "\n\n")
    print("Predator Positions", predator_positions, "length = ", len(predator_positions), "\n\n")
    combined_array = np.transpose(np.append(prey_positions, predator_positions, axis=0))
    print("Combined array", combined_array, "\n\n")

    colours = []
    for i in range(int(prey_population)):
        colours.append(prey_colour)
    for i in range(int(len(combined_array[0]) - prey_population)):
        colours.append(predator_colour)


    print("Colours", colours, "length = ", len(colours))

    print("Length of latitudes : ", len(combined_array[0]))
    print("Length of latitudes : ", len(combined_array[1]))
    combined_frame = pd.DataFrame( 
        {
        "latitudes" : combined_array[0],
        "longitudes" : combined_array[1],
        "colours" : colours
        }
    )
    st.write(f"But they may not enjoy the city in peace for long, for {MAX_SHOWN_ON_MAP if predator_population > MAX_SHOWN_ON_MAP else prey_population} {predator_name}s have made the city their home.")
    map = st.map(combined_frame, latitude="latitudes", longitude="longitudes", color="colours")
    time.sleep(5)
    map.empty()
    if predator_population < prey_population:
        remaining_preys = []
        for i in range(int(predator_population), int(prey_population)):  #this feels wrong but it works, so it might create an error later
            remaining_preys.append(prey_positions[i])
        st.write(f"They strike the young, the elderly and the weak, when their guard is down, carrying away their prey into the cold, dark night. The surviving {prey_name}s live to reproduce.")
        map = displayOnMap(remaining_preys, prey_size, prey_colour)
    else: 
        st.write(f"The hunger of the {predator_name}s is insatiable. The {prey_name} population of Sheffield has been rendered extinct. However, enterprising individuals from Derbyshire and Rotherham are sure to fill the ecological niche before the year is out.")
        map = displayOnMap(predator_positions, 1, predator_colour)

def doIterationAndDisplay():
    last_iteration = main.do_iteration()
    eatpreysOnMap(main.plant.population, main.moose.population, 1, "#00ff00", "#4d2c1f", main.plant.name, main.moose.name)


st.button(label="Do Next Iteration", on_click=doIterationAndDisplay )

doIterationAndDisplay()