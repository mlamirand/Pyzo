import matplotlib.pyplot as plt
import numpy
data = numpy.genfromtxt(
    fname = 'C:\\Users\\Monica\\Desktop\\REU - UW\\Datasets\\MicroarrayExpression (6).csv',
    delimiter = ',',
    usecols = (1,),
    )

plt.hist(data, bins=20, cumulative=True)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()