import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data = pd.read_csv('results_bs.csv')

colors = ['b', 'g', 'r']
markers = ['o', 's', 'D']

expected_heuristic_values = [i * 0.125 for i in range(9)]

plt.figure(figsize=(12, 8))  

#run the graph for each board
for i in range(1, 4):
    
    filtered_data = data[(data['Board'] == i) & 
                        (data['Beam Width'] == 100) & (data['heuristic_weight_value'] % 0.125 == 0)]
                        
    # Sorts the filtered data by heuristic_weight_value
    filtered_data = filtered_data.sort_values(by='heuristic_weight_value')
    
    actual_heuristic_values = filtered_data['heuristic_weight_value'].tolist()

    # 9 rows because the title of the csv file is still there
    assert len(filtered_data) == 9, f"Expected 9 rows, but found {len(filtered_data)} for board {i}"
    missing_values = set(expected_heuristic_values) - set(actual_heuristic_values)
    assert not missing_values, f"Missing heuristic values: {missing_values} for Board {i}"

    plt.plot(filtered_data['heuristic_weight_value'], filtered_data['Moves'], 
             marker=markers[i-1], color=colors[i-1], label=f'Board {i}', markersize=8)
    
# layout of the plot
plt.xlabel('Heuristic weight value', fontsize=16, labelpad=20)
plt.ylabel('Number of moves', fontsize=16, labelpad=20)
plt.title('Heuristic weight vs. Number of moves for boards 1, 2, and 3', fontsize=18, fontweight='bold')
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.xticks(expected_heuristic_values, fontsize=14)  
plt.yticks(fontsize=14)
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:0.0f}"))  
plt.legend(fontsize=14)

# Show the plot
plt.show()
