import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib as mpl
import csv
import time
import matplotlib.cm as cm

def visualize(d, game_number):

    # Define car positions and sizes (example)
    cars_in_game = import_table(d, game_number)
    cars_in_game = colors(cars_in_game)
    fig, ax = plt.subplots()
    plotting_grid(ax, cars_in_game, 0, d, game_number)

    car_moves_data = car_moves(d, game_number)


    move = 1
    print(move)
    for car_id, direction, steps in car_moves_data:
        if car_id in cars_in_game:
            for i in range(abs(steps)):

                if direction == 'R':  # Move right
                    cars_in_game[car_id][1] += 1
                    print(car_id)
                    print(cars_in_game)
                elif direction == 'L':  # Move left
                    cars_in_game[car_id][1] -= 1
                elif direction == 'U':  # Move up
                    cars_in_game[car_id][0] -= 1
                elif direction == 'D':  # Move down
                    cars_in_game[car_id][0] += 1
                plotting_grid(ax, cars_in_game, move, d, game_number)
                print(car_id)
            move += 1
            print(move)

def import_table(d, game_number):
    cars_in_game = {}
    with open(f'../../data/Rushhour_games/Rushhour{d}x{d}_{game_number}.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            car_id = row[0]
            direction = row[1]
            row_pos = int(row[3])-1
            col_pos = int(row[2])-1

            if direction == 'H':
                width = int(row[4])
                height = 1
            else:
                width = 1
                height = int(row[4])
            

            cars_in_game[car_id] = [row_pos, col_pos, width, height]

    return cars_in_game

def colors(cars_in_game):
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


def plotting_grid(ax, cars_in_game, move, d, game_number):
    ax.clear()

    for i in range(d + 1):
        ax.axhline(i, color='black', linestyle='-', linewidth=1)  # Horizontal grid lines
        ax.axvline(i, color='black', linestyle='-', linewidth=1)  # Vertical grid lines
    print(cars_in_game)

    for car_id, values in cars_in_game.items():
        row = values[0]
        col = values[1]
        width = values[2]
        height = values[3]
        color = values[4]  
        rect = patches.Rectangle((col, row), width, height, linewidth=1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)

    # Set labels and limits
    ax.set_xticks(np.arange(d + 1))
    ax.set_yticks(np.arange(d + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    ax.set_xlim(0, d)
    ax.set_ylim(0, d)
    ax.set_aspect('equal')
    ax.invert_yaxis()

    car_moves_data= car_moves(d, game_number)
    if move != len(car_moves_data):
        plt.title(f'Move {move}')
    else:
        plt.title(f'You won! You had a total of {move} moves!')
    
    for spine in ax.spines.values():
        spine.set_linewidth(8)


    plt.draw()
    plt.pause(0.3) 


def car_moves(d, game_number):
    car_moves_data = []
    with open(f'../../data/Random/Best_Moves_WOH/r_best_move_{game_number}_{d}x{d}.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            car_id = row[0]
            direction = row[1]
            steps = int(row[2])
            car_moves_data.append((car_id, direction, steps))
    car_moves_data 

    return car_moves_data

# Main script
if __name__ == "__main__":
    d = 9  # Example grid size
    game_number = 4  # Example game number
    visualize(d, game_number)