import random
import csv


from code.classes.board import Board


def move_car_random_WOH(board, runs):

    game_number = board.game_number
    d = board.dimension

    moveslist = []
    for i in range(runs):

        moves = 0
        while not (board.is_red_car_at_exit()):
            # Select a random move
            movable_vehicle, possible_vehicle_moves = select_random_move(board)

            # Combine all possible steps for all directions
            all_possible_steps = combine_possible_steps(possible_vehicle_moves)

            # Randomly select a step from all possible steps
            move_direction, step = random.choice(all_possible_steps)

            # Move the vehicle to the new position
            board.move_vehicle(movable_vehicle, move_direction, step)
            moves += 1
        print(f"Board {game_number} took {moves} moves")
        moveslist.append(moves)

        if i == 0:
            best_moves = moves

            if best_moves >= moves:
                best_moves = moves
                best_moves_list = board.move_history
            board.move_history = []

    csv_namen = []
    with open(f'data/Random/Freq_moves_WOH/board_{game_number}_{runs}_freq_move_WOH_{d}x{d}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        for list in moveslist:
            writer.writerow([list])
    csv_namen.append("data/Random/Freq_moves_WOH/board_{game_number}_{runs}_freq_move_WOH_{d}x{d}.csv")


    with open(f'data/Random/Best_Moves_WOH/board_{game_number}_{runs}_Best_moves_WOH_{d}x{d}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Move direction', 'Step'])

        for list in best_moves_list:
            writer.writerow(list)
    csv_namen.append("data/Random/Best_Moves_WOH/board_{game_number}_{runs}_Best_moves_WOH_{d}x{d}.csv")
    csv_namen.append("WOH")

    return csv_namen


def move_car_random_WH(board, runs):

    game_number = board.game_number
    d = board.dimension

    moveslist = []
    for i in range(runs):
        moves = 0
        while not (board.is_red_car_at_exit()):
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
            moves += 1
        print(f"Board {game_number} took {moves} moves")
        moveslist.append(moves)

        if i == 0:
            best_moves = moves

            if best_moves >= moves:
                best_moves = moves
                best_moves_list = board.move_history
            board.move_history = []

    csv_namen = []
    with open(f'data/Random/Freq_moves_WH/board_{game_number}_{runs}_freq_move_WH_{d}x{d}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        for list in moveslist:
            writer.writerow([list])
    csv_namen.append("data/Random/Freq_moves_WH/board_{game_number}_{runs}_freq_move_WH_{d}x{d}.csv")

    # !!! Verander 'r' in 'b' als je met Breadth werkt!!!!
    with open(f'data/Random/Best_Moves_WH/board_{game_number}_{runs}_Best_moves_WH_{d}x{d}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Move direction', 'Step'])

        for list in best_moves_list:
            writer.writerow(list)
    csv_namen.append("data/Random/Best_Moves_WH/board_{game_number}_{runs}_Best_moves_WH_{d}x{d}.csv")
    csv_namen.append("WH")

    return csv_namen

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

