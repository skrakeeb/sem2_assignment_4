'''
coded by: rakeeb
coded for: linear congruential generator
'''

import matplotlib.pyplot as plt 

a =  1664525     #multiplier 
c =  1013904223  #increment
m = 4294967296   #modulus
x = 1            #seed

numbers = 10000   # no of random numbers to be made
rand_numbers = []
for i in range(numbers+1):
	x = ((a*x + c)%m)
	rand_numbers.append(x)
	rand_numbers[i] =  rand_numbers[i]/float(m)  # normalization to 1

plt.hist(rand_numbers,density = True)
plt.show()