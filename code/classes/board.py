import csv
import hashlib


from code.classes.vehicle import Vehicle
from typing import List, Tuple, Dict, Set, Union
import copy


class Board:
    """
    Represents a game board for a Rush Hour-like puzzle game.

    Attributes:
        board (list): 2D list representing the game board.
        dimension (int): Size of the board (d x d).
        exit_coordinate (list): Coordinates of the exit.
        vehicle_dict (dict): Dictionary mapping vehicle IDs to Vehicle objects.
        movable_vehicles (set): Set of IDs of vehicles that can currently move.
        possible_moves_dict (dict): Dictionary mapping vehicle IDs to their
        possible moves.
        move_history (list): List of previous moves made on the board.
    """
    def __init__(self, d: int, game_number: int) -> None:
        """
        Initializes a board object.

        pre: game_number >= 1  # Game number must be positive
        post: self.board is initialized, with vehicles placed on it. This
        also includes the dimension, the exit cordinate,
        a dictionary with vehicles, a set with movable vehicles,
        a dictionary of possible moves per vehicle and
        a datastructure that captures move history.
        """

        # Check of game_number can work
        assert game_number >= 1, "game_number must be positive non-zero number"

        # Initialize items in board
        self.board: List[List[str]] = []
        self.dimension: int = d
        self.createboard()
        self.exit_cordinate: List[int] = [round((d/2 - 1)), d - 1]
        self.vehicle_dict: Dict[str, Vehicle] = {}
        self.movable_vehicles: Set[str] = set()
        self.possible_moves_dict: Dict[str, List[Tuple[str, List[int]]]] = {}
        self.move_history: List[List[Union[str, int]]] = []

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

                # Save vehicle as object in dict
                vehicle = Vehicle(car, direction, xcor, ycor, Size)
                self.vehicle_dict[car] = vehicle

        # Place cars onto the board
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
        Computes the SHA3-512 hash value of the current board state.

        post: Returns an integer hash value
        """
        state_str = str(self.get_board_state())
        new_hash = int(hashlib.sha3_512(state_str.encode('utf-8')).hexdigest(), 16)
        return new_hash

    def __lt__(self, other):
        """
        Less than comparison for Board objects.
        """
        return len(self.move_history) < len(other.move_history)

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

        pre: self.vehicle_dict exist and consists of car IDs and vehicle objects
        post: Vehicles are placed on self.board according to
        their initial positions
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

    def check_horizontal_moves(self, car_id: str, car_row: int, car_col: int, car_length: int) -> None:
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

    def check_vertical_moves(self, car_id: str, car_row: int, car_col: int, car_length: int) -> None:
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

    def move_vehicle(self, car_id: str, step: int) -> "Board":
        """
        Moves a vehicle on the board.

        pre: car_id in self.vehicle_dict.keys()  # Vehicle ID must exist in vehicle_dict
        pre: step > 0  # Step must be positive
        post: Vehicle is moved on the board, and the board state is updated
        """
        assert car_id in self.vehicle_dict.keys(), f"Vehicle ID '{car_id}' must exist in vehicle_dict"

        # Make a copy of board
        new_board = copy.copy(self)
        new_board.move_history = copy.copy(new_board.move_history)
        new_board.vehicle_dict = copy.copy(new_board.vehicle_dict)

        # Reset justmoved for all vehicles to False
        for carID, vehicles in self.vehicle_dict.items():
            vehicles.justmoved = False

        # Vind vehicle and new coordinates
        vehicle = self.vehicle_dict[car_id]
        if vehicle.direction == 'H':
            new_col = vehicle.col + step
            new_row = vehicle.row
        elif vehicle.direction == 'V':
            new_col = vehicle.col
            new_row = vehicle.row + step

        # Change justmoved from vehicle
        vehicle.justmoved = True

        # Append move to move history
        new_board.move_history.append([car_id, step])

        # Move the vehicle to the new position
        new_vehicle = vehicle.locationchange(new_row, new_col)
        new_board.vehicle_dict[new_vehicle.car] = new_vehicle

        # Update the board
        new_board.update_board()

        return new_board

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
                print(f"{self.board[i][j]:>2}", end='')
            print()
        print()

    def get_board_state(self) -> Tuple[Tuple[str, ...], ...]:
        """
        Gets the current state of the board.

        post: Returns the current board state as a tuple of tuples
        """
        return tuple(map(tuple, self.board))

    def heuri_red_clear_exit(self) -> bool:
        """
        Returns true if the way to the exit is clear for the red car.
        Otherwise it returns false.
        pre: Nothing
        post: Boolean
        """
        red_car = self.vehicle_dict.get('X', None)

        for i in range(red_car.col + 2, self.dimension, 1):
            if not (self.exit_cordinate[0], i) in self.empty_places():
                return False
        return True

    def heuri_get_red_to_exit(self) -> None:
        """
        When the path is free of vehicles for the red car,
        the red car will move to the exit.
        post: Moves red_car to the exit
        """
        # Checks if the way is clear
        if self.heuri_red_clear_exit():

            # How much should red car move?
            red_car = self.vehicle_dict.get('X', None)
            steps = self.dimension - red_car.col - 2

            # Moves red car by that amount
            return self.move_vehicle("X", steps)

    def heuri_change_moveable_cars(self) -> set:
        """
        Reproduces the data structure of moveable cars,
        but it takes out the car that was just moved.

        pre: self.moveable_vehicle exists as a set
        pre: self.vehicle_dict exists as a dictionary
        post: Set of (new) moveable cars
        """
        vehicle_id_with_just_moved = "Empty"

        # What car was just moved?
        for car_id, vehicle in self.vehicle_dict.items():
            if vehicle.justmoved:
                vehicle_id_with_just_moved = car_id
                break

        # Take car out of the data structure
        if not vehicle_id_with_just_moved == "Empty" and not len(self.movable_vehicles) == 1:
            self.movable_vehicles.remove(vehicle_id_with_just_moved)

        return self.movable_vehicles
