import random
from representatie import Board


def move_car_random(board):
	# Update the empty spaces and movable vehicles
    board.empty_places()
    board.vehicles_moveable()

    # Calculate the possible moves
    possible_moves = board.possible_sets()

    # Randomly select a vehicle that can move
    movable_vehicle = random.choice(list(board.movable_vehicles))

    # Get possible moves for the selected vehicle
    possible_vehicle_moves = possible_moves.get(movable_vehicle, [])

    # Combine all possible steps for all directions
    all_possible_steps = []
    for move_direction, move_steps in possible_vehicle_moves:
        for step in move_steps:
            all_possible_steps.append((move_direction, step))

  # Randomly select a step from all possible steps
    move_direction, step = random.choice(all_possible_steps)

    # Move the vehicle to the new position
    board.move_vehicle(movable_vehicle, move_direction, step)

    # Print the board after the move
    board.printboard()

    return








    


