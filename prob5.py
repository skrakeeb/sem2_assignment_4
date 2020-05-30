'''
coded by: rakeeb
coded for: Box Muller method for gaussian distribution
'''


import numpy as np 
import matplotlib.pyplot as plt 


n = 10000
mu = 0     # mean
sigma = 1  # variance
# creating two uniform deviates
x1 = np.random.rand(n)
x2 = np.random.rand(n)
# creating gaussian distribution using Box- Muller technique
y1 = mu + sigma* np.sqrt( -2* np.log(x1))* np.cos(2*np.pi * x2)
y2 = mu + sigma* np.sqrt( -2* np.log(x1))* np.sin(2*np.pi * x2)

# making a gaussian for fitting
def f(x):
	return((1/ (sigma* np.sqrt(2*np.pi))) *np.exp(- ((x-mu)/sigma)**2 /2))
num_arr = np.arange( np.amin(y1), np.amax(y1)+0.001, 0.001)  # making the number array
fit_fn = f(num_arr)

plt.plot(num_arr, fit_fn,'r')		
plt.hist(y1, density = True)
plt.title('Gaussian distribution of random numbers')
plt.show()