# Gas

## Installation

1. Clone de repository:
```bash
git clone https://github.com/deffie2/Gas.git
```
2. Installeer de vereiste pakketten:
```bash
python3 -m pip install -r requirements.txt
```
## Experiment
### Experiment 1
Objective: Evaluate the performance of breadth-first search (BFS) and beam search (BS) algorithms on boards of varying dimensions and configurations, aiming to identify beam widths for BS that achieve comparable move counts to BFS and finding the optimal beam width.

#### Breadth-First Search (BFS)

Boards and Parameters:

* Board 1: Run BFS.
```bash
python main.py 1 <dimension> bf <runs> v no
```
Replace <dimension> and <runs> accordingly.
* Board 2: Run BFS.
```bash
python main.py 2 <dimension> bf <runs> v no
```
Replace <dimension> and <runs> accordingly.
* Board 3: Run BFS.
```bash
python main.py 3 <dimension> bf <runs> v no
```
Replace <dimension> and <runs> accordingly.

#### Beam Search (BS)

Boards and Parameters:

* Board 1: Run BS with beam width selection.
```bash
python main.py 1 <dimension> bs <runs> v no
```
Replace <dimension> and <runs> accordingly.
* Board 2: Run BS with beam width selection.
```bash
python main.py 2 <dimension> bs <runs> v no
```
Replace <dimension> and <runs> accordingly.
* Board 3:  Run BS with beam width selection.
```bash
python main.py 3 <dimension> bs <runs> v no
```
Replace <dimension> and <runs> accordingly.
##### Beam Width Selection

For beam search, select the following beam widths:
* Board 1: Try beam widths 50, 100, 200.
* Board 2: Try beam widths 50, 100, 200, 300, 400.
* Board 3: Try beam widths 100, 200, 300, 400, 500.

During execution of the beam search commands, you will be prompted to enter the beam width value:
```bash
What value would you like for the beam width? <enter beam width value>
```
Enter your desired integer value for the beam width when prompted.

##### Visualization

After running each command (either BFS or BS), the results including the number of board states, moves, and the chosen beam width will be saved in a CSV file for each board. This CSV file can then be used to visualize and compare the performance of BFS and BS across different beam widths for each board. 

##### Generating Graphs 
To generate graphs from the CSV files, follow these steps:

1. Navigate to the Experiments directory.
2. Execute the following command in the terminal:
```bash
python3 graphs_for_ex1.py
```
This script will load the data from the CSV files and automatically generate graphs for time versus beam width, board states versus beam width, and moves versus beam width for each board.

By providing these instructions, you outline how to conduct the experiment, specify beam widths for BS, save results in CSV format, and generate visualizations for analysis.


### Experiment 2
Objective: Objective: Normalize heuristic values which currently rely heavily on empty spaces, aiming to improve algorithm performance of beam search across different board configurations and dimensions.