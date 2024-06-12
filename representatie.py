import csv


class Board:
    def __init__(self, d: int, game_number:int) -> None:
            self.board = []
            self.dimension = d
            self.createboard()
            self.exit_cordinate = [(d/2 - 1), d - 1]
            self.vehicle_dict = {}
            self.movable_vehicles = set()
            self.possible_moves_dict = {}
            self.move_history = []

            

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

                    # Save vehicle as object in dict
                    vehicle = Vehicle(car, direction, xcor, ycor, Size)
                    self.vehicle_dict[car] = vehicle
      

    def createboard(self) -> None:
        # Create an empty board with dimensions d x d
        self.board = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                row.append("_")
            self.board.append(row)

    def places_car(self) -> None:
        # Place all vehicles on the board
        for carkey, vehicle in self.vehicle_dict.items():
            for i in range(vehicle.size):
                if (vehicle.direction == "V"):
                    self.board[vehicle.row + i][vehicle.col] = carkey
                else:
                    self.board[vehicle.row][vehicle.col + i] = carkey

    def empty_places(self) -> list:
        # Find all empty spaces on the board
        self.empty_space = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.board[i][j] == "_"):
                    empty_place_tuple = (i, j)
                    self.empty_space.append(empty_place_tuple)
        return self.empty_space

    def vehicles_moveable(self):
        # Determine which vehicles can move
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

    def possible_sets(self):
        # Determine all possible moves for each movable vehicle
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

    def check_horizontal_moves(self, car_id, car_row, car_col, car_length):
        # Check possible moves to the left
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

    def check_vertical_moves(self, car_id, car_row, car_col, car_length):
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

    def is_red_car_at_exit(self) -> bool:
        # assert in plaats van false toevoegen
        assert self.vehicle_dict.get('X') is not None

        # Check if the red car is at the exit
        red_car = self.vehicle_dict.get('X', None)
        red_car_end_col = (red_car.col) + red_car.size - 1
        if red_car.direction == 'H' and (red_car.row) == self.exit_cordinate[0] and red_car_end_col == self.exit_cordinate[1]:
            return True
        return False

    def  move_vehicle(self, car_id, move_direction, step):
        # Move a vehicle in the specified direction by the given number of steps
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
        # Update the board after moving a vehicle
        self.createboard()
        self.places_car()
        # checken als empty_places weg kan. 
        self.empty_places()

    def printboard(self) -> None:
        # Print the current state of the board
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(f"{self.board[i][j]:>2}", end = '')
            print()
    
    
    # Bevat einddoellocatie rood
    # Visualiserend het bord met verschillende kleuren.
    # Donkergrijze border om d bij d lichtgrijs bord

    # Voertuigen


class Vehicle:
    def __init__(self, car, direction, x, y, Size: int) -> None:
        self.car = car 
        self.size = Size
        self.direction = direction 
        self.locationHead = [x, y]
        self.row = x
        self.col = y
        self.vehicle_positions = []
    
        # self.justmoved = False
        self.n_times_moved = 0
     
    def vehiclepositions(self):
        self.vehicle_positions = []
        for i in range(self.size):
            if self.direction == "H":
                self.vehicle_positions.append((self.row, self.col + i))
            elif self.direction == "V":
                self.vehicle_positions.append((self.row + i, self.col))
        return self.vehicle_positions


    # FUNCTIE LOCATIE
    def locationchange(self, x, y) -> None:
        self.n_times_moved += 1
        self.locationHead = [x, y]
        self.row = x
        self.col = y
        # Verander locatie -> nieuwe coordinaten

    # functie om beide locaties te hebben, om get makkelijker op te vragen. 

    def __repr__(self) -> str:
        return f"Vehicle({self.direction},{self.col},{self.row},{self.size})"

# MAIN: 
if __name__ == "__main__":


    board = Board(6,1)
    board.places_car()
    board.printboard()
    print(board.empty_places())
    print(board.vehicles_moveable())
    board.possible_sets()
    print(board.possible_moves_dict)

    # Check of rode auto pad vrij heeft (als er niks staat voor de rode auto)
        # Ja -> +1 move, beweeg rode auto naar einde, end game
    # Nee ga door
    # Eerst checken welke autos op dit moment schuifbaar zijn, dus lege plekken voor of achter zich hebben

    # Hoeveel is die auto schuifbaar? (dus -1 tot + 2 bijv)
        # Ga bij die auto van -1 totdat het geen lege plek meer is (while loop)
            # Sla data ergens op
        # Ga bij de auto van +1 totdat het geen lege plek meer is (while loop)
            # Sla data ergens op
    # Random 1 auto kiezen? -> later niet random
    # Random plaatsverandering +1 move (een random cijfer van verplaatsbaarheid dat niet 0 is) -> later niet random
    # Plaatsverandering opgeslaan.
    
    # Als endgame publiceer move
