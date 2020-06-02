'''
coded by: rakeeb
coded for: computing MCMC 
'''

import numpy as np 
import matplotlib.pyplot as plt 


def f(x):            # function to be sampled
	if (3 < x < 7) :
		return(1.0)
	else :
		return(0.0)

nsteps = 10000  # no of steps to be computed
n_array = np.arange(1,nsteps+1,1)

theta = 0.0    # initial value 

sel_theta = np.zeros(nsteps)  # for storing the selected values of theta
theta_prime_arr = np.zeros(nsteps) # for  storing all values of theta_prime 

for i in range(nsteps):
    theta_prime=theta+np.random.standard_normal()  # taking the proposal PDF as standard gaussian
    r = np.random.rand()      # choosing a random number between 0 and 1

    if f(theta)!= 0.0:
        if (f(theta_prime)/f(theta)) > r:
            theta = theta_prime
        else:
            theta = theta

    else:
        theta = theta_prime

    sel_theta[i] = theta
    theta_prime_arr[i] = theta_prime

#plotting the Markov chain:
fig = plt.figure( figsize=( 10, 4))
plt.scatter(n_array,sel_theta, color='red', marker="*", label='selected points')
plt.scatter(n_array,theta_prime_arr, marker="*",  label='Other points')
plt.plot(n_array,sel_theta, color="black", label='Markov chain')
plt.xlim(0,1000)
plt.legend()
plt.xlabel('Itarations')
plt.ylabel('Points')
plt.show()

# plotting the histogram of the distribution and comparing to exact PDF
def norm_f(x):    # normalized function
	if (3 < x < 7) :
		return(0.25)
	else :
		return(0.0)

x_plot = np.arange(0,15,0.1) #making array for plotting the norm_f(x)
y_plot = np.zeros(x_plot.size)
for i in range(x_plot.size):
	y_plot[i] = norm_f(x_plot[i])

plt.hist(sel_theta, density= True, bins=20)
plt.plot(x_plot, y_plot, color='orange',label= 'Actual distribution to be made')
plt.title('Plotting of the distribution')
plt.legend()
plt.show()