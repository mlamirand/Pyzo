import matplotlib.pyplot as plt
import numpy as np

    
def main():

    data = np.genfromtxt(
    fname = 'C:\\Users\\Monica\\Desktop\\REU - UW\\Datasets\\normalized_microarray_donor9861\\MicroarrayExpression.csv',
    delimiter = ',',
    invalid_raise = False,
    )
    
    x = np.transpose(data[45808:45809,1:])
    
    plt.hist(x, bins = 20)
    
main()