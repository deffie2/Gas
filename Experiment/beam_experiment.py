import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib as mpl
import csv
import matplotlib.cm as cm
import random
import time

def beam_time_graph(name_data_time: str, algorithm: str) -> None:
    """
    Input: name of CSV file
    Output: Plots a Histogram of moves for a certain board
    """

    list_of_n_moves = []
    
    with open(f'{name_data_time}') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for item in row:
                item = int(item.lstrip('\ufeff'))
                list_of_n_moves.append(item)


    # Plot Histogram on x
    plt.hist(list_of_n_moves, rwidth=1.0, bins = 50)
    plt.xlabel('Amount of moves') 
    plt.ylabel('Frequency')
    plt.title('Randomise table')

