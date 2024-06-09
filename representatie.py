import csv


class Board:
    def __init__(self, d: int) -> None:
            self.board = []
            self.dimension = d
            self.createboard()
            self.exit_cordinate = [d/2,d]
            self.vehicle_dict = {}
            
            # Initialize vehicles
            with open('Rushhour6x6_1.csv', "r") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    key = row[0]
                    direction = row[1]
                    ycor = int(row[2])
                    xcor = int(row[3])
                    size = int(row[4])
                    
                    # Save vehicle as object in dict
                    vehicle = Vehicle(direction, xcor, ycor, size, vehicle_moved=False)
                    self.vehicle_dict[key] = vehicle

    def createboard(self) -> None:
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                row.append("_")
            self.board.append(row)

    def printboard(self) -> None:
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(f"{self.board[i][j]:>2}", end = '')
            print()

    #FUNCTIE Welke auto's zijn beweegbaar? -> Na elke move refresh
        # Loopen door alle auto's op het bord
            # Wat is voor en achter voor dit voertuig?
            # coordinaat pakken indexeren collum en row.
            # Als V of H -> x of y + en - 1 en size moet doen 
            # Is een van die locaties leeg?
            # Ja -> voeg auto aan lijst (dict?) toe
        # Return dict  
    
    def places_car(self) -> None:
        # Ga alle voertuigen af:
        for carkey, vehicle in self.vehicle_dict.items():
            for i in range(vehicle.size):
                if (vehicle.direction == "V"):
                    self.board[vehicle.row + i - 1][vehicle.col - 1] = carkey
                else:
                    self.board[vehicle.row - 1][vehicle.col + i - 1] = carkey
                    
    #FUNCTIE Locatie lege plekken
        # Alle coordinaten - coordinatenvoertuigen (LET OP DAT DIT KAN VOOR HET DATATYPE) (Set)
    #FUNCTIE Beweeg voertuig
        # Vraag voertuigletter
        # Verander voertuig dmv FUNCTIE LOCATIE in voertuigen class
    # Bevat einddoellocatie rood
    # Visualiserend het bord met verschillende kleuren. 
    # Donkergrijze border om d bij d lichtgrijs bord

    # Voertuigen
class Vehicle:
    def __init__(self, direction, x, y, size: int, vehicle_moved=False) -> None:
        self.size = size
        self.direction = direction 
        self.locationHead = [x, y]
        self.row = x
        self.col = y
        self.locationtot = []
        self.vehicle_moved = vehicle_moved
        
        #self.justmoved = False
        self.n_times_moved = 0
        
    # FUNCTIE LOCATIE
    def locationchange(self, x, y) -> None:
        self.n_times_moved += 1
        # Verander locatie -> nieuwe coordinaten
        
    def __repr__(self) -> str:
        return f"Vehicle({self.direction},{self.col},{self.row},{self.size},{self.vehicle_moved})"

# MAIN: 
if __name__ == "__main__":
    board = Board(6)
    board.places_car()
    board.printboard()
    
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
    

