from representatie import Board
from randomise import move_car_random

import csv


from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.algorithms.breadth_first import (
    breadth_first_search_without_heur, 
    breadth_first_search_with_heur
)
from code.algorithms.random import move_car_random
from code.visualisation import frequency_graph



if __name__ == "__main__":


    # --------------------------- Random --------------------------------------
    # from sys import argv

    # # Load the requested game or else game 1
    # if len(argv) == 1:
    #     game_number = "1"
    # elif len(argv) == 2:
    #     game_number = argv[1]
    
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

    #     if i == 0:
    #         best_moves = moves

    #     if best_moves >= moves:
    #         best_moves = moves
    #         best_moves_list = board.move_history
    #     board.move_history = []

    # # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
    # with open(f'data/Freq_moves_table/Random/'
    #           f'r_freq_move_{game_number}_{d}x{d}.csv',
    #           mode='w', newline='') as file:
    #     writer = csv.writer(file)
            
    #     for list in moveslist:
    #         writer.writerow([list])

    # # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
    # with open(f'data/Best_moves_table/Random/'
    #           f'r_best_move_{game_number}_{d}x{d}.csv',
    #           mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Car', 'Move direction', 'Step'])

    #     for list in best_moves_list:
    #         writer.writerow(list)


    # --------------------------- Breadth First -------------------------------

    game_number = 
    board = Board(6, game_number)  # Maak het bord aan zoals je al doet
    
    # Voer het BFS-algoritme uit om de oplossing te vinden
    solution = breadth_first_search(board)
    
    if solution:
        d = board.dimension

        file_path = f'data/Best_moves_table/breadth_first/r_best_move_{game_number}_{d}x{d}.csv'

        with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Move direction', 'Step'])

        # Opslaan van elke move in de oplossing naar het CSV-bestand
        for move in solution:
            writer.writerow(move)
    
        print(f"Moves successfully saved to {file_path}")
    else:
        print("No solution found.")
        



    # # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
    # with open(f'data/Freq_moves_table/Random/'
    #           f'r_freq_move_{game_number}_{d}x{d}.csv',
    #           mode='w', newline='') as file:
    #     writer = csv.writer(file)
            
    #     for list in moveslist:
    #         writer.writerow([list])

    # # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
    # with open(f'data/Best_moves_table/Random/'
    #           f'r_best_move_{game_number}_{d}x{d}.csv',
    #           mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Car', 'Move direction', 'Step'])

    #     for list in best_moves_list:
    #         writer.writerow(list)

    # --------------------------- Visualisation -------------------------------

    #graphs 
    