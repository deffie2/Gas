from representatie import Board
from randomise import move_car_random
import csv

if __name__ == "__main__":
    
    from sys import argv

    # Load the requested game or else game 1
    if len(argv) == 1:
        game_number = "1"
    elif len(argv) == 2:
        game_number = argv[1]
    
    d = int(input("What is the dimension?"))

    # Call board

   
    
    runs = int(input("How many times do you want to run the simulation?"))

    # Check if the red car is already at the exit
    #if board.is_red_car_at_exit():
        #print("Red car is already at the exit! You won.")
        #return

    moveslist = []
    # All the runs
    for i in range(runs):
        board = Board(d, game_number)
        board.places_car()
        moves = 0
        # A single run
        while not (board.is_red_car_at_exit()):
            move_car_random(board)
            moves += 1
        print(f"Board {game_number} took {moves} moves")
        moveslist.append(moves)

    
    
    
    #if board.is_red_car_at_exit():
    #    print("Red car reached the exit! You won!")
     #   print(f"It took{moves} moves")
      #  break
    