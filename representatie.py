import csv


class Board:
    def __init__(self, d: int) -> None:
            self.board = [] 
            self.dimension = d
            self.createboard()
            self.ExitCordinate = [d/2,d]
            self.VehicleDict = {}
            self.movable_vehicles = set()
            self.possible_moves_dict = {}
            
            # Initialize vehicles
            with open('data/Rushhour6x6_1.csv', "r") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    key = row[0]
                    direction = row[1]
                    ycor = int(row[2])
                    xcor = int(row[3])
                    Size = int(row[4])
                    
                    # Save vehicle as object in dict
                    vehicle = Vehicle(direction, xcor, ycor, Size)
                    self.VehicleDict[key] = vehicle


    def createboard(self) -> None:
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                row.append("_")
            self.board.append(row)


    def vehicles_moveable(self):
        for carkey, vehicle in self.VehicleDict.items():
            car_orientation = vehicle.direction
            car_col = vehicle.col
            car_row = vehicle.row
            car_length = vehicle.size

            vehicle_positions= []

            for i in range(car_length):
                if vehicle.direction == "H":
                    vehicle_positions.append((car_row - 1, car_col + i - 1))
                elif vehicle.direction == "V":
                    vehicle_positions.append((car_row + i - 1, car_col - 1))

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
        for car_id in self.movable_vehicles:
                self.possible_moves_dict[car_id] = []

        for car_id in self.movable_vehicles:
            vehicle = self.VehicleDict[car_id]
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
        # Controleer beweging naar links
        move_steps_left = []

        for j in range((car_col - 1) - 1, -1, -1):
            if self.board[car_row - 1][j] == "_":
                move_steps_left.append(j - (car_col - 1))
            else:
                break
        if move_steps_left:
            self.possible_moves_dict[car_id].append(('L', move_steps_left))

        # Controleer beweging naar rechts
        move_steps_right = []
        for j in range((car_col - 1) + car_length, self.dimension):
            if self.board[car_row - 1][j] == "_":
                move_steps_right.append(j - (car_col - 1) - car_length + 1)
            else:
                break
        if move_steps_right:
            self.possible_moves_dict[car_id].append(('R', move_steps_right))


    def check_vertical_moves(self, car_id, car_row, car_col, car_length):
        # Controleer beweging naar boven
        move_steps_up = []
        for i in range((car_row - 1) - 1, -1, -1):
            if self.board[i][car_col - 1] == "_":
                move_steps_up.append(i - (car_row - 1))
            else:
                break
        if move_steps_up:
            self.possible_moves_dict[car_id].append(('U', move_steps_up))

        # Controleer beweging naar beneden
        move_steps_down = []
        for i in range((car_row - 1) + car_length, self.dimension):
            if self.board[i][car_col - 1] == "_":
                move_steps_down.append(i - (car_row - 1) - car_length + 1)
            else:
                break
        if move_steps_down:
            self.possible_moves_dict[car_id].append(('D', move_steps_down))


    def places_car(self) -> None:
        # Ga alle voertuigen af:
        for carkey, vehicle in self.VehicleDict.items():
            for i in range(vehicle.size):
                if (vehicle.direction == "V"):
                    self.board[vehicle.row + i - 1][vehicle.col - 1] = carkey
                else:
                    self.board[vehicle.row - 1][vehicle.col + i - 1] = carkey
                    
    # FUNCTIE Locatie lege plekken
    def empty_places(self) -> list:
        self.empty_space = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.board[i][j] == "_"):
                    empty_place_tuple = (i,j)
                    self.empty_space.append(empty_place_tuple)
        return self.empty_space


    def printboard(self) -> None:
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(f"{self.board[i][j]:>2}", end = '')
            print()
    
    #FUNCTIE Beweeg voertuig
        # Vraag voertuigletter
        # Verander voertuig dmv FUNCTIE LOCATIE in voertuigen class
    # Bevat einddoellocatie rood
    # Visualiserend het bord met verschillende kleuren. 
    # Donkergrijze border om d bij d lichtgrijs bord

    # Voertuigen
class Vehicle:
    def __init__(self, direction, x, y, Size: int) -> None:
        self.size = Size
        self.direction = direction 
        self.locationHead = [x, y]
        self.row = x
        self.col = y
        self.locationtot = []
        
        #self.justmoved = False
        self.n_times_moved = 0
        
    # FUNCTIE LOCATIE
    def locationchange(self, x, y) -> None:
        self.n_times_moved += 1
        self.locationHead = [x, y]
        # Verander locatie -> nieuwe coordinaten
        
    def __repr__(self) -> str:
        return f"Vehicle({self.direction},{self.col},{self.row},{self.size})"

# MAIN: 
if __name__ == "__main__":
    board = Board(6)
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
    

