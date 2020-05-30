import numpy as np 


# For a circle
def f(x,y):
	if ( (x-1)**2 + (y-1)**2 < 1): #defining an unit circle at(1,1)
		return(1)
	else :
		return(0)

num_points = 10000 # no of points taken
count = 0        
for i in range(num_points) :
	x = np.random.rand(2)*2  #choosing random 2d points inside the square of side 2. (In the 1st quadrant)
	f_val = f(x[0], x[1])

	if (f_val == 1):
		count = count + 1

area = 4*count/float(num_points) # multiplying the probability with area of the square
print( 'area of unit circle: ', area,'\n')

# for 10D sphere:
def f(x):
	s = 0
	for i in range(x.size):
		s = s + ( x[i]-1 )**2
	return(s)

num_points = 100000
count = 0 
for i in range(num_points):
	x = np.random.rand(10)*2
	if (f(x) < 1):
		count = count + 1
prob = count/float(num_points)
vol = (2**10) * prob 

print( 'Volume of a 10D unit sphere: ', vol)