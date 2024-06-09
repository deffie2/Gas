class Node:
    def __init__(self, vehicle_dict: dict):
        self.vehicle_dict = vehicle_dict
        self.last_moved_vehicle = None

    def update_vehicle_status(self, vehicle_key: str, new_col: int, new_row: int):
        if vehicle_key in self.vehicle_dict:
            orientation, _, _, length, _ = self.vehicle_dict[vehicle_key]

            # Build a new tuple with the desired values
            updated_vehicle = (orientation, new_col, new_row, length, True)

            self.vehicle_dict[vehicle_key] = updated_vehicle
            # Reset the status of the previously moved vehicle, if there is one
            if self.last_moved_vehicle:
                self.vehicle_dict[self.last_moved_vehicle] = self.vehicle_dict[self.last_moved_vehicle][:-1] + (False)
            
            # Update the last moved vehicle
            self.last_moved_vehicle = vehicle_key
            return True
        return False