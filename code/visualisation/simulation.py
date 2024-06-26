import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib.axes import Axes
import csv
import random
import time
from typing import Dict, List, Union, Tuple


def visualize(d: int, game_number: int, csv_names: str) -> None:
    """
    Uses data of the initial positon of the cars and all the moves,
    for each move the position of the car gets updated. With this
    updated data, a new game state gets plotted

    pre: d is a positive integer that indicates the size of the board,
    pre: game_number is a valid that identifies for game board.
    pre: csv_names is a string that represents the path to the csvfile
    with the moves you want to visualize.

    """
    cars_in_game = import_table(d, game_number)
    colors = get_colors(cars_in_game)
    cars_in_game = assinging_colors(colors, cars_in_game)
    fig, ax = plt.subplots()
    plotting_grid(ax, cars_in_game, 0, d, csv_names)
    car_moves_data = car_moves(csv_names, cars_in_game)

    move = 0
    for car_id, steps, width in car_moves_data:
        if car_id in cars_in_game:
            move += 1
            for i in range(abs(steps)):
                if width > 1:
                    if steps > 0:
                        cars_in_game[car_id][1] += 1
                    else:
                        cars_in_game[car_id][1] -= 1
                elif width == 1:
                    if steps > 0:
                        cars_in_game[car_id][0] += 1
                    else:
                        cars_in_game[car_id][0] -= 1
            plotting_grid(ax, cars_in_game, move, d, csv_names)
    plt.show(block=False)
    time.sleep(10)
    plt.close()


def import_table(d: int, game_number: int) -> Dict[str, List[int]]:
    """ 
    Collects data of the cars and their initial positions.

    pre: dimension and game number.
    post: cars_in_game is a dictionary with car_id as key (character), and row,
    column number, width and height as values.
    """
    cars_in_game = {}
    with open(f'data/Rushhour_games/Rushhour{d}x{d}_{game_number}.csv', "r") \
        as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for line in reader:
            car_id = line[0]
            direction = line[1]
            row = int(line[3])-1
            col = int(line[2])-1
            if direction == 'H':
                width = int(line[4])
                height = 1
            elif direction == 'V':
                width = 1
                height = int(line[4])
            cars_in_game[car_id] = [row, col, width, height]
    return cars_in_game


def get_colors(cars_in_game: Dict[str, List[int]]) -> List[List[float]]:
    """
    Creating a list of colors with the same length as the amount of cars. 
    The color gets picked from a color spectrum.

    pre: cars_in_game is a dictionary with car_id as key (character), and row, 
    column number, width and height (positive integers) as values.
    post:  colors.tolist is a list of colors codes from matplotlib.
    """
    n_cars = len(cars_in_game)
    cmap = mpl.colormaps["nipy_spectral"]
    colors = cmap(np.linspace(0.05, 0.80, n_cars))

    return colors.tolist()
    

def picking_random_colors(colors: List[List[float]]) -> List[float]:
    """
    Picking a random color out of the color list.

    pre: colors is a list of color codes from matplotlib
    post: color is a random color out of the list
    """
    random_index = random.randint(0, len(colors) - 1)
    color = colors.pop(random_index)
    return color

def assinging_colors(colors: List[List[float]], cars_in_game: \
                    Dict[str, List[int]]) -> \
                        Dict[str, List[Union[int, List[float], str]]]:
    """
    Each car gets a random color assigned, the car with
    car_id "X' gets the color red assigned

    pre: colors is a list of color codes from matplotlib
    pre:  cars_in_game is a dictionary with car_id as key (character), and row,
    column number, width and height (positive integers) as values
    post: cars_in_game is a dictionary with car_id as key (character), and row,
    column number, width and height(positive integers) AND the color
    (list of floats or str fot the red car) as value
    """
    for car_id in cars_in_game.keys():
        if car_id == 'X':
            cars_in_game[car_id].append('red')
        else:
            cars_in_game[car_id].append(picking_random_colors(colors))
    return cars_in_game


def car_moves(csv_names: str, cars_in_game: Dict[str, \
        List[Union[int, List[float], str]]]) -> List[Tuple[str, int, int]]:
    """
    Reads car move data from a CSV file and returns a list of
    tuples containing information about each car move, including width,
    which is needed to know the orientation of the car.

    pre: csv_names is a string that represents the path to the csvfile
    with the moves you want to visualize.
    post: a list with tuples which contain the car_id as string, steps
    as positive or negative integers and width as positive integer.
    """
    car_moves_data = []
    with open(f'{csv_names}') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            car_id = row[0]
            steps = int(row[1])
            width = cars_in_game[car_id][2]
            car_moves_data.append((car_id, steps, width))
    return car_moves_data


def plotting_grid(ax: Axes, cars_in_game: \
                  Dict[str, List[Union[int, List[float], str]]], \
                      move: int, d: int, csv_names: str) -> None:
    """
    Plotting the game.

    pre: the axes object.
    pre: cars_in_game is a dictionary with car_id as key (character), and row,
    column number, width and height(positive integers) AND the color
    (list of floats or str fot the red car) as value.
    pre: move count is a positive integer.
    pre: d is a positive integer that indicates the size of the board.
    pre: game_number is a valid that identifies for game board.

    post: a plot representing the cars and their moves.

    """
    ax.clear()

    # making the grid
    for i in range(d + 1):
        ax.axhline(i, color='black', linestyle='-', linewidth=1)
        ax.axvline(i, color='black', linestyle='-', linewidth=1)

    # adding cars as rectangles to the grid
    for car_id, values in cars_in_game.items():
        row, col, width, height, color = values  
        rect = patches.Rectangle((col, row), width, height, linewidth=1, \
                                 edgecolor='black', facecolor=color)
        ax.add_patch(rect)

    # settings grid
    ax.set_xticks(np.arange(d + 1))
    ax.set_yticks(np.arange(d + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    ax.set_xlim(0, d)
    ax.set_ylim(0, d)
    ax.set_aspect('equal')
    ax.invert_yaxis()

    # title of plot
    car_moves_data = car_moves(csv_names, cars_in_game)
    if move != len(car_moves_data):
        plt.title(f'Move {move}')
    else:
        plt.title(f"Well done! You completed the game in {move} moves!")
    
    # border around the grid
    for spine in ax.spines.values():
        spine.set_linewidth(8)

    # updating the plot
    plt.draw()
    # pause of 0,5 seconds
    plt.pause(0.5) 

