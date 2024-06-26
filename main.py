import csv
import os
import time
import random
import sys

from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.algorithms.breadth_first import breadth_first_search
from code.algorithms.random import move_car_random_WH, move_car_random_WOH
from code.algorithms.beam_search import beam_search
from code.visualisation.visualise import frequency_graph
from code.visualisation.simulation import visualize

# from visualise import frequency_graph

if __name__ == "__main__":

    if len(sys.argv) < 6:
        print("Usage: script.py <game_number> <d> <algoritme> <runs> <shorest_path>")
        sys.exit(1)
    
    game_number = int(sys.argv[1])
    d = int(sys.argv[2])
    algorithm = sys.argv[3]
    runs = int(sys.argv[4])
    shorest_path = sys.argv[5]

    
#     --------------------------- Random --------------------------------------
    if shorest_path == "no":

        if algorithm == "r" and shorest_path == "no":
            csv_names = move_car_random_WOH(d, game_number, runs)
        elif algorithm == "rh" and shorest_path == "no":
            csv_names = move_car_random_WH(d, game_number, runs)
            csv_names[0]

    # --------------------------- Breadth First -------------------------------

    # Breadth-first search without heuristics applied to game boards 1, 2, 3, and 4.

    if algorithm == "bf" and shorest_path == "no":
        solution = breadth_first_search(d, game_number, runs)
        

    # --------------------------- Beam Search   -------------------------------

    if algorithm == "bs" and shorest_path == "no":
        solution = beam_search(d, game_number, runs)

    # --------------------------- Visualisation -------------------------------

    # Graps

    if shorest_path == "no": 

        if algorithm == "r" or algorithm == "rh":
            frequency_graph(csv_names[0], csv_names[2])
            visualize(d, game_number, csv_names[1])

        # Simulation

        elif algorithm == "bf":
            visualize(d, game_number, solution)

        elif algorithm == "bs":
            visualize(d, game_number, solution)


    # --------------------------------------------------------------------------
    # shorest path only simulation

    if shorest_path == "yes":

        if algorithm == "r":
            name_data = str(input("What is the name of the dataset you wish to access? "))
            path = f'data/Random/Best_Moves_WOH/{name_data}'
            visualize(d, game_number, path)

        elif algorithm == "rh":
            name_data = str(input("What is the name of the dataset you wish to access? "))
            path = f'data/Random/Best_Moves_WH/{name_data}'
            visualize(d, game_number, path)

        elif algorithm == "bf":
            path = f'data/Breadth_First/board_{game_number}_{d}X{d}.csv'
            visualize(d, game_number, path)

        elif algorithm == "bs":
            name_data = str(input("What is the name of the dataset you wish to access? "))
            path = f'data/Beam_Search/{name_data}'
            visualize(d, game_number, path)








    