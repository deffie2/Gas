from code.classes.board import Board
#import sys
#sys.path.append("../classes")
#from board import Board


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
    # print(f"score fraction moved: {score_fraction_moved}")
    
    # The higher the further away it is to win with this board
    total_count = score_red_car_distance + score_blocking_cars - score_free_space_blocking_cars + score_fraction_moved
    
    # Invert the score (so higher means, the closer the board would be to a solution)
    total_count *= -1
    
    return total_count
    
    # DONE
def distance_for_red_car(board: "Board") -> int:
    """
    Pre: board
    Post: score (as an int)
    Counts the distance the red car still has to move to go to the exit
    """
    
    red_car = board.vehicle_dict['X']
    
    return board.dimension - (red_car.col + red_car.size)
    

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
    return blocking_cars

#def movability_red_car(board: "Board") -> int
    

# # Ik snap dit niet
# def blocking_cars_distance(board: 'Board') -> int:
    # """
    # Heuristic: Total distance of blocking cars from their movable position
    # """
    # total_distance = 0
    # red_car = board.vehicle_dict['X']
    # for col in range(red_car.col + red_car.size, board.dimension):
        # if board.board[red_car.row][col] != "_":
            # blocking_car_id = board.board[red_car.row][col]
            # blocking_car = board.vehicle_dict[blocking_car_id]
            # #if blocking_car.direction == 'H':
             # #   distance = abs(blocking_car.row - red_car.row)
            # #else:
             # #   distance = abs(blocking_car.col - red_car.col)
            # #total_distance += distance
    # return total_distance

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
            blocking_car = board.vehicle_dict[blocking_car_id]
            #board.check_vertical_moves(blocking_car_id, blocking_car.row, 
            #                            blocking_car.col, blocking_car.size)
            #possible_moves_dict = board.possible_sets()
            movable_vehicles, possible_moves = board.generate_all_possible_moves()
            # print(f"board.movable_vehicles: {board.movable_vehicles}")
            # print(f"dictionary possible moves: {possible_moves}")
            if blocking_car_id in board.movable_vehicles:
                for Tuple in possible_moves[blocking_car_id]:
                    # print(Tuple)
                    free_space += len(Tuple[1])
    # print(free_space)
    return free_space

    # DONE
def total_moves_of_car_just_moved(board: 'Board') -> int:
    """
    Pre: board
    Post: score (as an int)
    A variable that determines how much a car has moved already, ranging from 0 to 10
    The score is relative to the total amount of cars moved
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
    score = round((just_moved_n_moved / total_cars_moved) * 10)
    
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
    
    