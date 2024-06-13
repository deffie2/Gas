import numpy as np
import matplotlib.pyplot as plt
import csv

def frequency_graph(name_data: str, name_new_file: str) -> None:
    """
    Input: name of CSV file
    Output: Plots a Histogram of moves for a certain board
    """

    list_of_n_moves = []
    
    # Open file and save data in list
    with open(f"data/Freq_moves_table/Random/{name_data}") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for item in row:
                item = int(item.lstrip('\ufeff'))
                list_of_n_moves.append(item)
            
    # Plot Histogram on x
    plt.hist(list_of_n_moves, rwidth=1.0)
    plt.xlabel('Amount of moves')
    plt.ylabel('Frequency')
    plt.title('Randomise table')
    
    # Save the plot to a file
    plt.savefig(f'data/Freq_graph/Random/{name_new_file}.png')


if __name__ == "__main__":
    name_data = str(input("What is the name of the dataset you wish to access? "))
    name_new_file = str(input("How do you want to name your new png-file? "))
    frequency_graph(name_data, name_new_file)