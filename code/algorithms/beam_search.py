from typing import List, Tuple, Dict
import csv
import time
import os


from code.classes.board import Board
from code.algorithms.heuristics import total_count_BEAM


def beam_search(d: int, game_number: int, runs: int) -> str:
    """
    Perform beam search on the given initial board to find a path
    where the red car reaches the exit.

    pre: d is a positive integer that indicates the size of the board.
    pre: game_number is a valid that identifies for game board.
    pre: runs is a positive integer that indicates the number of runs to
    attempt.

    post: returns in a the file path of the saved CSV file containing
    the solution path if a solution is found within the specified number
    of runs.
    post: returns None if no solution is found.
    """
    assert isinstance(d, int) and d > 0, "d must be a positive integer."
    assert isinstance(game_number, int) and game_number > 0, \
        "game_number must be higher then zero."
    assert isinstance(runs, int) and runs > 0, \
        "runs must be a positive integer."

    # Check if the CSV file exists for the given game configuration
    csv_path = f'data/Rushhour_games/Rushhour{d}x{d}_{game_number}.csv'
    assert os.path.isfile(csv_path), \
        f"Invalid game configuration for d={d} and game_number={game_number}"

    # Prompting the user to input parameters for beam search configuration
    beam_width = int(input("What value would you like for the beam width? "))
    heuristic_weight_value = float(
        input("What heuristics weight-value would you like to test? ")
    )

    # Starting the timer to measure execution time
    start_time = time.time()
    csv_name = None
    for i in range(runs):
        initial_board = Board(d, game_number)

        # Initialize the parents dictionary for the search
        initial_board, parents = initialize_search(initial_board)

        boards = [initial_board]

        while boards:

            # Check if the current state is a winning state
            for current_board in boards:
                if current_board.is_red_car_at_exit():
                    solution = reconstruct_path(parents, hash(current_board))
                    # Stop the timer
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"The number of visited states: {len(parents) - 1}")
                    print(f"The code took {elapsed_time} seconds to execute.")

                    # Save the solution to the CSV file
                    csv_name = save_solution_to_csv(
                        solution, d, game_number, beam_width, elapsed_time,
                        heuristic_weight_value, parents
                    )
                    return csv_name

            # Process the possible moves from the current board state
            states = process_moves(boards, parents)
            scored_states = score_states(states, heuristic_weight_value)
            scored_states = apply_beam(scored_states, beam_width)
            boards = []
            # Select the top states according to the beam width for further \
            # exploration
            for _, board, _, _ in scored_states:
                boards.append(board)

    return None


def calculate_heuristic(board: Board, heuristic_weight_value: float) -> int:
    """
    Calculate the heuristic value for a given board state using a specific
    heuristic function.

    pre: heuristic_weight_value is a non-negative float representing the weight
    in the heuristic calculation.
    post: returns of each board a integer representing the heuristic value
    """
    assert isinstance(heuristic_weight_value, float)
    return total_count_BEAM(board, heuristic_weight_value)


def initialize_search(initial_board: Board) -> Tuple[
        Board, Dict[int, Tuple[int, str, int]]]:
    """Initializes the parents dictionary for the search."""
    parents: Dict[int, Tuple[int, str, int]] = {}

    # initial board with its heuristic value
    initial_state = hash(initial_board)
    parents[initial_state] = None
    return initial_board, parents


def process_moves(
    boards: list[Board],
    parents: dict[int, tuple[int, str, int]]
) -> list[tuple[tuple[Board, str, int], Board]]:
    """
    Generate next possible states from a list of current board states.

    post: Returns a list of tuples containing next possible board states,
    the car id, and the steps taken.
    """
    next_states: List[Tuple[Board, str, int]] = []

    for current_board in boards:
        movable_vehicles, possible_moves = \
            current_board.generate_all_possible_moves()

        for car_id in movable_vehicles:
            for move_direction, step_list in possible_moves[car_id]:
                for steps in step_list:
                    new_board = current_board.move_vehicle(car_id, steps)

                    # Store new board and heuristic value in list if not \
                    # already in parents
                    h = hash(new_board)
                    if h not in parents:
                        next_states.append((new_board, car_id, steps))
                        parents[h] = (hash(current_board), car_id, steps)

    return next_states


def score_states(
    states: list[tuple[Board, str, int]],
    heuristic_weight_value: float
) -> list[tuple[int, Board, str, int]]:
    """
    Assign heuristic scores to each state based on a specified heuristic
    function.

    post: returns a list of tuples containing heuristic scores, boards,
    car ids, and steps.
    """
    scored_states: List[Tuple[int, Board, str, int]] = []
    for board, car_id, steps in states:
        heuristic_value = calculate_heuristic(board, heuristic_weight_value)
        scored_states.append((heuristic_value, board, car_id, steps))
    return scored_states


def apply_beam(states: list[tuple[int, Board, str, int]],
               beam_width: int) -> list[tuple[int, Board, str, int]]:
    """
    Apply beam search selection to retain only the top states based on
    their heuristic scores.

    pre: beam_width is a positive integer representing the number of top
    states to retain.
    post: returns a list of tuples containing the top states after beam
    search selection.
    """
    assert isinstance(beam_width, int) and beam_width > 0, \
        "beam_width must be a positive integer."
    states.sort(key=lambda x: x[0], reverse=True)
    return states[:beam_width]


def reconstruct_path(parents: dict, state: int):
    """
    Reconstruct the path from the goal state back to the initial state using
    parent relationships.

    pre: state is the hash of the goal state.
    post: returns a list of lists representing the sequence of actions to
    reach from the initial to the goal state.
    """
    assert isinstance(state, int), "state must be an integer."
    path: List[Tuple[str, int]] = []
    while parents[state] is not None:
        parent_state, car_id, steps = parents[state]
        path.append([car_id, steps])
        state = parent_state
    # Reverse the path to go from start to end
    return path[::-1]


def save_solution_to_csv(
    solution: List[Tuple[str, int]], d: int, game_number: int,
    beam_width: int, elapsed_time: float, heuristic_weight_value: float,
    parents: Dict[int, Tuple[int, str, int]]
) -> str:
    """
    Saves the solution path to a CSV file.

    post: returns the file path where the solution is saved.
    """
    file_path1 = (
        f'data/Beam_Search/board_{game_number}_'
        f'bm_{beam_width}_'
        f'hv_{heuristic_weight_value}.csv'
    )
    with open(file_path1, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Step'])
        for move in solution:
            writer.writerow(move)
        print(len(solution))
        print(f"Moves successfully saved to {file_path1}")

    # Save additional results to CSV voor experiment
    filepath2 = 'Experiment/results_bs.csv'
    file_exists = os.path.isfile(filepath2)
    with open(filepath2, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                'Board', 'Algorithm', 'Board States', 'Time',
                'Beam Width', 'Moves', 'heuristic_weight_value'
            ])
            file_exists = True
        writer.writerow([
            game_number, 'bs', len(parents) - 1, elapsed_time,
            beam_width, len(solution), heuristic_weight_value
        ])

    return file_path1
