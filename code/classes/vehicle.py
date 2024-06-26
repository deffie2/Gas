import copy


class Vehicle:

    def __init__(self, car: str, direction: str, x: int, y: int, Size: int) -> None:
        """
        Initialize multiple variables.
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

        post: List filled with tuple coordinates
        """
        self.vehicle_positions = []
        for i in range(self.size):
            if self.direction == "H":
                self.vehicle_positions.append((self.row, self.col + i))
            elif self.direction == "V":
                self.vehicle_positions.append((self.row + i, self.col))
        return self.vehicle_positions

    def locationchange(self, x: int, y: int) -> None:
        """
        Changes the location of the vehicle.
        Pre: x and y coordinates
        Post: self.row and self.col will be changed,
        if the amount of times moved will be changed
        """

        new_car = copy.copy(self)

        new_car.n_times_moved += 1
        new_car.locationHead = [x, y]
        new_car.row = x
        new_car.col = y

        return new_car
