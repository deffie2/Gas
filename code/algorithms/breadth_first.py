from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.classes.queue import Queue




def breadth_first_search_without_heur(initial_bord):
	# Create een queue om toestanden van het bord en bijbehorende moves te beheren
	queue = Queue
	# Bijhouden van welke bordtoestanden zijn al geweest, dit voorkont herhaling
	visited_state = set()

	# Zet het initial_bord in queue en ook de in visited_state
	queue.enqueue(initial_bord, [])
	visited_state.add(initial_bord)

	# Nu ga je checken als de queue niet leeg is
	while not queue.is_empty():
		# Get the current state from the queue and pop it
		current_board, path = queue.dequeue()

		# Check if the initial state is already a winning state
		if current_board.is_red_car_at_exit():
			return path

		# Genereer alle mogelijke zetten en voeg ze toe aan queue
		movable_vehicles, possible_moves = generate_all_possible_moves()

		for car_id in movable_vehicles:
			for move_direction, step_list in possible_moves[car_id]:
				for steps in step_list:
					# Maak een kopie van het bord en voer de zet uit
					new_board = current_board.copy_board()
					new_board.move_vehicle(car_id, move_direction, steps)

					# Controleer of de nieuwe toestand al is bezocht
					new_board_state = get_board_state(new_board)
					if new_board_state not in visited_state:
						visited_state.add(new_board_state)
						queue.enqueue(new_board, path.apppend([car_id, move_direction, steps]))

	return None
        



def breadth_first_search_with_heur():
	pass



