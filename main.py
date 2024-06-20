import csv
import os
import time
import random
import sys

from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.algorithms.breadth_first import breadth_first_search
from code.algorithms.random import move_car_random_WH, move_car_random_WOH
from code.visualisation.visualise import frequency_graph

# from visualise import frequency_graph

if __name__ == "__main__":

    # from sys import argv

    # Load the requested game or else game 1
    # if len(argv) == 1:
    #     game_number = "1"
    # elif len(argv) == 2:
    #     game_number = argv[1]
    
    # if len(argv) == 3:
    #     d= argv[3]

    if len(sys.argv) < 4:
        print("Usage: script.py <game_number> <d> <algoritme> <runs>")
        sys.exit(1)
    
    game_number = int(sys.argv[1])
    d = int(sys.argv[2])
    algorithm = sys.argv[3]
    runs = int(sys.argv[4])
    visualise= sys.argv[5]

    
#     --------------------------- Random --------------------------------------
    
    if algorithm == "r":
        csv_names = move_car_random_WOH(d, game_number, runs)
    elif algorithm == "rh":
        csv_names = move_car_random_WH(d, game_number, runs)
        print(csv_names)
        csv_names[0]

    # --------------------------- Breadth First -------------------------------

    # Breadth-first search without heuristics applied to game boards 1, 2, 3, and 4.

    if algorithm == "bf":
        solution = breadth_first_search(d, game_number, runs)
        print(solution)

    

    # --------------------------- Beam Search   -------------------------------

    if algorithm == "bs":
        solution = beam_search(d, game_number, runs)
        print(solution)


    # --------------------------- Visualisation -------------------------------

    # Graps

    if visualise == "v" and (algorithm == "r" or algorithm == "rh"):
        frequency_graph(csv_names[0], csv_names[2])

    # Simulation

    elif visualise == "v" and algorithm == "b":
        print("hello")

    elif visualise == "v" and algorithm == "bs":
        print(hello)


    