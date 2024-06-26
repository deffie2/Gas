from code.classes.board import Board
from typing import Tuple


def total_count_BEAM(board: "Board", weight_fraction_moved: float) -> float:
    """
    Calculate the heuristic value for a given board state.

    pre: board (Board), weight_fraction_moved is a non-negative 
    float representing the weight of the factioin moved heuristic.
    post: returns an integer representing the heuristic value.
    """
    #Calcluating scores
    scores = calculate_scores(board)
    normalized_scores = normalize_scores(scores, board)
    weights = calculate_weights(weight_fraction_moved)

    #Calculatie total heuristic score
    total_count = (
        weights[0] * normalized_scores[0] -
        weights[1] * normalized_scores[1] +
        weights[2] * normalized_scores[2] -
        weight_fraction_moved * normalized_scores[3]
    )

    # If the red car has a clear way to the exit
    if board.heuri_red_clear_exit():
        total_count += 1000
    
    # If the red car is already at the end
    if board.is_red_car_at_exit():
        total_count += 2000
    
    return total_count


def normalize(value: int, min_value: int, max_value: int) -> float:
    """
    Normalize a value within a given range.

    pre: value (int), min_value (int), max_value (int)
    post: returns a float representing the normalized value.
    """
    return (value - min_value) / (max_value - min_value)


def calculate_scores(board: "Board") -> Tuple[int, int, int, float]:
    """
    Calculates the heuristic scores for the given board.

    pre: board (Board)
    post: returns a tuple of scores (int, int, int, float).
    """
    score_red_car_distance = distance_for_red_car(board)
    score_blocking_cars = count_blocking_cars(board)
    score_free_space_blocking_cars = free_space_blocking_cars(board)
    score_fraction_moved = total_moves_of_car_just_moved(board)

    return (
        score_red_car_distance,
        score_blocking_cars,
        score_free_space_blocking_cars,
        score_fraction_moved
    )


def max_empty_spaces(board: "Board") -> int:
    """
    Calculates the max amount of empty spaces of the blocking cars
    for the normalisation

    pre: board (Board)
    post:the max empty spaces, a positive integers
    
    """
    red_car = board.vehicle_dict.get('X')
    location = red_car.col + red_car.size
    max_blocking_cars = 0
    total_size = 0
    colomns_left = 0
    for i in range(location, board.dimension):
        colomns_left =+ 1
        for car_id, value in board.vehicle_dict.items():
            col = value.col
            direction = value.direction
            size = value.size
            if col == i and direction == 'V':
                max_blocking_cars += 1
                total_size += size
      
    empty_spaces = (board.dimension * colomns_left) - total_size
    if empty_spaces == 0:
        empty_spaces = 1

    return empty_spaces   


def max_blocking_cars(board: "Board") -> int:
    """
    Calculates the max amount blocking cars for the normalisation.

    pre: board (Board)
    post:the max empty spaces, a positive integers

    """
    red_car = board.vehicle_dict.get('X')
    location = red_car.col + red_car.size
    max_blocking_cars = 0
    total_size = 0
    for i in range(location, board.dimension):
        for car_id, value in board.vehicle_dict.items():
            col = value.col
            direction = value.direction
            size = value.size
            if col == i and direction == 'V':
                max_blocking_cars += 1
                total_size += size
                break
    if max_blocking_cars == 0:
        max_blocking_cars = 1

    return max_blocking_cars


def calculate_weights(weight_fraction_moved: float) -> Tuple[float, float, float]:
    """
    Calculates weights for each heuristic.

    pre: weight_fraction_moved (float)
    post: returns a tuple of weights (float, float, float).
    """
    weight_red_car_distance = (1.0 - weight_fraction_moved) / 3
    weight_blocking_cars = (1.0 - weight_fraction_moved) / 3
    weight_free_space_blocking_cars = (1.0 - weight_fraction_moved) / 3

    return (
        weight_red_car_distance,
        weight_blocking_cars,
        weight_free_space_blocking_cars
    )

    
def normalize_scores(scores: Tuple[int, int, int, float], board: "Board") -> \
    Tuple[float, float, float, float]:
    """
    Normalizes the calculated heuristic scores.

    pre: scores (tuple of int, int, int, float), board (Board)
    post: returns a tuple of normalized scores (float, float, float, float).
    """
    normalized_red_car_distance = normalize(scores[0], 0, board.dimension - 1)
    normalized_blocking_cars = normalize(scores[1], 0, max_blocking_cars(board))
    normalized_free_space_blocking_cars = normalize(scores[2], 0, max_empty_spaces(board))
    normalized_fraction_moved = normalize(scores[3], 0, 10)

    return (
        normalized_red_car_distance,
        normalized_blocking_cars,
        normalized_free_space_blocking_cars,
        normalized_fraction_moved
    )


def distance_for_red_car(board: "Board") -> int:
    """
    Counts the distance the red car still has to move to go to the exit

    pre: board (Board)
    post: returns an int representing the score.
    """
    red_car = board.vehicle_dict['X']
    distance_score = board.dimension - (red_car.col + red_car.size)

    return distance_score
    

def count_blocking_cars(board: 'Board') -> int:
    """
    Counts the amount of cars that block the red car from an exit

    pre: board (Board)
    post: returns an int representing the score.
    """
    red_car = board.vehicle_dict['X']
    blocking_cars = 0
    for col in range(red_car.col + red_car.size, board.dimension):
        if board.board[red_car.row][col] != "_":
            blocking_cars += 1

    return blocking_cars


def free_space_blocking_cars(board: 'Board') -> int:
    """
    Calculates the total amount of empty places the blocking cars
    could move to.

    pre: new option  board
    post: score (as an int)
    """
    free_space = 0
    red_car = board.vehicle_dict['X']
    for col in range(red_car.col + red_car.size, board.dimension):
        if board.board[red_car.row][col] != "_":
            blocking_car_id = board.board[red_car.row][col]
            movable_vehicles, possible_moves = board.generate_all_possible_moves()
            if blocking_car_id in board.movable_vehicles:
                for Tuple in possible_moves[blocking_car_id]:
                    free_space += len(Tuple[1])
    print(f"free space: {free_space}")
    return free_space


def total_moves_of_car_just_moved(board: 'Board') -> float:
    """
    A variable that determines how much a car has moved already, relative to
    the average amount of times the cars moved
    
    pre: board (Board)
    post: score (as an int)
    
    """
    # Total amount of cars moved
    total_cars_moved = sum(vehicle.n_times_moved for vehicle in board.vehicle_dict.values())
    
    # The amount of times moved by just_moved car
    just_moved_n_moved = 0
    for carID, vehicles in board.vehicle_dict.items():
        if vehicles.justmoved == True:
            just_moved_n_moved = vehicles.n_times_moved
            break
    
    if total_cars_moved == 0:
        return 0
    
    # Calculate score
    n_cars= len(board.vehicle_dict)
    average = total_cars_moved / n_cars 
    score = just_moved_n_moved / average

    return score

    
    
