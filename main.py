from representatie import Board
from randomise import move_car_random
import csv

if __name__ == "__main__":

    # Call board
    #board = Board(6)
    #board.places_car()
    #board.printboard()
    
    runs = input("How many times do you want to run the simulation? ")

    # Check if the red car is already at the exit
    #if board.is_red_car_at_exit():
        #print("Red car is already at the exit! You won.")
        #return
        
    moveslist = []
    # All the runs
    for i in runs:
    
        moves = 0
        # Call board
        board = Board(6)
        board.places_car()
        board.printboard()
        # A single run
        while not (board.is_red_car_at_exit()):
            move_car_random(board)
            moves += 1
        print(f"It took {moves} moves")
        moveslist.append(moves)
    
    
    
    #if board.is_red_car_at_exit():
    #    print("Red car reached the exit! You won!")
     #   print(f"It took{moves} moves")
      #  break
    