from code.classes.board import Board
from code.algorithms.heuristics import total_count_BEAM

import csv
import time
import os



def beam_search(d, game_number, runs):
    """
    Perform beam search on the given initial board to find a path
    where the red car reaches the exit.
    """
    beam_width = int(input("What value would you like for the beam width? "))
    heuristic_weight_value = float(input("What heuristics weight-value would you like to test? "))
    start_time = time.time()
    csv_name = None
    for i in range(runs):
        initial_board = Board(d, game_number)
        
        # Initialize the priority queue and parents dictionary for the search
        initial_board, parents = initialize_search(initial_board)

        boards = [initial_board]

        while boards:

            # Check if the current state is a winning state
            for current_board in boards:
                if current_board.is_red_car_at_exit():
                    solution = reconstruct_path(parents, hash(current_board))
                    end_time = time.time()
                    print(f"De lengte van de dictionary is: {len(parents) - 1}")
                    elapsed_time = end_time - start_time
                    print(f"De code heeft {elapsed_time} seconden nodig gehad om uit te voeren.")
                
                # Save the solution to the CSV file
                    csv_name, amount_moves = save_solution_to_csv(solution, d, game_number, beam_width)
                    # Save the solution details to the CSV file
                    filepath = f'Experiment/results_bs.csv'
                    file_exists = os.path.isfile(filepath)
                    with open(filepath, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        if not file_exists:
                            writer.writerow(['Board', 'Algorithm', 'Board States', 'Time', 'Beam Width', 'Moves', 'heuristic_weight_value'])
                            file_exists = True
                        writer.writerow([game_number, 'bs', len(parents) - 1, elapsed_time, beam_width, amount_moves, heuristic_weight_value])
                    return csv_name

            # Process the possible moves from the current board state
            states = process_moves(boards, parents)
            print("children", len(states))
            #states = filter_states_on_parents(states, parents)
            #add_to_parent_states(states, parents)
            scored_states = score_states(states, heuristic_weight_value)
            scored_states = apply_beam(scored_states, beam_width)
            boards = []
            for _, board, _, _ in scored_states:
                boards.append(board)

            print("width", len(boards))

    if csv_name:
        return csv_name
    return None


def calculate_heuristic(board, heuristic_weight_value):
    return total_count_BEAM(board, heuristic_weight_value)
    

def initialize_search(initial_board):
    """Initializes the priority queue and parents dictionary for the search."""
    parents = {}

    # Enqueue the initial board with its heuristic value
    initial_state = hash(initial_board)
    parents[initial_state] = None
    return initial_board, parents


def process_moves(boards: list[Board], parents: dict[int, tuple[int, str, int]]) \
    -> list[tuple[tuple[Board, str, int], Board]]:
    next_states = []

    for current_board in boards:
        movable_vehicles, possible_moves = current_board.generate_all_possible_moves()

        for car_id in movable_vehicles:
            for move_direction, step_list in possible_moves[car_id]:
                for steps in step_list:
                    new_board = current_board.move_vehicle(car_id, steps)

                    # Sla het nieuwe bord en de heuristische waarde op in een lijst
                    h = hash(new_board) 
                    if h not in parents:
                        next_states.append((new_board, car_id, steps))
                        parents[h] = (hash(current_board), car_id, steps)


    return next_states

def score_states(states: list[tuple[Board, str, int]], heuristic_weight_value: float) -> list[tuple[int, Board, str, int]]:
    scored_states = []
    for board, car_id, steps in states:
        scored_states.append((calculate_heuristic(board, heuristic_weight_value), board, car_id, steps))
    return scored_states

def apply_beam(states: list[tuple[int, Board, str, int]], beam_width: int) -> list[tuple[int, Board, str, int]]:
    states.sort(key=lambda x: x[0], reverse=True)
    return states[:beam_width]


def reconstruct_path(parents: dict, state: int):
    """
    Reconstruct the path from the goal state back to the initial state using parent relationships.
    """
    # print(f"Reconstructing path for state: {state}")
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

def save_solution_to_csv(solution, d, game_number, beam_width):
    """
    Save the solution path to a CSV file.
    """
    file_path = f'data/Beam_Search/board_{game_number}_{d}x{d}_beam_width_{beam_width}.csv'
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Step'])
        for move in solution:
            writer.writerow(move)
        print(f"Moves successfully saved to {file_path}")

    # Read the number of lines in the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        amount_moves = sum(1 for row in reader) - 1
    
    return file_path, amount_moves