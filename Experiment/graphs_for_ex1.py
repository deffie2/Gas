import pandas as pd
import matplotlib.pyplot as plt
import csv

# Step 1: Load data from CSV file
df = pd.read_csv('results_bs.csv')

# Step 2: Filter data for 'bs' algorithm
df_bs = df[df['Algorithm'] == 'bs']

# Step 3: Get unique board numbers for bs algorithm
board_numbers = df_bs['Board'].unique()

# Step 4: Plot graphs for each board number
for board_number in board_numbers:
    # Subset of data for the current board number and 'bs' algorithm
    df_board = df_bs[df_bs['Board'] == board_number]
    
    # Grafiek 1: Time versus Beamwidth
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.plot(df_board['Time'], df_board['Beam Width'], marker='o')
    plt.title(f'Board {board_number}: Time versus Beam Width')
    plt.xlabel('Time')
    plt.ylabel('Beam Width')

    # Grafiek 2: State Space versus Beamwidth
    plt.subplot(1, 3, 2)
    plt.plot(df_board['Board States'], df_board['Beam Width'], marker='o')
    plt.title(f'Board {board_number}: State Space versus Beam Width')
    plt.xlabel('State Space')
    plt.ylabel('Beam Width')

    # Grafiek 3: Moves versus Beamwidth
    plt.subplot(1, 3, 3)
    plt.plot(df_board['Moves'], df_board['Beam Width'], marker='o')
    plt.title(f'Board {board_number}: Moves versus Beam Width')
    plt.xlabel('Moves')
    plt.ylabel('Beam Width')

    # Determine where you want to save the graph.
    save_path = f'./board_{board_number}'
    plt.savefig(save_path)
    plt.show()
