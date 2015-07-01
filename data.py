
def importData(fileName):
    import numpy
    data = numpy.genfromtxt(fname = fileName,
    delimiter = ',',
    invalid_raise = False,
    )
    return data
    
def main():
   data = importData('C:\\Users\\Monica\\Desktop\\REU - UW\\Datasets\\normalized_microarray_donor9861\\MicroarrayExpression.csv')
   
   #dimension = 58,692 x 947
   print("The dimensions = ", data.shape)
   
   print("The type of elements of the array are ", data.dtype)
   
   #number of elements = 55,581,324
   print("The number of elements in the matrix is ", data.size)
   
   #maximum value = 18.3817518519
   print("The maximum value is ", np.amax(data[:,1:]))
   
   #minimum value = 1.47306631397
   print("The minimum value is ", np.amin(data))
   
   #mean value = 5.21651942865
   print("The mean value is ", np.mean(data[:,1:]))
   
   #standard deviation = 2.91795251025
   print("The standard deviation is ", np.std(data[:,1:]))
   
   #median value = 4.91474354466
   print("The median value is ", np.median(data[:,1:]))
   
   
main()