# Gas

## Introduction
Welcome to the Rush Hour project! This project focuses on solving Rush Hour puzzles using various algorithms and strategies.

Rush Hour is a puzzle game where the aim is to navigate a red car off the board by sliding other vehicles that obstruct its path. Vehicles can only be moved horizontally or vertically along their respective rows, and the red car can only exit in a straight line. One move consist out if any empty blocks that. 1

## Case Introduction

In this project, we tackle solving various Rush Hour boards:

* Board 1 to 3: These are 6 by 6 boards.
* Board 4 to 6: These are 9 by 9 boards and are more challenging.
* Board 7: This is a 12 by 12 board and is very challenging, requiring efficient solution algorithms.

To solve the boards, we implemented the following rule:

* Each vehicle can move within its lane provided it is not blocked by another vehicle.
* If there are multiple consecutive empty spaces in front of or behind a vehicle, it can move through all these spaces in a single move.


## Algorithm Descriptions
#### Random


#### Random with Heuristics


#### Breadth-First Search


#### Beam Search


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

For our project, we utilized the following algorithms: Random (R), Random with heuristics (RH), Breadth First Search (BFS), and Beam Search (BS). Here's a detailed guide on how to effectively run these algorithms and store results:

#### Explantion of `main.py`
The script `main.py` is designed to execute different algorithms based on command-line arguments. Here’s how it works:
##### Command Line Arguments
The script expects the following arguments to be passed when executing for the algorithms:
```bash
python3 main.py <game_number> <d> <algorithm> <runs> <shortest_path>
```
* `<game_number>`: Specifies the board configuration to run the algorithm on. There are 7 boards numbered sequentially from 1 to 7.
* `<d>`: Represents the dimension of the board.
    * Boards 1 to 3 have `d = 6`.
    * Boards 4 to 6 have `d = 9`.
    * Board 7 has `d = 12`.
* `<algorithm>`: Identifies the algorithm to execute:
    * `r` for Random.
    * `rh` for Random with heuristics.
    * `bf` for Breadth First Search.
    * `bs` for Beam Search.
* `<runs>`: Specifies the number of times the algorithm will be executed. Must be a positive integer.
* `<shortest_path>`: Selecting `yes` allows you to view a simulation based on previous runs specific to that board configuration. Selecting `no` initiates a new run of the algorithm on the chosen board.

##### Example Usage
To illustrate, here’s how you would run each algorithm for board configurations:

* Random Algorithm (r)
    ```bash
    python3 main.py 1 6 r 5 no
    ```
    * Executes Random algorithm on board 1 (`game_number = 1`), dimension `d = 6`, for 5 runs and no shortest path simulation.

* Random with heuristics (rh)
    ```bash
    python3 main.py 7 12 rh 100 no
    ```
    * Executes Random with heuristics on board 7 (`game_number = 7`), dimension `d = 12`, for 100 runs and no shortest path simulation.

* Breadth First Search (bf)
    ```bash
    python3 main.py 5 9 bf 1 no
    ```
    * Executes BFS on board 5 (game_number = 5), dimension `d = 9`, for 1 run and no shortest path simulation.

* Beam Search (bs)
    ```bash
    python3 main.py 2 6 bs 1 no
    ```
    * Executes Beam Search on board 2 (`game_number = 2`), dimension `d = 6`, for 1 runs and no shortest path simulation.


## Visualization Only
shortest_path can be set to `yes` or `no`. If set to `no`, the chosen algorithm is executed. If set to `yes`, the script assumes the algorithm has been run previously and you wish to view the simulation of that solution. For `r`, `rh`, and `bs`, when choosing to run with yes, you will be prompted:
```bash
What is the name of the dataset you wish to access? 
``` 
Here, you will type the full file name, with `bf` you don't have to enter any file name. 

##### Example of short path simualtion
```bash
python3 main.py 2 6 bs 1 yes
```
* Executes Beam Search on board 2 (`game_number = 2`), dimension `d = 6`, for 1 runs and shortest path simulation.

##### Explanation
* Argument Parsing: The script uses `sys.argv` to parse and interpret these command-line arguments.
* Algorithm Execution: Based on the specified algorithm (`r`, `rh`, `bf`, `bs`), the script initiates the corresponding algorithmic process.
* Shortest Path Simulation: When set to `yes`, you can view the simulation of the solving board. When set to `no`, the algorithm runs on the chosen board.
* Data Handling: Results from each run or iteration are typically stored in the appropriate directory under `data` for further analysis.

This guide provides a clear understanding of how to use `main.py` and how each parameter affects its operation, ensuring effective execution and result visualization for your project.

## Calculating Spate Space
By running this code, you can print all the calculated state spaces of the boards. The state space is the number of possible states a single board can occupy. A formula has been devised to calculate this state space, which you can learn more about in the presentation on 27/6/2024 or by examining the code itself. To find the state spaces, navigate to the `code`. 
```bash
python3 statespace.py
```
## Experiment setup
For these experiments, you need to run the bs (Beam Search) and the bf (Breadth First Search) algorithms. The instructions for running them in the terminal are described above in the "Running the Algorithms" section.

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
Before excuting the BS and BF commands delete the `results_bs.csv` file and the `results_bf.csv` in the `Experiments` directory. 
Run the aforementioned BFS commands for each board. Subsequently, execute the BS commands for each board using the specified beam width options below and always set the heuristic weight value to 0.25.

##### Beam Width Selection
For beam search, select the following beam widths:
* Board 1: Try beam widths 50, 100, 200.
* Board 2: Try beam widths 50, 100, 200, 300, 400.
* Board 3: Try beam widths 100, 200, 300, 400, 500.

##### Visualization
After running each commands for BFS and BS, the results including the number of board states, moves, and the chosen beam width will be saved in a CSV file for each board. This CSV file can then be used to visualize and compare the performance of BFS and BS across different beam widths for each board. 

##### Generating Graphs 
To generate graphs from the CSV files, follow these steps:
##### Step 1: Generate BS Graphs
1. Navigate to the `Experiments` directory.
2. Execute the following command in the terminal:
```bash
python3 graphs_for_ex1.py
```
These scripts will automatically process data from the CSV files to produce graphs for analysis.

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

