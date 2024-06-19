import copy

class Vehicle:

    def __init__(self, car, direction, x, y, Size: int) -> None:
        """
        Initialize multiple variables
        """
        self.car = car 
        self.size = Size
        self.direction = direction 
        self.locationHead = [x, y]
        self.row = x
        self.col = y
        self.vehicle_positions = []
    
        self.justmoved = False
        self.n_times_moved = 0
     
    def vehiclepositions(self) -> list:
        """
        Finds the coordinates on which the vehicle stands.
        For example a car of lenght 2 could stand on (1,2) and (1,3)
        """
        
        self.vehicle_positions = []
        for i in range(self.size):
            if self.direction == "H":
                self.vehicle_positions.append((self.row, self.col + i))
            elif self.direction == "V":
                self.vehicle_positions.append((self.row + i, self.col))
        return self.vehicle_positions


    # FUNCTIE LOCATIE
    def locationchange(self, x, y) -> None:
        """
        Changes the location of the vehicle.
        """
        self.n_times_moved += 1
        self.locationHead = [x, y]
        self.row = x
        self.col = y
        


        # new_car = copy.copy(self)

        # new_car.n_times_moved += 1
        # new_car.locationHead = [x, y]
        # new_car.row = x
        # new_car.col = y

        # return new_car
        # Verander locatie -> nieuwe coordinaten

    # functie om beide locaties te hebben, om get makkelijker op te vragen. 

    def __repr__(self) -> str:
        return f"Vehicle({self.direction},{self.col},{self.row},{self.size})"
