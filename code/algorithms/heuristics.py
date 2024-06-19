from code.classes.board import Board


def count_blocking_cars(board: 'Board') -> int:
    """
    Heuristic: Number of blocking cars
    """

    # for loop moet beginnen op de plek 


    red_car = board.vehicle_dict['X']
    blocking_cars = 0
    for col in range(red_car.col + red_car.size, board.dimension):
        if board.board[red_car.row][col] != "_":
            blocking_cars += 1
    return blocking_cars

def blocking_cars_distance(board: 'Board') -> int:
    """
    Heuristic: Total distance of blocking cars from their movable position
    """
    total_distance = 0
    red_car = board.vehicle_dict['X']
    for col in range(red_car.col + red_car.size, board.dimension):
        if board.board[red_car.row][col] != "_":
            blocking_car_id = board.board[red_car.row][col]
            blocking_car = board.vehicle_dict[blocking_car_id]
            if blocking_car.direction == 'H':
                distance = abs(blocking_car.row - red_car.row)
            else:
                distance = abs(blocking_car.col - red_car.col)
            total_distance += distance
    return total_distance

def free_space_around_blocking_cars(board: 'Board') -> int:
    """
    Heuristic: Free space around blocking cars
    """
    free_space = 0
    red_car = board.vehicle_dict['X']
    for col in range(red_car.col + red_car.size, board.dimension):
        if board.board[red_car.row][col] != "_":
            blocking_car_id = board.board[red_car.row][col]
            blocking_car = board.vehicle_dict[blocking_car_id]
            for pos in blocking_car.vehiclepositions():
                if pos in board.empty_places():
                    free_space += 1
    return free_space

def block_level(board: 'Board') -> int:
    """
    Heuristic: Blocking level
    """
    blocking_level = 0
    red_car = board.vehicle_dict['X']
    for col in range(red_car.col + red_car.size, board.dimension):
        if board.board[red_car.row][col] != "_":
            blocking_level += 1
    return blocking_level

def total_moves_of_all_cars(board: 'Board') -> int:
    """
    Heuristic: Total movements of all cars
    """
    return sum(vehicle.n_times_moved for vehicle in board.vehicle_dict.values())

if __name__ == "__main__":

    board = Board(6,1)
    board.printboard()
    