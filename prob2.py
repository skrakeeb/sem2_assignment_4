'''
coded by: rakeeb
coded for: generating random number between 0,1
'''


from numpy.random import  rand 
import matplotlib.pyplot as plt 

x = rand(10001)

plt.hist(x, density = True)
plt.show()