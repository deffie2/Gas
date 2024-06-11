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
    
    #asking dimension
    d = int(input("What is the dimension? "))

    #asking how many runs
    runs = int(input("How many times do you want to run the simulation? "))

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