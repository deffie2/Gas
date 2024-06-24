import math

def calculate_statespace_row(b: int, totla: int, nauto: int)-> int:
    """
    Pre: 
    - b = the length of the row or collum
    - totla = the total lenght of the vehicles combined
    - nauto = the amount of vehicles
    Post: 
    - An int 
    Calculates the statespace for a single row or collum.
    """
    # Calculate n and k
    n = b - totla + nauto
    k = nauto
    
    # Calculate the amount of option for that row
    statespace = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    return statespace
    
def calculate_statespace_multiple(listrow: list[list[int]], listcol: list[list[int]]) -> int:
    """
    Pre:
    - listrow: contains the b, totla and nauto per row (see function calculate_statespace_row)
    - listcol: contains the b, totla and nauto per row (see function calculate_statespace_row)
    Post:
    - An int: which is the total statespace of that board.
    Calculates the total statespace of a board.
    """
    # Initialize statespace as 1 (because 1 * a = a)
    statespace = 1
    
    # Loop over the listrow
    for i in range(len(listrow)):
        state_this_row = calculate_statespace_row(listrow[i][0], listrow[i][1], listrow[i][2])
        statespace *= state_this_row
        
    # Loop over listcol
    for i in range(len(listcol)):
        state_this_col = calculate_statespace_row(listcol[i][0], listcol[i][1], listcol[i][2])
        statespace *= state_this_col

    return statespace
    
    
if __name__ == "__main__":
    
    # Game 1 rows and col
    row_input_game1 = [[6,5,2],[6,4,2],[6,2,1],[6,4,2],[6,2,1],[6,0,0]]
    col_input_game1 = [[6,2,1],[6,0,0],[6,4,2],[6,2,1],[6,0,0],[6,2,1]]
    
    # Game 2 rows and col
    row_input_game2 = [[6,4,2],[6,4,2],[6,2,1],[6,4,2],[6,2,1],[6,2,1]]
    col_input_game2 = [[6,2,1],[6,0,0],[6,0,0],[6,2,1],[6,2,1],[6,3,1]]
    
    # Game 3 rows and col
    row_input_game3 = [[6,2,1],[6,0,0],[6,2,1],[6,2,1],[6,2,1],[6,2,1]]
    col_input_game3 = [[6,2,1],[6,0,0],[6,3,1],[6,3,1],[6,0,0],[6,3,1]]
        
    # Game 4 rows and col
    row_input_game4 = [[9,3,1],[9,3,1],[9,0,0],[9,5,1],[9,2,1],[9,3,2],[9,4,2],[9,0,0],[9,7,3]]
    col_input_game4 = [[9,6,3],[9,0,0],[9,3,1],[9,7,3],[9,2,1],[9,3,1],[9,0,0],[9,0,0],[9,6,2]]
    
    # Game 5 rows and col
    row_input_game5 = [[9,3,1],[9,2,1],[9,2,1],[9,4,2],[9,5,2],[9,0,0],[9,4,2],[9,5,2],[9,2,1]]
    col_input_game5 = [[9,4,2],[9,2,1],[9,2,1],[9,3,1],[9,2,1],[9,5,2],[9,4,2],[9,0,0],[9,5,2]]
    
    # Game 6 rows and col
    row_input_game6 = [[9,4,2],[9,5,2],[9,4,2],[9,3,1],[9,2,1],[9,4,2],[9,5,2],[9,4,2],[9,3,1]]
    col_input_game6 = [[9,5,2],[9,2,1],[9,2,1],[9,3,1],[9,7,3],[9,2,1],[9,0,0],[9,2,1],[9,3,1]]
    
    # Game 7 rows and col
    row_input_game7 = [[12,5,2],[12,0,0],[12,7,3],[12,4,2],[12,6,2],[12,2,1],[12,5,2],[12,7,3],[12,8,3],[12,5,2],[12,0,0],[12,7,3]]
    col_input_game7 = [[12,5,2],[12,3,1],[12,2,1],[12,2,1],[12,2,1],[12,6,3],[12,11,4],[12,2,1],[12,0,0],[12,4,2],[12,5,2],[12,6,3]]
    
    # Calculate gamestates for all games
    statespace_1 = calculate_statespace_multiple(row_input_game1, col_input_game1)
    statespace_2 = calculate_statespace_multiple(row_input_game2, col_input_game2)
    statespace_3 = calculate_statespace_multiple(row_input_game3, col_input_game3)
    statespace_4 = calculate_statespace_multiple(row_input_game4, col_input_game4)
    statespace_5 = calculate_statespace_multiple(row_input_game5, col_input_game5)
    statespace_6 = calculate_statespace_multiple(row_input_game6, col_input_game6)
    statespace_7 = calculate_statespace_multiple(row_input_game6, col_input_game7)
    
    print(f"Statespace for game 1: {statespace_1:.2e}")
    print(f"Statespace for game 2: {statespace_2:.2e}")
    print(f"Statespace for game 3: {statespace_3:.2e}")
    print(f"Statespace for game 4: {statespace_4:.2e}")
    print(f"Statespace for game 5: {statespace_5:.2e}")
    print(f"Statespace for game 6: {statespace_6:.2e}")
    print(f"Statespace for game 7: {statespace_7:.2e}")