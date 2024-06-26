import numpy as np
import matplotlib.pyplot as plt
import csv

def frequency_graph(name_data: str, algorithm: str) -> None:
    """
    Input: name of CSV file
    Output: Plots a Histogram of moves for a certain board
    """

    list_of_n_moves = []

    if algorithm == "WOH":
        # Open file and save data in list
        with open(f'{name_data}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for item in row:
                    item = int(item.lstrip('\ufeff'))
                    list_of_n_moves.append(item)

    elif algorithm == "WH":
        # Open file and save data in list
        with open(f'{name_data}') as csv_file:
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

    name_new_file = str(input("How do you want to name your new png-file? "))

    if algorithm == "WOH":
        # Save the plot to a file
        plt.savefig(f'data/Graphs/Random/Freq_graph_WOH/{name_new_file}.png')
        print("Saving succesfull")
    elif algorithm == "WH":
        # Save the plot to a file
        plt.savefig(f'data/Graphs/Random/Freq_graph_WH/{name_new_file}.png')
        print("Saving succesfull")
    else:
        print("Saving not succesfull, wrong alogrithm")


if __name__ == "__main__":
    name_data = str(input("What is the name of the dataset you wish to access? "))
    algorithm = str(input("What algorithm do you want to save? "))
    frequency_graph(name_data, algorithm)
