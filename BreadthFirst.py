import queue
import copy

def move_care_breadth_first():
    depth = 50                   # No deeper than "depth"       
    queue = queue.Queue()
    queue.put("")               # Add begin state to queue
    while not queue.empty():
        state = queue.get()
        print(state)
        if len(state) < depth:
            for i in ["L","R"]: # Wat is hier L en R? -> welke auto of hoeveel? 
            # -> allebei leidt tot een beweging, dus beide nodig
                child = copy.deepcopy(state) # deepcopy the state
                child += i                   # make new child    
                queue.put(child)             # add new child        
