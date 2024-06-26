# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.patches as patches
# import matplotlib as mpl
# import csv
# import matplotlib.cm as cm
# import random
# import time

# def beam_time_graph(name_data_time: str, algorithm: str) -> None:
#     """
#     Input: name of CSV file
#     Output: Plots a Histogram of moves for a certain board
#     """

#     list_of_n_moves = []
    
#     with open(f'{name_data_time}') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for row in csv_reader:
#             for item in row:
#                 item = int(item.lstrip('\ufeff'))
#                 list_of_n_moves.append(item)


#     # Plot Histogram on x
#     plt.hist(list_of_n_moves, rwidth=1.0, bins = 50)
#     plt.xlabel('Amount of moves') 
#     plt.ylabel('Frequency')
#     plt.title('Randomise table')

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the CSV file
data = pd.read_csv('results_bs.csv')

# Define colors and styles for the plots
colors = ['b', 'g', 'r']
styles = ['-', '--', '-.']
markers = ['o', 's', 'D']

# Define the expected heuristic values
expected_heuristic_values = [i * 0.125 for i in range(9)]

for i in range(1, 4):
    # Filter the data for board i with beam width 100 and weight values from 0 to 1.0 in steps of 0.125
    filtered_data = data[(data['Board'] == i) & 
                        (data['Beam Width'] == 100) & (data['heuristic_weight_value'] % 0.125 == 0)]
                        
    # Sort the filtered data by heuristic_weight_value
    filtered_data = filtered_data.sort_values(by='heuristic_weight_value')

    # Debugging information to check filtered data
    print(f"\nFiltered data for Board {i}:\n", filtered_data)

    # Ensure there are exactly 8 rows and all expected heuristic values are present
    actual_heuristic_values = filtered_data['heuristic_weight_value'].tolist()
    print(f"Actual heuristic values for Board {i}: {actual_heuristic_values}")
    
    assert len(filtered_data) == 8, f"Expected 8 rows, but found {len(filtered_data)} for Board {i}"
    missing_values = set(expected_heuristic_values) - set(actual_heuristic_values)
    assert not missing_values, f"Missing heuristic values: {missing_values} for Board {i}"

    # Plot the heuristic values (weight_value) against the number of moves
    plt.figure(figsize=(12, 8))  # Increased figure size
    plt.plot(filtered_data['heuristic_weight_value'], filtered_data['Moves'], 
             marker=markers[i-1], linestyle=styles[i-1], color=colors[i-1], label=f'Board {i}', markersize=8)
    
    # Adding labels, title, and grid with increased font sizes, padding, and bold title
    plt.xlabel('Heuristic Weight Value', fontsize=16, labelpad=20)
    plt.ylabel('Number of Moves', fontsize=16, labelpad=20)
    plt.title(f'Board {i}: Heuristic Weight vs. Number of Moves', fontsize=18, fontweight='bold')
    plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
    plt.xticks(expected_heuristic_values, fontsize=14)  # Ensuring x-axis has ticks for each step with increased font size
    plt.yticks(fontsize=14)
    plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:0.0f}"))  # Remove decimal places from y-axis numbers
    plt.legend(fontsize=14)
    
    # Adding markers for each data point
    for x, y in zip(filtered_data['heuristic_weight_value'], filtered_data['Moves']):
        plt.text(x, y, f'{y}', fontsize=12, ha='right', va='bottom')

    plt.show()