import random


from ..classes.board import Board


def move_car_random(board):
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

    # Move the vehicle to the new position
    board.move_vehicle(movable_vehicle, move_direction, step)

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
