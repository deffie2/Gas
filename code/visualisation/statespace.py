# Berken statespace
import math

def calculate_Statespace(b: int, totla: int, nauto: int)-> int:
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
if __name__ == "__main__":
    print(math.factorial(7) / (math.factorial(2)* math.factorial(5)))
    print(math.factorial(6) / (math.factorial(2)* math.factorial(4)))
    kolom = 21 * 8 * 8 * 7* 8 * 15 * 21 * 15
    rij = 7 * 8 * 8 * 21 * 15 * 21 * 15 * 8
    print(kolom * rij)