import numpy as np 
import matplotlib.pyplot as plt 

y = np.loadtxt("prob4.txt")

# making a exponential for fitting
def f(x):
	return( 2*np.exp(- 2*x ))  # for mean to be 0.5
num_arr = np.arange( np.amin(y), np.amax(y)+0.001, 0.001)  # making the number array
fit_fn = f(num_arr)

plt.plot(num_arr, fit_fn,'r')
plt.hist(y, density = True, bins=100)
plt.title('Histogram of exponentially distributed random numbers')
plt.xlabel('number')
plt.ylabel('frequency')
plt.show()
