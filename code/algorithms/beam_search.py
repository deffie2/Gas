# from code.classes.board import Board
# from code.classes.priorityqueue import PriorityQueue
import sys
sys.path.append("../classes")
from board import Board
from priorityqueue import PriorityQueue

from typing import List

def beam_search(d, game_number, runs):
	"""
    Perform beam search on the given initial board to find a path
    where the red car reaches the exit.
    """

    beam_width = int(input("What value would you like for the beam width? "))
   	csv_name = None
    for i in range(runs):
        initial_board = Board(d, game_number)
        
        # Initialize the priority queue and parents dictionary for the search
        pq, parents = initialize_search(initial_board)

        while not pq.is_empty():
            # Get the current state from the priority queue
            current_board = pq.pop()

            # Check if the current state is a winning state
            if current_board.is_red_car_at_exit():
                pq.clear()
                solution = reconstruct_path(parents, hash(current_board))
                
                # Save the solution to the CSV file
                csv_name = save_solution_to_csv(solution, d, game_number)
                break  # Break after finding the solution for this run

            # Process the possible moves from the current board state
            process_moves(current_board, pq, parents, beam_width)

    if csv_name:
        return csv_name
    return None


def calculate_heuristic(board):
	pass


def initialize_search(initial_board):
    """Initializes the priority queue and parents dictionary for the search."""
    pq = PriorityQueue()
    parents = {}

    # Enqueue the initial board with its heuristic value
    heuristic_value = calculate_heuristic(initial_board)
    pq.push(initial_board, heuristic_value)
    initial_state = hash(initial_board)
    parents[initial_state] = None

    return priority_queue, parents


def process_moves(current_board: Board, pq: PriorityQueue, parents: dict, beam_width: int):
    """
    Generate and process all possible moves from the current board state.

    """
    movable_vehicles, possible_moves = current_board.generate_all_possible_moves()
    next_states = []

    for car_id in movable_vehicles:
        for move_direction, step_list in possible_moves[car_id]:
            for steps in step_list:
                # Maak een kopie van het bord en voer de zet uit
                #new_board = copy.deepcopy(current_board)
                new_board = current_board.move_vehicle(car_id, steps)
                
                # BEAM: Geef elk nieuw bord een waarde
                    # -> Gebeurd met heuristics functie
                heuristic_value = calculate_heuristic(new_board)

                # Sla het nieuwe bord en de heuristische waarde op in een lijst
                new_board_state = hash(new_board.get_board_state())
                if new_board_state not in parents:
                	next_states.append((heuristic_value, new_board, car_id, steps))

  	# Sorteer de volgende toestanden op basis van heuristische waarde
  	next_states.sort(key=lambda x: x[0], reverse=True)

  	# Voeg de beste beam_width toestanden toe aan de prioriteitswachtrij
    for heuristic_value, new_board, car_id, steps in next_states[:beam_width]:
        new_board_state = hash(new_board.get_board_state())
        if new_board_state not in parents:
            pq.push(new_board, heuristic_value)
            parents[new_board_state] = (hash(current_board.get_board_state()), car_id, steps)


def reconstruct_path(parents: dict, state: int):
    """
    Reconstruct the path from the goal state back to the initial state using parent relationships.
    """
    path = []
    while parents[state] is not None:
        # Haal de ouderstaat en de bijbehorende zet op
        parent_state, car_id, steps = parents[state]
        # Voeg de zet toe aan het pad
        path.append([car_id, steps])
        # Update de huidige toestand naar de ouderstaat voor de volgende iteratie
        state = parent_state
    # Keer het pad om zodat het van begin naar eind gaat
    return path[::-1]

def save_solution_to_csv(solution, d, game_number):
    """
    Save the solution path to a CSV file.
    """
    file_path = f'data/Breadth_First/Best_Moves/board_{game_number}_{d}x{d}.csv'
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Step'])
        for move in solution:
            writer.writerow(move)
        print(f"Moves successfully saved to {file_path}")

    return file_path


if __name__ == "__main__":

	board1 = Board(9,6)
