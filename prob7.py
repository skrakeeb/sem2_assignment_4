'''
coded by: rakeeb
coded for: implimenting chi squared method
'''


import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import chi2

score = np.arange(2,13,1)
obs_count1 = np.array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])
obs_count2 = np.array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5])
expected_np = np.array([4, 8, 12, 16, 20, 24, 20, 16, 12, 8, 4])

# evaluation of V:
V1 = 0
V2 = 0
for i in range(score.size):
	V1 = V1 + ( (obs_count1[i]-expected_np[i])**2 )/float(expected_np[i])
	V2 = V2 + ( (obs_count2[i]-expected_np[i])**2 )/float(expected_np[i])

k = score.size - 1
p1 = 1 - chi2.cdf(V1,k)  # probability of getting V >= V1
p2 = 1 - chi2.cdf(V2,k)  # probability of getting V >= V2

def test_result(p):
	if (p < 0.01 or p > 0.99):
		print('Numbers are not sufficiently random')
	elif (0.01 <= p <= 0.05 or 0.95 <= p <= 0.99):
		print('Numbers are suspect')
	elif (0.05 < p <= 0.1 or 0.9 <= p < 0.99):
		print('Numbers are almost suspect')
	else :
		print('Numbers are sufficiently random')	



print( test_result(p1), ' for observed  counts 1\n', test_result(p2), ' for observed  counts 2')