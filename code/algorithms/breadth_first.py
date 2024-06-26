import csv
import time
import os


from code.classes.board import Board
from code.classes.queue import Queue
from typing import List, Tuple, Dict


def breadth_first_search(d: int, game_number: int, runs: int):
    """
    Perform breadth-first search on the given initial board to find a path
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

    # Starting the timer to measure execution time
    start_time = time.time()
    csv_name = None
    for i in range(runs):
        initial_board = Board(d, game_number)

        # Initialize the queue and parents dictionary for the search
        queue, parents = initialize_search(initial_board)

        moves = 0
        # Check if queue is not empty
        while not queue.is_empty():

            # Print a message every 100000 moves
            moves += 1
            if moves % 2000000 == 0:
                print(f"Move count: {moves}")

            # Get the current state from the queue and pop it
            current_board = queue.dequeue()

            # Check if the initial state is already a winning state
            if current_board.is_red_car_at_exit():
                solution = reconstruct_path(parents, hash(current_board))
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"The code took {elapsed_time} seconds to execute.")
                print(f"The number of visited states: {len(parents) - 1}")
                queue.clear()

                # Save the solution to the CSV file
                csv_name = save_solution_to_csv(
                    solution, d, game_number,
                    elapsed_time, parents
                )
                return csv_name

            # Process possible moves from the current board state
            process_moves(current_board, queue, parents)

    return None


def initialize_search(initial_bord: Board) -> Tuple[
        Board, Dict[int, Tuple[int, str, int]]]:
    """
    Initializes the queue and parents dictionary for the search.

    post: returns a initialized queue and a parent dictionary
    """
    queue = Queue()
    parents = {}

    # Enqueue the initial board and mark it as visited
    queue.enqueue(initial_bord)
    initial_state = hash(initial_bord)
    parents[initial_state] = None

    return queue, parents


def process_moves(
    current_board: Board,
    queue: Queue,
    parents: Dict[int, [Tuple[int, str, int]]]
) -> None:
    """
    Generate and process all possible moves from the current board state.

    post: new board states are added to queue.
    """
    movable_vehicles, possible_moves = \
        current_board.generate_all_possible_moves()

    for car_id in movable_vehicles:
        for move_direction, step_list in possible_moves[car_id]:
            for steps in step_list:
                new_board = current_board.move_vehicle(car_id, steps)
                new_board_state = hash(new_board)
                # Check if the new state has been visited
                if new_board_state not in parents:
                    queue.enqueue(new_board)
                    parents[new_board_state] = \
                        (hash(current_board), car_id, steps)


def reconstruct_path(parents: Dict[int, Tuple[int, str, int]],
                    state: int) -> List[Tuple[str, int]]:
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
    elapsed_time: float,
    parents: Dict[int, Tuple[int, str, int]]
) -> str:
    """
    Saves the solution path to a CSV file.

    post: returns the file path where the solution is saved.
    """
    file_path1 = f'data/Breadth_First/board_{game_number}_{d}x{d}.csv'
    with open(file_path1, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Step'])
        for move in solution:
            writer.writerow(move)
        print(f"Moves successfully saved to {file_path1}")

    # Save additional results to CSV voor experiment
    filepath2 = 'Experiment/results_bf.csv'
    file_exists = os.path.isfile(filepath2)
    with open(filepath2, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                'Board', 'Algorithm', 'Board States',
                'Time', 'Moves'
            ])
            file_exists = True
        writer.writerow([
            game_number, 'bf', len(parents) - 1,
            elapsed_time, len(solution)
        ])

    return file_path1
