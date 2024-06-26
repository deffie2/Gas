import csv
import random
from typing import List, Tuple

from code.classes.board import Board


def move_car_random_WOH(d: int, game_number: int, runs: int) -> List[str]:
    """
    Perform random moves without heuristics (WOH) to solve the board
    and save the results to CSV files.

    Post: the number of moves for each run and the best move sequence
    are saved in CSV files.
    Post: a list of CSV file paths and the algorithm name are returned.
    """
    random.seed(42)  # Set the seed for reproducibility
    best_moves = float('inf')

    moveslist = []
    for i in range(runs):

        board = Board(d, game_number)

        moves = 0
        while not (board.is_red_car_at_exit()):
            # Select a random move
            movable_vehicle, possible_vehicle_moves = \
                select_random_move(board, False)

            # Combine all possible steps for all directions
            all_possible_steps = \
                combine_possible_steps(possible_vehicle_moves)

            # Randomly select a step from all possible steps
            move_direction, step = random.choice(all_possible_steps)

            # Move the vehicle to the new position
            new_board = board.move_vehicle(movable_vehicle, step)

            board = new_board
            moves += 1
        moveslist.append(moves)

        if i == 0 or moves < best_moves:
            best_moves = moves
            best_moves_list = board.move_history

    algorithm = "WOH"
    csv_namen = save_moves_to_csv(
        game_number, runs, d, moveslist, best_moves_list, algorithm
    )
    return csv_namen


def move_car_random_WH(d: int, game_number: int, runs: int) -> List[str]:
    """
    Perform random moves with heuristics (WH) to solve the board and
    save the results to CSV files.

    Post: the number of moves for each run and the best move sequence
    are saved in CSV files.
    Post: a list of CSV file paths and the algorithm name are returned.
    """
    random.seed(42)  # Set the seed for reproducibility
    best_moves = float('inf')

    moveslist = []
    for i in range(runs):

        board = Board(d, game_number)

        moves = 0
        while not (board.is_red_car_at_exit()):
            # Select a random move
            movable_vehicle, possible_vehicle_moves = \
                select_random_move(board, True)

            # Combine all possible steps for all directions
            all_possible_steps = \
                combine_possible_steps(possible_vehicle_moves)

            # Randomly select a step from all possible steps
            move_direction, step = random.choice(all_possible_steps)

            if not (board.heuri_red_clear_exit()):
                # Move the vehicle to the new position
                new_board = board.move_vehicle(movable_vehicle, step)
            else:
                new_board = board.heuri_get_red_to_exit()

            board = new_board
            moves += 1
        moveslist.append(moves)

        if i == 0 or moves < best_moves:
            best_moves = moves
            best_moves_list = board.move_history

    algorithm = "WH"
    csv_namen = save_moves_to_csv(
        game_number, runs, d, moveslist, best_moves_list, algorithm
    )
    return csv_namen


def select_random_move(
    board: Board,
    heuristics: bool
) -> Tuple[str, List[Tuple[str, Tuple[int, int]]]]:
    """
    Select a random move from the board's possible moves.

    Post: a randomly selected movable vehicle and its possible moves
    are returned.
    """
    # Generate all possible moves
    movable_vehicles, possible_moves = \
        board.generate_all_possible_moves()

    if heuristics:
        movable_vehicles = board.heuri_change_moveable_cars()
    # Randomly select a vehicle that can move
    movable_vehicle = random.choice(list(movable_vehicles))

    # Get possible moves for the selected vehicle
    possible_vehicle_moves = possible_moves.get(movable_vehicle, [])

    return movable_vehicle, possible_vehicle_moves


def combine_possible_steps(
    possible_vehicle_moves: List[Tuple[str, List[Tuple[int, int]]]]
) -> List[Tuple[str, Tuple[int, int]]]:
    """
    Combine all possible steps for all directions of a vehicle's moves.

    Postconditions: a combined list of all possible steps is returned.
    """
    all_possible_steps = []
    for move_direction, move_steps in possible_vehicle_moves:
        for step in move_steps:
            all_possible_steps.append((move_direction, step))
    return all_possible_steps


def save_moves_to_csv(
    game_number: int,
    runs: int, d: int,
    moveslist: List[int],
    best_moves_list: List[Tuple[str, Tuple[int, int]]],
    algorithm: str
) -> List[str]:
    """
    Save the moves and best moves to CSV files.

    Post: Two CSV files are created: one for the frequency of moves
    and one for the best moves.
    """
    csv_namen = []
    filepath1 = (
        'data/Random/'
        f'Freq_moves_{algorithm}/'
        f'board_{game_number}_{runs}_'
        f'freq_move_{algorithm}_{d}x{d}.csv'
    )
    with open(filepath1, mode='w', newline='') as file:
        writer = csv.writer(file)

        for move in moveslist:
            writer.writerow([move])
    csv_namen.append(filepath1)

    filepath2 = (
        'data/Random/'
        f'Best_Moves_{algorithm}/'
        f'board_{game_number}_{runs}_'
        f'Best_moves_{algorithm}_{d}x{d}.csv'
    )
    with open(filepath2, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Step'])

        for move in best_moves_list:
            writer.writerow(move)
    csv_namen.append(filepath2)
    csv_namen.append(algorithm)
    return csv_namen
