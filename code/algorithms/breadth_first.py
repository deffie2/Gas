import copy


from code.classes.board import Board
from code.classes.queue import Queue
from typing import List, Optional, Tuple


def breadth_first_search_without_heur(initial_bord: Board):
    """
    Perform breadth-first search on the given initial board to find a path
    where the red car reaches the exit.
    """
    assert isinstance(initial_board, Board), "initial_board should be an instance of Board"

    # Create een queue om toestanden van het bord en bijbehorende moves te beheren
    queue = Queue()
    # Bijhouden van de ouders van elk bord voor pad reconstructie
    parents = {}

    # Zet het initial_bord in queue en visited_state
    queue.enqueue(initial_bord)
    initial_state = hash(initial_bord)
    parents[initial_state] = None

    # Nu ga je checken als de queue niet leeg is
    while not queue.is_empty():
        # Get the current state from the queue and pop it
        current_board = queue.dequeue()
        # print(current_board)

        # Check if the initial state is already a winning state
        if current_board.is_red_car_at_exit():
            queue.clear()
            return reconstruct_path(parents, hash(current_board))

        # Verwerk de mogelijke zetten vanuit de huidige toestand van het bord
        process_moves(current_board, queue, parents)

    return None


def breadth_first_search_with_early_constraints(initial_board: Board, constrain_number: int):
    """Executes BFS with early constraints and resets search if constraints are exceeded."""

    movable_vehicles, possible_moves = initial_board.generate_all_possible_moves()
    all_paths_to_exit = []

    for car_id in movable_vehicles:
        queue, parents = initialize_search(initial_board)
        

        # Move the current car and initialize the search from that state
        for move_direction, step_list in possible_moves[car_id]:
            for steps in step_list:
                new_board = copy.deepcopy(initial_board)
                new_board.move_vehicle(car_id, move_direction, steps)

                new_board_state = hash(new_board.get_board_state())

                # Controleer of de nieuwe toestand al is bezocht
                if new_board_state not in queue.visited_state:
                    queue.enqueue(new_board)
                    parents[new_board_state] = (hash(initial_board.get_board_state()), car_id, move_direction, steps)

                    moves = 1
                    while not queue.is_empty():

                        # Get the current state from the queue and pop it
                        current_board = queue.dequeue()

                        # Check if the current state is already a winning state
                        if current_board.is_red_car_at_exit():
                            red_car_path = reconstruct_path(parents, hash(current_board))
                            all_paths_to_exit.add(red_car_path)
                            queue.clear()
                            queue, parents = initialize_search(initial_board)
                            break

                        elif moves >= constrain_number:
                            queue.clear()
                            queue, parents = initialize_search(initial_board)
                            break


                        # Verwerk de mogelijke zetten vanuit de huidige toestand van het bord
                        process_moves(current_board, queue, parents)
                        moves += 1
    
    if all_paths_to_exit:
        return min(all_paths_to_exit, key=len)
    else:
        return None

def initialize_search(initial_bord):
    """Initializes the queue and parents dictionary for the search."""
    queue = Queue()
    parents = {}

    # Enqueue the initial board and mark it as visited
    queue.enqueue(initial_bord)
    initial_state = hash(initial_bord)
    parents[initial_state] = None

    return queue, parents


def process_moves(current_board: Board, queue: Queue, parents: dict):
    """
    Generate and process all possible moves from the current board state.

    """
    movable_vehicles, possible_moves = current_board.generate_all_possible_moves()

    for car_id in movable_vehicles:
        for move_direction, step_list in possible_moves[car_id]:
            for steps in step_list:
                # Maak een kopie van het bord en voer de zet uit
                new_board = copy.deepcopy(current_board)
                new_board.move_vehicle(car_id, move_direction, steps)

                new_board_state = hash(new_board.get_board_state())

                # Controleer of de nieuwe toestand al is bezocht
                if new_board_state not in queue.visited_state:
                    queue.enqueue(new_board)
                    parents[new_board_state] = (hash(current_board.get_board_state()), car_id, move_direction, steps)
                    print(f"Key: {new_board_state}, Value: {parents[new_board_state]}")


def reconstruct_path(parents: dict, state: int):
    """
    Reconstruct the path from the goal state back to the initial state using parent relationships.
    """
    path = []
    while parents[state] is not None:
        # Haal de ouderstaat en de bijbehorende zet op
        parent_state, car_id, move_direction, steps = parents[state]
        # Voeg de zet toe aan het pad
        path.append([car_id, move_direction, steps])
        # Update de huidige toestand naar de ouderstaat voor de volgende iteratie
        state = parent_state
    # Keer het pad om zodat het van begin naar eind gaat
    return path[::-1]




