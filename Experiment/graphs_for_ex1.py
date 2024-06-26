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
    
    # Grafiek 1: Tijd versus Beamwidth
    plt.figure(figsize=(15, 5))  # Grootte van de figuur aanpassen indien nodig
    plt.subplot(1, 3, 1)  # Eerste grafiek (1 rij, 3 kolommen, eerste positie)
    plt.plot(df_board['Beam Width', df_board['Time']], marker='o')
    plt.title(f'Board {board_number}: Time versus Beam Width')
    plt.xlabel('Beam Width')
    plt.ylabel('Time')

    # Grafiek 2: State Space versus Beamwidth
    plt.subplot(1, 3, 2)  # Tweede grafiek (1 rij, 3 kolommen, tweede positie)
    plt.plot(df_board['Board states'], df_board['Beam Width'], marker='o')
    plt.title(f'Board {board_number}: State Space versus Beam Width')
    plt.xlabel('State Space')
    plt.ylabel('Beam Width')

    # Grafiek 3: Moves versus Beamwidth
    plt.subplot(1, 3, 3)  # Derde grafiek (1 rij, 3 kolommen, derde positie)
    plt.plot(df_board['Moves'], df_board['Beam Width'], marker='o')
    plt.title(f'Board {board_number}: Moves versus Beam Width')
    plt.xlabel('Moves')
    plt.ylabel('Beam Width')

    # Automatische uitlijning van de subplots
    plt.tight_layout()

    # Toon de grafieken voor dit boardnummer
    plt.show()