import csv
import os
import time
import random
import sys

from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.algorithms.breadth_first import breadth_first_search
from code.algorithms.random import move_car_random_WH, move_car_random_WOH
from visualise import frequency_graph
# from code.visualisation import frequency_graph


if __name__ == "__main__":

    
#     --------------------------- Random --------------------------------------

#     ####################################################################
    # Voor testen

    # from sys import argv

    # Load the requested game or else game 1
    # if len(argv) == 1:
    #     game_number = "1"
    # elif len(argv) == 2:
    #     game_number = argv[1]
    
    # if len(argv) == 3:
    #     d= argv[3]

    if len(sys.argv) < 5:
        print("Usage: script.py <game_number> <d> <algoritme> <runs>")
        sys.exit(1)
    
    game_number = int(sys.argv[1])
    d = int(sys.argv[2])
    algorithm = sys.argv[3]
    runs = int(sys.argv[4])
    visualise= sys.argv[5]

    # board = Board(d, game_number)

    if algorithm == "r":
        csv_names = move_car_random_WOH(d, game_number, runs)
    elif algorithm == "rh":
        csv_names = move_car_random_WH(d, game_number, runs)
        print(csv_names)
        csv_names[0]
    
    if visualise == "v" and (algorithm == "r" or algorithm == "rh"):
        frequency_graph(csv_names[0], csv_names[2])

    # # asking dimension
    # d = int(input("What is the dimension? "))

    # # asking how many runs
    # runs = int(input("How many times do you want to run the simulation? "))

    # best_moves = None
    # current_moves = 0
    # best_moves_list = []

    # moveslist = []
    # # All the runs
    # for i in range(runs):
    #     board = Board(d, game_number)
    #     board.places_car()
    #     moves = 0
    #     # A single run
    #     while not (board.is_red_car_at_exit()):
    #         move_car_random(board)
    #         moves += 1
    #     print(f"Board {game_number} took {moves} moves")
    #     moveslist.append(moves)

#     #######################################################################

    # Random Function without any heuristics
    # Seed instellen voor reproduceerbare resultaten
    # random.seed(42)

    # start = time.time()

    #moveslist = []
    # while time.time() - start < 300:
    # for i in range(1000):
    #     board = Board(d, game_number)
    #     board.printboard()
    #     moves = 0
    #     while not (board.is_red_car_at_exit()):
    #         # if start == 60:
    #         #     end = time.time() - start
    #         move_car_random_WH(board)
    #         moves += 1
    #     print(f"Board {game_number} took {moves} moves")
    #     moveslist.append(moves)


    #######################################################################



    # --------------------------- Breadth First -------------------------------

    # Breadth-first search without heuristics applied to game boards 1, 2, 3, and 4.

    if algorithm == "b":
        solution = breadth_first_search(d, game_number, runs)
        print(solution)

    if visualise == "v" and algorithm == "b":
        print("hello")



    # --------------------------- Visualisation -------------------------------

    #graphs 
    