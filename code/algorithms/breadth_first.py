import copy
import csv


from code.classes.board import Board
from code.classes.queue import Queue
from typing import List, Optional, Tuple


def breadth_first_search(d, game_number, runs):
    """
    Perform breadth-first search on the given initial board to find a path
    where the red car reaches the exit.
    """
    csv_name = None
    for i in range(runs):

        initial_board = Board(d, game_number)
        
        # Initialize the queue and parents dictionary for the search
        queue, parents = initialize_search(initial_board)

        # Nu ga je checken als de queue niet leeg is
        while not queue.is_empty():
            # Get the current state from the queue and pop it
            current_board = queue.dequeue()
            # print(current_board)

            # Check if the initial state is already a winning state
            if current_board.is_red_car_at_exit():
                queue.clear()
                solution = reconstruct_path(parents, hash(current_board))

                # Save the solution to the CSV file
                csv_name = save_solution_to_csv(solution, d, game_number)
                break  # Break after finding the solution for this run

            # Verwerk de mogelijke zetten vanuit de huidige toestand van het bord
            process_moves(current_board, queue, parents)

    if csv_name:
        return csv_name
    return None

def initialize_search(initial_bord):
    """Initializes the queue and parents dictionary for the search."""
    # Create een queue om toestanden van het bord en bijbehorende moves te beheren
    queue = Queue()
    # Bijhouden van de ouders van elk bord voor pad reconstructie
    parents = {}

    # Enqueue the initial board and mark it as visited
    queue.enqueue(initial_bord)
    initial_state = hash(initial_bord)
    parents[initial_state] = None

    return queue, parents


def process_moves(current_board: Board, queue: Queue, parents: dict):
    """
    Generate and process all possible moves from the current board state.

    """
    movable_vehicles, possible_moves = current_board.generate_all_possible_moves()

    for car_id in movable_vehicles:
        for move_direction, step_list in possible_moves[car_id]:
            for steps in step_list:
                # Maak een kopie van het bord en voer de zet uit
                #new_board = copy.deepcopy(current_board)
                new_board = current_board.move_vehicle(car_id, steps)
                
                # BEAM: Geef elk nieuw bord een waarde
                    # -> Gebeurd met heuristics functie
                    
                # BEAM: Sla het new_board op in een datastructuur:
                    #- Datastructuur kan gesorteerd worden
                    #- De Heuristicswaarde, (de auto en het aantal stappen?), het bord
                
                # BEAM: OUT OF LOOP: Sorteer de scores van de mogelijke borden
                
                # BEAM: OUT OF LOOP: Indexeer alleen de beste BEAM (int) borden op basis van heuristicswaarde
                
                # BEAM: Restart the same loop
                
                new_board_state = hash(new_board.get_board_state())

                # Controleer of de nieuwe toestand al is bezocht
                if new_board_state not in queue.visited_state:
                    queue.enqueue(new_board)
                    parents[new_board_state] = (hash(current_board.get_board_state()), car_id, steps)
                    # print(f"Key: {new_board_state}, Value: {parents[new_board_state]}")
                    # new_board.printboard()
                    # print()
    # print("move_klaar")



def reconstruct_path(parents: dict, state: int):
    """
    Reconstruct the path from the goal state back to the initial state using parent relationships.
    """
    path = []
    while parents[state] is not None:
        # Haal de ouderstaat en de bijbehorende zet op
        parent_state, car_id, steps = parents[state]
        # Voeg de zet toe aan het pad
        path.append([car_id, steps])
        # Update de huidige toestand naar de ouderstaat voor de volgende iteratie
        state = parent_state
    # Keer het pad om zodat het van begin naar eind gaat
    return path[::-1]

def save_solution_to_csv(solution, d, game_number):
    """
    Save the solution path to a CSV file.
    """
    file_path = f'data/Breadth_First/Best_Moves/board_{game_number}_{d}x{d}.csv'
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Car', 'Step'])
        for move in solution:
            writer.writerow(move)
        print(f"Moves successfully saved to {file_path}")

    return file_path





