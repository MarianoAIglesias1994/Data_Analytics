# ------------------------------------------------------------------------------
# Original code
# ------------------------------------------------------------------------------

#import random

# def weighted_random(values, weights):
# 	total_weight = sum(weights)	# In this line and in the following one, a normalization of the weights is carried out.
# 	acum_weights = [w / total_weight for w in weights[:]] # I consider it a good idea, since weights might not be given
# in a normalized format as in the example. But the name might be confusing, as the variable is reused in the next lines.
# 	for i in range(len(weights)): # Here it seems that it attempts to obtain the cumulative distribution function 
# (i.e., the accumulated weights).
# 		acum_weights[i] += acum_weights[i] # But instead, it calculates the double of each element. 
# For instance, in the example it gets acum_weights = [1.0, 0.6, 0.4].
# 	rand = random.random() # It generates a random float uniformly distributed in the semi-open range [0.0, 1.0). 
# This would be the basis to compare against the accumulated weights.
# 	for value, weight in zip(values, acum_weights): # For each pair value - accumulated weight, 
# it will map the cumulative distribution function to the uniformly distributed random variable.
# 		if weight > rand: # It checks if the random float is below the accumulated weigth.
# 			return value # In that case, the value paired to the accumulated weight should be retrieved.

# ------------------------------------------------------------------------------
# Fixed code
# ------------------------------------------------------------------------------

import random

def weighted_random(values, weights):
	total_weight = sum(weights)
	acum_weights = [w / total_weight for w in weights[:]] 
	# The normalization procedure is kept, and the variable name stays the same, in order to change the least in the code.
	for i in range(1, len(weights)):
	# This is modified in order to obtain the cumulative distribution function,
	# the accumulated weights up to the actual weight.
	# The first accumulated weight will always be the first weight.
	# The next ones will be obtained as the previous accumulation plus the actual weight.
		acum_weights[i] += acum_weights[i-1] 
	rand = random.random()	
	# Now, this weighted random sampling has the correct cumulative distribution function, therefore it works accordingly.
	for value, weight in zip(values, acum_weights): 
		if weight > rand:
			return value