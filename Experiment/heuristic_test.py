import pytest
from code.classes.board import Board 

example_board = [
    ['_', 'A', 'A', 'B', 'B', 'B'],
    ['_', 'C', 'C', 'E', 'D', 'D'],
    ['X', 'X', 'G', 'E', '_', 'I'],
    ['F', 'F', 'G', 'H', 'H', 'I'],
    ['K', '_', 'L', '_', 'J', 'J'],
    ['K', '_', 'L', '_', '_', '_']
]

def setup_board():
    return Board(example_board)

def test_distance_for_red_car(setup_board):
    expected_distance = 6  # Expected distance for red car 'X'
    actual_distance = setup_board.distance_for_red_car()
    assert actual_distance == expected_distance

def test_count_blocking_cars(setup_board):
    expected_count = 4  # Expected number of cars blocking red car 'X'
    actual_count = setup_board.count_blocking_cars()
    assert actual_count == expected_count

def test_free_space_blocking_cars(setup_board):
    expected_free_space = 3  # Expected total free spaces for blocking cars
    actual_free_space = setup_board.free_space_blocking_cars()
    assert actual_free_space == expected_free_space

def test_total_moves_of_car_just_moved(setup_board):
    expected_moves = 5  # Expected total moves made by just moved cars
    actual_moves = setup_board.total_moves_of_car_just_moved()
    assert actual_moves == expected_moves