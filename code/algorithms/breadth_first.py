import copy


from code.classes.board import Board
from code.classes.queue import Queue


def breadth_first_search_without_heur(initial_bord):
	"""Het retourneert een lijst met alle possible_moves die het heeft gemaakt totdat de rode auto bij de exit is."""

	# Create een queue om toestanden van het bord en bijbehorende moves te beheren
	queue = Queue()
	# Bijhouden van welke bordtoestanden zijn al geweest, dit voorkont herhaling
	visited_state = set()

	# Zet het initial_bord in queue en ook de in visited_state
	queue.enqueue((initial_bord, []))
	visited_state.add(initial_bord)

	# Nu ga je checken als de queue niet leeg is
	while not queue.is_empty():
		# Get the current state from the queue and pop it
		current_board, path = queue.dequeue()

		# Check if the initial state is already a winning state
		if current_board.is_red_car_at_exit():
			return path

		# Verwerk de mogelijke zetten vanuit de huidige toestand van het bord
		process_moves(current_board, path, visited_state, queue)

	return None




def breadth_first_search_with_heur():
	pass



def process_moves(current_board, path, visited_state, queue):
    # Genereer alle mogelijke zetten voor de huidige toestand van het bord
    movable_vehicles, possible_moves = current_board.generate_all_possible_moves()

    for car_id in movable_vehicles:
        for move_direction, step_list in possible_moves[car_id]:
            for steps in step_list:
                # Maak een kopie van het bord en voer de zet uit
                new_board = copy.deepcopy(current_board)
                new_board.move_vehicle(car_id, move_direction, steps)

                new_board_state = new_board.get_board_state()
                new_board_hash = hash(new_board_state)

                # Controleer of de nieuwe toestand al is bezocht
                if new_board_hash not in visited_state:
                    visited_state.add(new_board_state)
                    new_path = path + [[car_id, move_direction, steps]]
                    queue.enqueue((new_board, new_path))

