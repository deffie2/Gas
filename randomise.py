import random
from representatie import Board


def move_car_random(board):
	# Update the empty spaces and movable vehicles
    board.empty_places()
    board.vehicles_moveable()

    # Calculate the possible moves
    possible_moves = board.possible_sets()
    print(possible_moves)

    # Randomly select a vehicle that can move
    movable_vehicle = random.choice(list(board.movable_vehicles))

    print(movable_vehicle)

    # Get possible moves for the selected vehicle
    possible_vehicle_moves = possible_moves.get(movable_vehicle, [])
    print(possible_vehicle_moves)

    # Randomly select a possible move for the selected vehicle
    move_direction, move_steps = random.choice(possible_vehicle_moves)

    # Randomly select a step in the selected direction
    step = random.choice(move_steps)

    # Move the vehicle to the new position
    board.move_vehicle(movable_vehicle, move_direction, step)

    # Print the board after the move
    board.printboard()

    return












    


