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


if __name__ == "__main__":

    # Check if the correct number of command-line arguments is provided.
    # If not, print usage instructions and exit the script.
    if len(sys.argv) < 5:
        print("Usage: script.py <game_number> <d> <algoritme> <runs> <shorest_path>")
        sys.exit(1)
    
    # Parse command-line arguments
    game_number = int(sys.argv[1])
    d = int(sys.argv[2])
    algorithm = sys.argv[3]
    runs = int(sys.argv[4])
    shorest_path = sys.argv[5]

#     --------------------------- Random --------------------------------------
    if shorest_path == "no":
        # Execute random algorithms based on command-line argument 'algorithm'
        if algorithm == "r" and shorest_path == "no":
            csv_names = move_car_random_WOH(d, game_number, runs)
        elif algorithm == "rh" and shorest_path == "no":
            csv_names = move_car_random_WH(d, game_number, runs)
            csv_names[0]

    # --------------------------- Breadth First -------------------------------
    # Perform breadth-first search on specified game board and dimensions
    if algorithm == "bf" and shorest_path == "no":
        solution = breadth_first_search(d, game_number, runs)
        

    # --------------------------- Beam Search   -------------------------------
    # Execute beam search algorithm on specified game board and dimensions
    if algorithm == "bs" and shorest_path == "no":
        solution = beam_search(d, game_number, runs)

    # --------------------------- Visualisation -------------------------------
    # Generate graphs or visualizations based on algorithm results
    if shorest_path == "no": 

        if algorithm == "r" or algorithm == "rh":
            frequency_graph(csv_names[0], csv_names[2])
            visualize(d, game_number, csv_names[1])

        elif algorithm == "bf" or "bs":
            visualize(d, game_number, solution)

    # --------------------------------------------------------------------------
    # Perform simulation for shortest path only
    if shorest_path == "yes":
        if algorithm == "r" or "rh":
            # Visualize shortest path for random with and withour heuristics
            name_data = str(input("What is the name of the dataset you wish to access? "))
            path = f'data/Random/Best_Moves_WOH/{name_data}'
            visualize(d, game_number, path)

        elif algorithm == "bf":
            # Visualize shortest path for breadth-first search
            path = f'data/Breadth_First/board_{game_number}_{d}X{d}.csv'
            visualize(d, game_number, path)

        elif algorithm == "bs":
            # Visualize shortest path for beam search
            name_data = str(input("What is the name of the dataset you wish to access? "))
            path = f'data/Beam_Search/{name_data}'
            visualize(d, game_number, path)
    