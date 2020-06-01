'''
coded by: rakeeb
coded for: function for computing volumes of n ball for various radius 
'''


import numpy as np 

def vol_of_n_ball( dimension, radius, num_points):

	count  = 0

	for i in range(num_points):
		x = np.random.uniform(- radius, radius , dimension)  #craeting points in the given dimension inside a cube of side 2*radius
		s = 0
		for j in range(x.size):
			s = s + x[j]**2      # determining distance from the centre

		if (s < radius**2):
			count = count + 1
	prob = count/float(num_points)  # probability of getting a point inside the sphere
	volume = ((2*radius)**dimension) * prob  #as the vol of cube with side 2*radius = (2*radius)**dimension
	return(volume)		

print('Volume of a 10D unit sphere: ', vol_of_n_ball(10,1,100000))



	