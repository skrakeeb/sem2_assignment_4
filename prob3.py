'''
coded by: rakeeb
coded for: comparing time taken by hand written and numpy function for generating random numbers
'''


import time

start_time = time.time()

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

end_time1 = time.time()

from numpy.random import  rand 
rand_numpy = rand(numbers+1)	

end_time2 = time.time()

print('Time taken for Linear congruential generator:',(end_time1 - start_time),'\nTime taken for numpy library:',(end_time2 - end_time1))