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
