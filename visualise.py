#

import numpy as np
import matplotlib.pyplot as plt

def frequency_graph(list_of_n_moves) -> None:
    #%matplotlib inline
    #plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
    
    # Plot Histogram on x
    plt.hist(list_of_n_moves, bins=1)
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
    

if __name__ == "__main__":
    list1 = [1,1,4,5,2,2,4,4,4,7,9]
    frequency_graph(list1)