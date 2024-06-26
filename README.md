# Gas

## Introduction
Welcome to the Rush Hour project! This project focuses on solving Rush Hour puzzles using various algorithms and strategies.

Rush Hour is a puzzle game where the aim is to navigate a red car off the board by sliding other vehicles that obstruct its path. Vehicles can only be moved horizontally or vertically along their respective rows, and the red car can only exit in a straight line.

## Case Introduction

In this project, we tackle solving various Rush Hour boards:

* Board 1 to 3: Simple setups to get familiar with the game and basic strategies.
* Board 4 to 6: More challenging boards requiring efficient solution algorithms.
* Board 7: A special challenge that may require adjustments to our algorithms.

## Implementation
We have developed a Python implementation for Rush Hour, utilizing a board representation and different search algorithms to find solutions. Below is how you can set up and run the project:

## Installation

1. Clone de repository:
```bash
git clone https://github.com/deffie2/Gas.git
```
2. Installeer de vereiste pakketten:
```bash
python3 -m pip install -r requirements.txt
```
## Running the Algorithms

Leg uit hoe de commands werken in de main en hoe alles werkt en opgeslagen wordt. random, BFS en BS



## Experiment setup

### Running Board Commands
To excute the experiments, run commands for each specified board configuration:

#### Breadth-First Search (BFS)
Run boards 1, 2, and 3 using the following commands:

* **Board 1:**
```bash
python3 main.py 1 6 bf 1 v no
```
* **Board 2:**
```bash
python3 main.py 2 6 bf 1 v no
```
* **Board 3:**
```bash
python3 main.py 3 6 bf 1 v no
```
#### Beam Search (BS)
For boards 1, 2, and 3, run BS with beam width selection:
* **Board 1:**
```bash
python3 main.py 1 6 bs 1 v no
```
* **Board 2:**
```bash
python3 main.py 2 6 bs 1 v no
```
* **Board 3:**
```bash
python3 main.py 3 6 bs 1 v no
```

##### Note
During the execution of BS commands in this experiment, you will be prompted to enter both a beam width value and a heuristic weight-value.

When prompted during the beam search commands, follow these steps:
```arduino
What value would you like for the beam width? <enter beam width value>
```
Enter your desired integer value for the beam width.

```arduino
What heuristics weight-value would you like to test? <enter heuristic weight-value>
```
Enter your desired heuristic weight-value.

### Experiment 1
##### Objective
Evaluate the performance of breadth-first search (BFS) and beam search (BS) algorithms on boards of varying dimensions and configurations, aiming to identify beam widths for BS that achieve comparable move counts to BFS and finding the optimal beam width.

##### Conducting BFS and BS
Run the aforementioned BFS commands for each board. Subsequently, execute the BS commands for each board using the specified beam width options below and always set the heuristic weight value to 0.25.

##### Beam Width Selection
For beam search, select the following beam widths:
* Board 1: Try beam widths 50, 100, 200.
* Board 2: Try beam widths 50, 100, 200, 300, 400.
* Board 3: Try beam widths 100, 200, 300, 400, 500.

##### Visualization
After running each commands for BFS and BS, the results including the number of board states, moves, and the chosen beam width will be saved in a CSV file for each board. This CSV file can then be used to visualize and compare the performance of BFS and BS across different beam widths for each board. 

##### Generating Graphs 
To generate graphs and tables from the CSV files, follow these steps:
##### Step 1: Generate BS Graphs
1. Navigate to the `Experiments` directory.
2. Execute the following command in the terminal:
```bash
python3 graphs_for_ex1.py
```
##### Step 2: Generate BFS and BS Tables
1. Navigate to the `Experiments` directory.
2. Execute the following command in the terminal:
```bash
python3 tabels_for_ex1.py
```
These scripts will automatically process data from the CSV files to produce graphs and tables for analysis.

### Experiment 2
Objective: We want to test if a specific heuristic actually creates better results. This will be tested by varying the weights for this heuristic from 0 to 0.5 in increments of 0.125. The heuristic we want to check, checks the relativity of the amount of the car that has just moved, with the average amount of moves of all cars. If the car that just moved, moved more that the average moves of all cars, the total score gets lower for this board. The lower the score the less chance the board will be selected. 

##### Conducting BS
Before excuting the BS commands delete the `results_bs.csv` file in the `Experiments` directory. 
Then Run the aforementioned BS commands for each board using a beam width of 100 and the heuristic weight-value options below.

##### Heuristic weight-value
For beam search, evalute the following heuristic weight-value:
* Board 1: Try 0, 0.125, 0.25, 0.375, 0.5.
* Board 2: Try 0, 0.125, 0.25, 0.375, 0.5.
* Board 3: Try 0, 0.125, 0.25, 0.375, 0.5.

##### Visualization
After excuting each BS command, the results including the number of board states, moves, chosen beam width and heuristic weight-value will be saved in a CSV file for each board. This CSV file can then be used to visualize and compare the performance of BS with different heuristic weight-values for each board. 

##### Generating Graphs 
To generate graphs from the CSV files, follow these steps:
##### Step 1: Generate BS Graphs
1. Navigate to the `Experiments` directory.
2. Execute the following command in the terminal:
```bash
python3 graphs_for_ex2.py
```
These scripts will automatically process data from the CSV files to produce graphs for analysis.

