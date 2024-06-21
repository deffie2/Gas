import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib as mpl
import csv
import time
import matplotlib.cm as cm

def visualize(d: int, game_number: int ):
    """ 
    Uses data of the initial positon of the cars and all the moves, 
    for each move the position of the car gets updated. With this updated data, 
    a new game state gets plotted

    pre: dimension (d) and game_number (game_number)
    """

    cars_in_game = import_table(d, game_number)
    cars_in_game = colors(cars_in_game)
    fig, ax = plt.subplots()
    plotting_grid(ax, cars_in_game, 0, d, game_number)
    car_moves_data = car_moves(d, game_number, cars_in_game)

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
            plotting_grid(ax, cars_in_game, move, d, game_number)
    plt.show()

def import_table(d, game_number):
    """ 
    Collects data of the cars and their initial positions 

    pre: dimension and game number
    post: dictionary with the car id as key value and the row, colomn, width an heigt as the key

    """
    cars_in_game = {}
    with open(f'../../data/Rushhour_games/Rushhour{d}x{d}_{game_number}.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
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

def colors(cars_in_game):
    """
    Assigns a color to each car, picked out of the "gist_ncar" colormap of matplotlip

    pre: dictionary with car id as key and postiontion as value 
    post: returns same dictionary, but now with color added to the value
    
    """
    n_cars = len(cars_in_game)
    cmap = mpl.colormaps["gist_ncar"]
    colors = cmap(np.linspace(0, 1, n_cars))
    color_index = 0
    for car_id in cars_in_game.keys():
        if car_id == 'X':
            cars_in_game[car_id].append('red')
        else:
            cars_in_game[car_id].append(colors[color_index])
            color_index += 1

    return cars_in_game

def car_moves(d, game_number, cars_in_game):
    """
    Collects data of the moves of the cars.

    pre: table with car_id and their moves
    post: a list with for each move a list with car_id, direction and move
    """

    car_moves_data = []
    with open(f'../../data/Breadth_First/Best_Moves/board_{game_number}_{d}x{d}.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            car_id = row[0]
            steps = int(row[1])
            width = cars_in_game[car_id][2]
            print(width)
            car_moves_data.append((car_id, steps, width))
    print(car_moves_data)
    return car_moves_data



def plotting_grid(ax, cars_in_game, move, d, game_number):
    """
    Plotting the game.

    pre: the axes object, dictionary with car_id as key and postions as value, 
    move count and dimension and game_number
    post: a plot

    """
    ax.clear()

    # making the grid
    for i in range(d + 1):
        ax.axhline(i, color='black', linestyle='-', linewidth=1)  # Horizontal grid lines
        ax.axvline(i, color='black', linestyle='-', linewidth=1)  # Vertical grid lines

    # adding cars as rectangles to the grid
    for car_id, values in cars_in_game.items():
        row, col, width, height, color = values  
        rect = patches.Rectangle((col, row), width, height, linewidth=1, edgecolor='black', facecolor=color)
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
    car_moves_data= car_moves(d, game_number, cars_in_game)
    if move != len(car_moves_data):
        plt.title(f'Move {move}')
    else:
        plt.title(f'You won! You had a total of {move} moves!')
    
    # border around the grid
    for spine in ax.spines.values():
        spine.set_linewidth(8)

    # updating the plot
    plt.draw()
    # pause of 0,5 seconds
    plt.pause(0.5) 


# Main script
if __name__ == "__main__":
    d = 6  # Example grid size
    game_number = 1  # Example game number
    visualize(d, game_number)