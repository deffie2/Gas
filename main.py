import csv
import os
import time
import random
import sys

from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.algorithms.breadth_first import (
    breadth_first_search_without_heur
)
from code.algorithms.random import move_car_random_WH, move_car_random_WOH
from visualise import frequency_graph
# from code.visualisation import frequency_graph

# from natsort import natsorted


if __name__ == "__main__":

    # List of gameboards with dimensions and game numbers
    gameboards_list = [(6, 1), (6, 2), (6, 3), (9, 4), (9, 5), (9, 6), (12, 7)]


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

    board = Board(d, game_number)

    if algorithm == "r":
        csv_names = move_car_random_WOH(board, runs)
    elif algorithm == "rh":
        csv_names = move_car_random_WH(board, runs)
        print(csv_names)
        csv_names[0]
    
    if visualise == "v":
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

    # game_number = 4
    # d = 9

    # file_path1 = f'.data/Random/Freq_moves_WOH/{game_number}_freq_move_{d}x{d}.csv'
    # file_path2 = f'.data/Random/Best_Moves_WOH/{game_number}_best_move_{d}x{d}.csv'
    # file_path3 = f'.data/Random/Freq_moves_WH/{game_number}_freq_move_{d}x{d}.csv'
    # file_path4 = f'.data/Random/Best_Moves_WH/{game_number}_best_move_{d}x{d}.csv'
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

    ## Random Function without any heuristics 
            #move_car_random(board, move, d, game_number,d)

    # for d, game_number in gameboards_list:
    #     file_path1 = f'.data/Random/Freq_moves_WOH/{game_number}_freq_move_{d}x{d}.csv'
    #     file_path2 = f'.data/Random/Best_Moves_WOH/{game_number}_best_move_{d}x{d}.csv'
    #     file_path3 = f'.data/Random/Freq_moves_WH/{game_number}_freq_move_{d}x{d}.csv'
    #     file_path4 = f'.data/Random/Best_Moves_WH/{game_number}_best_move_{d}x{d}.csv'

    #     moveslist = []
    #     for i in range(1000):
    #         board = Board(d, game_number)
    #         moves = 0
    #         while not (board.is_red_car_at_exit()):
    #             move_car_random_WOH(board)
    #             moves += 1
    #         print(f"Board {game_number} took {moves} moves")
    #         moveslist.append(moves)

    #         if i == 0:
    #             best_moves = moves

    #         if best_moves >= moves:
    #             best_moves = moves
    #             best_moves_list = board.move_history
    #         board.move_history = []

    #     if i == 0:
    #         best_moves = moves


    #     if best_moves >= moves:
    #         best_moves = moves
    #         best_moves_list = board.move_history
    #     board.move_history = []

    # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
    # os.makedirs(os.path.dirname(f'.data/Random/Freq_moves_WOH/{game_number}_freq_move_{d}x{d}.csv'), exist_ok=True)
    # with open(f'data/Random/Freq_moves_WH/{game_number}_freq_move_{d}x{d}.csv', mode='w', newline='') as file:
    #     writer = csv.writer(file)
            
    #     for list in moveslist:
    #         writer.writerow([list])

    # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
    # os.makedirs(os.path.dirname(file_path2), exist_ok=True)
    # with open(f'data/Random/Best_Moves_WH/{game_number}_best_move_{d}x{d}.csv', mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Car', 'Move direction', 'Step'])

    #     for list in best_moves_list:
    #         writer.writerow(list)

    

#     # Random Function with heuristics


# ##. van Charlotte aangepast
#     runs = 1
#     moveslist = []
#     d = 6
#     game_number = 1
#     # All the runs
#     for i in range(runs):
#         board = Board(d, game_number)
#         board.places_car()
#         moves = 0
#         # A single run
#         while not (board.is_red_car_at_exit()):
#             move_car_random(board)
#             moves += 1
#         print(f"Board {game_number} took {moves} moves")
#         moveslist.append(moves)

# #. van Charlotte aangepast

#     moveslist = []
#     # All the runs
#     for i in range(runs):
#         board = Board(d, game_number)
#         board.places_car()
#         moves = 0
#         # A single run
#         while not (board.is_red_car_at_exit()):
#             move_car_random_with_heuri(board)
#             moves += 1
#         print(f"Board {game_number} took {moves} moves")
#         moveslist.append(moves)


#     ##

#         if i == 0:
#             best_moves = moves




    # --------------------------- Breadth First -------------------------------

    # Breadth-first search without heuristics applied to game boards 1, 2, 3, and 4.
    #gameboards_list = [(6, 1)] #(6, 2), (6, 3), (9, 4)

    # for d, game_number in gameboards_list:


    # game_number = 4
    # d = 9    
    # board = Board(d, game_number)
    
    # file_path5 = f'./data/Breadth_First/Best_Moves_WOH/{game_number}_{d}x{d}.csv'

    # # Voer het BFS-algoritme uit om de oplossing te vinden
    # solution = breadth_first_search_without_heur(board)
    
    # if solution:

    #     # Open het bestand voor schrijven ('w' modus, overschrijven als het bestaat)
    #     os.makedirs(os.path.dirname(file_path5), exist_ok=True)
    #     with open(file_path5, mode='w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(['Car', 'Move direction', 'Step'])
    #         for move in solution:
    #             writer.writerow(move)
    #         print(f"Moves successfully saved to {file_path5}")
    # else:
    #     print("No solution found.")

    # # Breadth-first search with early constraint checking applied to game boards 4, 5, 6 en 7.
    # gameboards_list = [(9, 5), (9, 6), (12, 7)]
    # constraint_number = 2000000

    # for d, game_number in gameboards_list:
    #     file_path6 = f'./data/Breadth_First/Best_Moves_ECC/{game_number}_{d}x{d}.csv'
    #     board = Board(d, game_number)
    #     board.printboard()
    #     print(d)
    #     print(game_number)

    #     solution = breadth_first_search_with_early_constraints(board, constraint_number)

    #     if solution:

    #         # Open het bestand voor schrijven ('w' modus, overschrijven als het bestaat)
    #         os.makedirs(os.path.dirname(file_path6), exist_ok=True)
    #         with open(file_path6, mode='w', newline='') as file:
    #             writer = csv.writer(file)
    #             writer.writerow(['Car', 'Move direction', 'Step'])
    #             for move in solution:
    #                 writer.writerow(move)
    #             print(f"Moves successfully saved to {file_path6}")
    #     else:
    #         print("No solution found.")




    # --------------------------- Visualisation -------------------------------

    #graphs 
    