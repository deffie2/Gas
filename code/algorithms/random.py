import random


from code.classes.board import Board


def move_car_random_WOH(board):
	# Select a random move
    movable_vehicle, possible_vehicle_moves = select_random_move(board)

    # Combine all possible steps for all directions
    all_possible_steps = combine_possible_steps(possible_vehicle_moves)

    # Randomly select a step from all possible steps
    move_direction, step = random.choice(all_possible_steps)

    # Move the vehicle to the new position
    board.move_vehicle(movable_vehicle, move_direction, step)

    # print()
    # board.printboard()
    # print()


def move_car_random_WH(board):
    # Select a random move
    movable_vehicle, possible_vehicle_moves = select_random_move(board)

    # Combine all possible steps for all directions
    all_possible_steps = combine_possible_steps(possible_vehicle_moves)

    # Randomly select a step from all possible steps
    move_direction, step = random.choice(all_possible_steps)

    if not (board.heuri_red_clear_exit()):
        # Move the vehicle to the new position
        board.move_vehicle(movable_vehicle, move_direction, step)
    else:
        board.heuri_get_red_to_exit()




def select_random_move(board):
    # Generate all possible moves
    movable_vehicles, possible_moves = board.generate_all_possible_moves()

    # Randomly select a vehicle that can move
    movable_vehicle = random.choice(list(movable_vehicles))

    # Get possible moves for the selected vehicle
    possible_vehicle_moves = possible_moves.get(movable_vehicle, [])

    return movable_vehicle, possible_vehicle_moves


def combine_possible_steps(possible_vehicle_moves):
    all_possible_steps = []
    for move_direction, move_steps in possible_vehicle_moves:
        for step in move_steps:
            all_possible_steps.append((move_direction, step))
    return all_possible_steps

# for d, game_number in gameboards_list:
#         file_path1 = f'.data/Random/Freq_moves_WOH/{game_number}_freq_move_{d}x{d}.csv'
#         file_path2 = f'.data/Random/Best_Moves_WOH/{game_number}_best_move_{d}x{d}.csv'
#         file_path3 = f'.data/Random/Freq_moves_WH/{game_number}_freq_move_{d}x{d}.csv'
#         file_path4 = f'.data/Random/Best_Moves_WH/{game_number}_best_move_{d}x{d}.csv'

#         moveslist = []
#         for i in range(1000):
#             board = Board(d, game_number)
#             moves = 0
#             while not (board.is_red_car_at_exit()):
#                 move_car_random(board)
#                 moves += 1
#             print(f"Board {game_number} took {moves} moves")
#             moveslist.append(moves)

#             if i == 0:
#                 best_moves = moves

#             if best_moves >= moves:
#                 best_moves = moves
#                 best_moves_list = board.move_history
#             board.move_history = []

#         # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
#         with open(file_path_1, mode='w', newline='') as file:
#             writer = csv.writer(file)
                
#             for list in moveslist:
#                 writer.writerow([list])

#         # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
#         with open(file_path2, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Car', 'Move direction', 'Step'])

#             for list in best_moves_list:
#                 writer.writerow(list)

