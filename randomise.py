
# in the main
board = Board(6)

while True:
	board.places_car()
	board.printboard()
	move_car_random(board.VehicleDict, board.dimension)


import random
from node import Node


def move_car_random(vehicle_dict, dimension):

    # List of available cars
    available_cars = list(vehicle_dict.keys())

    vehicle_moved = True
    car_id = None

    while vehicle_moved:

	    # Choose a random car
	    car_id = random.choice(available_cars)

	    # Get only the value of car_moved from the tuple stored in vehicle_dict[car_id]
	    vehicle_moved = None
	    for value in vehicle_dict[car_id]:
	        if isinstance(value, bool):
	            vehicle_moved = value
	            break

	car_movement = False
	while not car_movement:
		# Kies een random getal om aantal v erplaatsingen
		move_count = random.choice(list(range(1, dimension, + 1)))

		if car_orientation == 'H':
			# can move left or right
			possible_direction = ["left", "right"]
			move_direction = random.choice(possible_direction)

			# Check if move_direction is possible
			car_movement = is_move_possible(move_count, move_direction, vehicle_dict, car_id)

			# Update the vehicle dictionary
			if car_movement == True:
				node.update_vehicle_status(car_id)

		elif car_orientation == 'V':
			# can move up or down
			possible_direction = ["up", "down"]
			move_direction = random.choice(possible_direction)

			# Check if move_direction is possible
			car_movement = is_move_possible(move_count, possible_direction, move_direction)

			# Update the vehicle dictionary
			if car_movement == True:
				node.update_vehicle_status(car_id)

	return 


def is_move_possible(move_count, move_direction, vehicle_dict, car_id):
	if move_direction == "left":
		car_orientation, car_col, car_row, car_length, _ = vehicle_dict[car_id]
		new_col = car_col - move_count
		## Check if the new position is within the bounds of the board
		if new_col >= 1:
			for carkey, carvalues in vehicle_dict.items():
				if carkey != car_id:
					 other_orientation, other_col, other_row, other_length, _ = carvalues
					 # Check if there is a horizontally oriented car in the same row
					 if other_orientation == 'H' and other_row == car_row:
					 	# Check for a collision if the cars overlap horizontally
					 	if new_col <= other_col + other_length - 1:
					 		return False
					 elif other_orientation == 'V':
					 	# Check for a collision if the cars overlap vertically
					 	if car_row == other_row and new_col == other_col:
					 		return false
					 	# Check if there is a vertically oriented car in the path of the moving car
					 	if new_col == other_col
						 	vertical_vehicle_positions= []
							for i in range(1, other_length):
							    vertical_vehicle_positions.append(other_row + i)
							if car_row in vertical_vehicle_positions:
								return False
			return True
		return False


	elif move_direction == "right":
		car_orientation, car_col, car_row, car_length, _ = vehicle_dict[car_id]
		new_col = car_col + move_count
		# Check if the new position is within the bounds of the board
		if new_col <= board.dimension - car_length + 1
			for carkey, carvalues in vehicle_dict.items():
				if carkey != car_id:
					 other_orientation, other_col, other_row, other_length, _ = carvalues
					 # Check if there is a horizontally oriented car in the same row
					 if other_orientation == 'H' and other_row == car_row:
					 	# Check for a collision if the cars overlap horizontally
					 	if new_col + car_length - 1 >= other_col:
					 		return False
					 elif other_orientation == 'V':
					 	# Check for a collision if the cars overlap vertically
					 	if car_row == other_row and new_col == other_col:
					 		return false
					 	# Check if there is a vertically oriented car in the path of the moving car
					 	if new_col == other_col
						 	vertical_vehicle_positions= []
							for i in range(1, other_length):
							    vertical_vehicle_positions.append(other_row + i)
							if car_row in vertical_vehicle_positions:
								return False
			return True
		return False


	elif move_direction == "up":
		car_orientation, car_col, car_row, car_length, _ = vehicle_dict[car_id]
		new_row = car_row - move_count
		# Check if the new position is within the bounds of the board
		if new_row >= 1:
			for carkey, carvalues in vehicle_dict.items():
				if carkey != car_id:
					 other_orientation, other_col, other_row, other_length, _ = carvalues
					 # Check if there is a horizontally oriented car in the same row
					 if other_orientation == 'H':
					 	# Check for a collision if the cars overlap horizontally
					 	if new_row == other_row and car_col == other_col:
					 		return false
					 	if new_row == other_row
						 	horizontal_vehicle_positions= []
							for i in range(1, other_length):
							    vertical_vehicle_positions.append(other_col + i)
							if car_col in horizontal_vehicle_positions:
								return False
						# Check if there is a vertically oriented car in the same column
						elif other_orientation == 'V' and car_col == other_col:
					 	# Check for a collision if the cars overlap vertically
					 		if new_row <= other_row + other_length - 1:
					 			return False					 	
			return True
		return False

	elif move_direction == "down":
		car_orientation, car_col, car_row, car_length, _ = vehicle_dict[car_id]
		new_row = car_row + move_count
		# Check if the new position is within the bounds of the board
		if new_row <= board.dimension - car_length + 1 :
			for carkey, carvalues in vehicle_dict.items():
				if carkey != car_id:
					 other_orientation, other_col, other_row, other_length, _ = carvalues
					 # Check if there is a horizontally oriented car in the same row
					 if other_orientation == 'H':
					 	# Check for a collision if the cars overlap horizontally
					 	if new_row == other_row and car_col == other_col:
					 		return false
					 	if new_row == other_row
						 	horizontal_vehicle_positions= []
							for i in range(1, other_length):
							    vertical_vehicle_positions.append(other_col + i)
							if car_col in horizontal_vehicle_positions:
								return False
						# Check if there is a vertically oriented car in the same column
						elif other_orientation == 'V' and car_col == other_col:
					 	# Check for a collision if the cars overlap vertically
					 		if new_row + car_length - 1  >= other_row
					 			return False					 	
			return True
		return False






    


