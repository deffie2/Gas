from representatie import Board
from randomise import move_car_random

def main():
    board = Board(6)
    board.places_car()
    board.printboard()

    # Check if the red car is already at the exit
    if board.is_red_car_at_exit():
        print("Red car is already at the exit! You won.")
        return

    for i in range(10):
        print(f"Move {i + 1}")
        move_car_random(board)
        if board.is_red_car_at_exit():
            print("Red car reached the exit! You won.")
            break
    else:
        print("Red car did not reach the exit after 2 moves.")

if __name__ == "__main__":
    main()