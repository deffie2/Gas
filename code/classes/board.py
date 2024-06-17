import csv
import math
import os


from code.classes.vehicle import Vehicle
from typing import List, Tuple, Dict, Set, Union

#############################
# Om het te testen: python3 board.py
# from vehicle import Vehicle
###########################


class Board:
    """  
    Represents a game board for a Rush Hour-like puzzle game.

    Attributes:
        board (list): 2D list representing the game board.
        dimension (int): Size of the board (d x d).
        exit_coordinate (list): Coordinates of the exit.
        vehicle_dict (dict): Dictionary mapping vehicle IDs to Vehicle objects.
        movable_vehicles (set): Set of IDs of vehicles that can currently move.
        possible_moves_dict (dict): Dictionary mapping vehicle IDs to their possible moves.
        move_history (list): List of previous moves made on the board.
    """
    def __init__(self, d: int, game_number:int) -> None:
        """
        Initializes a board object.

        pre: game_number >= 1  # Game number must be positive
        post: self.board is initialized with empty spaces
        post: self.vehicle_dict is populated with vehicles from CSV
        """
        assert game_number >= 1, "game_number must be greater than or equal to 1"
        self.board: List[List[str]] = []
        self.dimension: int = d
        self.createboard()
        self.exit_cordinate: List[int] = [round((d/2 - 1)), d - 1]
        self.vehicle_dict: Dict[str, Vehicle] = {}
        self.movable_vehicles: Set[str] = set()
        self.possible_moves_dict: Dict[str, List[Tuple[str, List[int]]]] = {}
        self.move_history: List[List[Union[str, int]]] = []


        ####################################################################
        # # Om het te testen: python3 board.py
        # current_dir = os.path.dirname(__file__)  # Geeft het pad naar de huidige map van dit script
        # csv_path = os.path.join(current_dir, '..', '..', 'data', 'Rushhour_games', f'Rushhour{d}x{d}_{game_number}.csv')

        #   # waardes van row en colum direct wijzigen met -1 in de x en y coordinats.
        # # Initialize vehicles from the CSV file
        # with open(csv_path, "r") as csvfile:
        #     reader = csv.reader(csvfile)
        #     next(reader)
        #     for row in reader:
        #         car = row[0]
        #         direction = row[1]
        #         ycor = int(row[2]) - 1
        #         xcor = int(row[3]) - 1
        #         Size = int(row[4])

        ##################################################################

        # waardes van row en colum direct wijzigen met -1 in de x en y coordinats.
        # Initialize vehicles from the CSV file
        with open(f'data/Rushhour_games/Rushhour{d}x{d}_{game_number}.csv', "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                car = row[0]
                direction = row[1]
                ycor = int(row[2]) - 1
                xcor = int(row[3]) - 1
                Size = int(row[4])
        ##############################################################

                # Save vehicle as object in dict
                vehicle = Vehicle(car, direction, xcor, ycor, Size)
                self.vehicle_dict[car] = vehicle

        self.places_car()

    def __eq__(self, other) -> bool:
        """
        Compares two Board objects for equality.

        pre: isinstance(other, Board)  # Other object must be of type Board
        post: Returns True if boards are equal, False otherwise
        """
        if isinstance(other, Board):
            return self.board == other.board
        else:
            return NotImplemented

    def __hash__(self) -> int:
        """
        Computes the hash value of the current board state.

        post: Returns an integer hash value
        """
        return hash(self.get_board_state())

    def createboard(self) -> None:
        """
        Creates an empty board with dimensions self.dimension x self.dimension.

        post: self.board is initialized with '_' in all cells
        """
        self.board = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                row.append("_")
            self.board.append(row)

    def places_car(self) -> None:
        """
        Places all vehicles on the board based on their initial positions.

        post: Vehicles are placed on self.board according to their initial positions
        """
        for carkey, vehicle in self.vehicle_dict.items():
            for i in range(vehicle.size):
                if (vehicle.direction == "V"):
                    self.board[vehicle.row + i][vehicle.col] = carkey
                else:
                    self.board[vehicle.row][vehicle.col + i] = carkey

    def empty_places(self) -> List[Tuple[int, int]]:
        """
        Finds all empty spaces on the board.

        post: Returns a list of tuples representing empty spaces on the board
        """
        self.empty_space = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.board[i][j] == "_"):
                    empty_place_tuple = (i, j)
                    self.empty_space.append(empty_place_tuple)
        return self.empty_space

    def vehicles_moveable(self) -> Set[str]:
        """
        Determines which vehicles can move.

        post: Returns a set of IDs of vehicles that can currently move
        """
        self.movable_vehicles = set()
        for carkey, vehicle in self.vehicle_dict.items():
            car_orientation = vehicle.direction
            # zoek beide coordinaten per auto . misschien verplaatseen naar vehicle class

            vehicle = self.vehicle_dict[carkey]
            vehicle_positions = vehicle.vehiclepositions()

            for pos_row, pos_col in vehicle_positions:
                if car_orientation == 'H':
                    for (new_row, new_col) in self.empty_space:
                        if (pos_row, pos_col + 1) == (new_row, new_col) or \
                            (pos_row, pos_col - 1) == (new_row, new_col):
                            self.movable_vehicles.add(carkey)
                elif car_orientation == 'V':
                    for (new_row, new_col) in self.empty_space:
                        if (pos_row + 1, pos_col) == (new_row, new_col) or \
                            (pos_row - 1, pos_col) == (new_row, new_col):
                            self.movable_vehicles.add(carkey)
        return self.movable_vehicles

    def possible_sets(self) -> Dict[str, List[Tuple[str, List[int]]]]:
        """
        Determines all possible moves for each movable vehicle.

        post: Returns a dictionary mapping vehicle IDs to lists of possible moves
        """
        self.possible_moves_dict = {}
        for car_id in self.movable_vehicles:
                self.possible_moves_dict[car_id] = []
                vehicle = self.vehicle_dict[car_id]
                car_orientation = vehicle.direction
                car_col = vehicle.col
                car_row = vehicle.row
                car_length = vehicle.size
                if car_orientation == 'H':
                    self.check_horizontal_moves(car_id, car_row, car_col, car_length)
                elif car_orientation == 'V':
                    self.check_vertical_moves(car_id, car_row, car_col, car_length)
        return self.possible_moves_dict

    def check_horizontal_moves(self, car_id: str, car_row: int, car_col: int, car_length: int ) -> None:
        """
        Checks possible horizontal moves for a vehicle.

        pre: car_id in self.vehicle_dict.keys()  # Vehicle ID must exist in vehicle_dict
        post: Appends possible horizontal moves to self.possible_moves_dict[car_id]
        """
        # Check possible moves to the left
        assert car_id in self.vehicle_dict.keys(), f"Vehicle ID '{car_id}' must exist in vehicle_dict"
        move_steps_left = []
        for j in range(car_col - 1, -1, -1):
            if self.board[car_row][j] == "_":
                move_steps_left.append(j - car_col)
            else:
                break
        if move_steps_left:
            self.possible_moves_dict[car_id].append(('L', move_steps_left))

        # Check possible moves to the right
        move_steps_right = []
        for j in range(car_col + car_length, self.dimension):
            if self.board[car_row][j] == "_":
                move_steps_right.append(j - car_col - car_length + 1)
            else:
                break
        if move_steps_right:
            self.possible_moves_dict[car_id].append(('R', move_steps_right))

    def check_vertical_moves(self, car_id: str, car_row: int, car_col: int, car_length: int ) -> None:
        """
        Checks possible vertical moves for a vehicle.

        pre: car_id in self.vehicle_dict.keys()  # Vehicle ID must exist in vehicle_dict
        post: Appends possible vertical moves to self.possible_moves_dict[car_id]
        """
        assert car_id in self.vehicle_dict.keys(), f"Vehicle ID '{car_id}' must exist in vehicle_dict"
        # Check possible moves upward
        move_steps_up = []
        for i in range(car_row - 1, -1, -1):
            if self.board[i][car_col] == "_":
                move_steps_up.append(i - car_row)
            else:
                break
        if move_steps_up:
            self.possible_moves_dict[car_id].append(('U', move_steps_up))

        # Check possible moves downward
        move_steps_down = []
        for i in range(car_row + car_length, self.dimension):
            if self.board[i][car_col] == "_":
                move_steps_down.append(i - car_row - car_length + 1)
            else:
                break
        if move_steps_down:
            self.possible_moves_dict[car_id].append(('D', move_steps_down))

    def generate_all_possible_moves(self) -> Tuple[Set[str], Dict[str, List[Tuple[str, List[int]]]]]:
        """
        Generates all possible moves for movable vehicles.

        post: Returns a tuple containing movable vehicles (set) and their possible moves (dict)
        """
        empty_spaces = self.empty_places()
        movable_vehicles = self.vehicles_moveable()
        possible_moves = self.possible_sets()
        return movable_vehicles, possible_moves

    def is_red_car_at_exit(self) -> bool:
        """
        Checks if the red car has reached the exit.

        post: Returns True if the red car is at the exit, False otherwise
        """
        # assert in plaats van false toevoegen
        assert self.vehicle_dict.get('X') is not None

        # Check if the red car is at the exit
        red_car = self.vehicle_dict.get('X', None)
        red_car_end_col = (red_car.col) + red_car.size - 1
        if red_car.direction == 'H' and (red_car.row) == self.exit_cordinate[0] and red_car_end_col == self.exit_cordinate[1]:
            return True
        return False

    def move_vehicle(self, car_id: str, move_direction: str, step: int) -> None:
        """
        Moves a vehicle on the board.

        pre: car_id in self.vehicle_dict.keys()  # Vehicle ID must exist in vehicle_dict
        pre: move_direction in ['L', 'R', 'U', 'D']  # Valid move directions
        pre: step > 0  # Step must be positive
        post: Vehicle is moved on the board, and the board state is updated
        """
        assert car_id in self.vehicle_dict.keys(), f"Vehicle ID '{car_id}' must exist in vehicle_dict"
        assert move_direction in ['L', 'R', 'U', 'D'], f"Invalid move direction: {move_direction}"
        vehicle = self.vehicle_dict[car_id]
        if move_direction == 'L' or move_direction == 'R':
            new_col = vehicle.col + step
            new_row = vehicle.row
        elif move_direction == 'U' or move_direction == 'D':
            new_col = vehicle.col
            new_row = vehicle.row + step
        
        # Append move to move history
        self.move_history.append([car_id, move_direction, step])
      
        # Move the vehicle to the new position
        vehicle.locationchange(new_row, new_col)

        # Update the board
        self.update_board()

    def update_board(self) -> None:
        """
        Updates the board after moving a vehicle.

        post: self.board is updated to reflect the current positions of all vehicles
        """
        self.createboard()
        self.places_car()

    def printboard(self) -> None:
        """
        Prints the current state of the board.

        post: Prints the board to the console
        """
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(f"{self.board[i][j]:>2}", end = '')
            print()
    
    def heuri_red_clear_exit(self) -> bool:
        """
        Input: Nothing
        Output: Boolean
        Returns true if the way to the exit is clear for the red car.
        Otherwise it returns false.
        """
        red_car = self.vehicle_dict.get('X', None)
        
        for i in range(red_car.col + 2, self.dimension, 1):
            if not [self.exit_cordinate[0], i] in self.empty_places:
                return False
        return True
        
    def heuri_get_red_to_exit(self) -> None:
        """
        Input: Nothing
        Output: Moves red_car_to exit
        """
        
        # Checks if the way is clear
        if (heuri_red_clear_exit()):
        
            # How much should red car move?
            red_car = self.vehicle_dict.get('X', None)
            steps = self.dimension - red_car.col -1
        
            # Moves red car by that amount
            move_vehicle("X", "R", steps)

    def get_board_state(self) -> Tuple[Tuple[str, ...], ...]:
        """
        Gets the current state of the board.

        post: Returns the current board state as a tuple of tuples
        """
        return tuple(map(tuple, self.board))


# MAIN: 
if __name__ == "__main__":


    board = Board(9,6)
    board.printboard()
    print()
    hash(board)
    print(hash(board))
    print(board)
    print(board.get_board_state())

    # test eq__
    board1 = Board(6,1)
    board2 = Board(6,1)

    print(board1 is board2)
    print(board1 == board2)


    # board.places_car()
    # board.printboard()
    # board.printboard()
    # print(board.empty_places())
    # print(board.vehicles_moveable())
    # board.possible_sets()
    # print(board.possible_moves_dict)
    # print(board.exit_cordinate)
    # print(board.get_board_state())
