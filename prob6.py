'''
coded by: rakeeb
coded for: implimenting rejection method
'''


import numpy as np 
import matplotlib.pyplot as plt 


def f(x):
	return( np.sqrt(2/np.pi)* np.exp(-x**2 /2))

def g(x):
	return(1.5* np.exp(-x))
x_min = 0
x_max = 10
dx = 0.1
x_plot = np.arange(x_min, x_max+dx , dx)
y_max = np.amax( g(x_plot))

n_points = 10000
x = np.random.rand(n_points)
x = - np.log(x)
y = np.random.rand(n_points) * g(x)

y_good = y[y < f(x)]
x_good = x[y < f(x)]

y_bad = y[y > f(x)]
x_bad = x[y > f(x)]


plt.plot(x_plot ,f(x_plot),'r', label= 'Actual distribution to be made')
plt.plot(x_plot ,g(x_plot),'g', label= 'Approximating function')	
plt.scatter(x_good,y_good, color = 'orange', label= 'Good points to be selected')
plt.title('Plot of good points')
plt.legend()
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.ylim(0, 1.4)
plt.show()

plt.hist(x_good, density = True)
plt.plot(x_plot,f(x_plot),'r',label= 'Actual distribution to be made')
plt.title('Plot of PDF')
plt.legend()
plt.show()
