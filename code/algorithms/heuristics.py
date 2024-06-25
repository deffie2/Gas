from code.classes.board import Board
# import sys
# sys.path.append("../classes")
# from board import Board


def total_count_BEAM(board: "Board") -> int:
    """
    Pre: board
    Post: int (the score)
    Counts the total score of importance. 
    The higher te score, the closer this board supposingly is to a solution 
    """
    
    score_red_car_distance = distance_for_red_car(board) 
    score_blocking_cars = count_blocking_cars(board)
    score_free_space_blocking_cars = free_space_blocking_cars(board)
    score_fraction_moved = total_moves_of_car_just_moved(board)
    
    # NIEUW : Normaliseer de scores (stel dat ze allemaal binnen [0, 10] vallen)
    normalized_red_car_distance = normalize(score_red_car_distance, 0, board.dimension - 1)
    normalized_blocking_cars = normalize(score_blocking_cars, 0, max_blocking_cars(board))
    normalized_free_space_blocking_cars = normalize(score_free_space_blocking_cars, 0, max_empty_spaces(board))
    normalized_fraction_moved = normalize(score_fraction_moved, 0, 10)
    print(f"normalized_fraction_moved {normalized_fraction_moved}")

    # NIEUW: Weeg de genormaliseerde scores
    weight_red_car_distance = 0.25
    weight_blocking_cars = 0.25
    weight_free_space_blocking_cars = 0.25
    weight_fraction_moved = 0.25

    # NIEUW
    total_count = (
        weight_red_car_distance * normalized_red_car_distance +
        weight_blocking_cars * normalized_blocking_cars -
        weight_free_space_blocking_cars * normalized_free_space_blocking_cars +
        weight_fraction_moved * normalized_fraction_moved
    )

    # The higher the further away it is to win with this board
    # EERST: total_count = score_red_car_distance + score_blocking_cars - score_free_space_blocking_cars + score_fraction_moved
    
    # Invert the score (so higher means, the closer the board would be to a solution)
    total_count *= -1
    
    # If the red car has a clear way to the exit
    if board.heuri_red_clear_exit():
        total_count += 1000
    
    # If the red car is already at the end
    if board.is_red_car_at_exit():
        total_count += 2000
    print(f"total_count: {total_count}")
    return total_count

# NIEUW
def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

def max_empty_spaces(board: "Board"):
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

def max_blocking_cars(board: "Board"):
    red_car = board.vehicle_dict.get('X')
    location = red_car.col + red_car.size
    max_blocking_cars = 0
    total_size = 0
    for i in range(location, board.dimension):
        colomns_left =+ 1
        for car_id, value in board.vehicle_dict.items():
            col = value.col
            direction = value.direction
            size = value.size
            if col == i and direction == 'V':
                max_blocking_cars += 1
                total_size += size
                break
    print(f"max_blocking_cars {max_blocking_cars}") 
    if max_blocking_cars == 0:
        max_blocking_cars = 1
    return max_blocking_cars
     


    # DONE
def distance_for_red_car(board: "Board") -> int:
    """
    Pre: board
    Post: score (as an int)
    Counts the distance the red car still has to move to go to the exit
    """
    
    red_car = board.vehicle_dict['X']
    distance_score = board.dimension - (red_car.col + red_car.size)
    print (f"distance_score: {distance_score}")
    return distance_score
    

    # DONE
def count_blocking_cars(board: 'Board') -> int:
    """
    Pre: board
    Post: score (as an int)
    Counts the amount of cars that block the red car from an exit
    """

    red_car = board.vehicle_dict['X']
    blocking_cars = 0
    for col in range(red_car.col + red_car.size, board.dimension):
        if board.board[red_car.row][col] != "_":
            blocking_cars += 1
    print(f"blocking cars {blocking_cars}")
    return blocking_cars

# DONE
def free_space_blocking_cars(board: 'Board') -> int:
    """
    Pre: New option  board
    Post: score (as an int)
    Calculates the total amount of empty places 
    the blocking cars could move to.
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

    # DONE
def total_moves_of_car_just_moved(board: 'Board') -> int:
    """
    Pre: board
    Post: score (as an int)
    A variable that determines how much a car has moved already, relative to the average amount of times the cars moved
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
    
    n_cars= len(board.vehicle_dict)
    average = total_cars_moved / n_cars 
    score = just_moved_n_moved / average

    # Calculate score
    print(f"just n moved {just_moved_n_moved}")
    print(f"total car moved {total_cars_moved}")
    #score = round((just_moved_n_moved / total_cars_moved) * 10)
          
    
    print(f"how much the car relatively already has moved: {score}")
    return score

if __name__ == "__main__":

    board = Board(6,1)
    board3 = Board(6,3)
    #board.printboard()
    board3.printboard()
    #helper = {"Banaan": 6, "Appel": 3}
    #print(helper)
    totalcount = total_count_BEAM(board3)
    # print(totalcount)
    
    
