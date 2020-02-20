# Exercise 1
This function returns random values from a list, given the weights.
The main idea is to obtain the cumulative distribution function (from the weights) and then map it to a uniformly distributed random variable in the semi-open range [0.0, 1.0), also known as 'F⁻1 method'.
For example: weighted_random([1, 2, 3], [0.5, 0.3, 0.2]), should return 1 with 50% of probabilities, 2 with 30% and 3 with 20%. Therefore acum_weights should be [0.5, 0.8, 1.0], but this is not the case in the original code.

In the following figure, the main concept behind this procedure is illustrated. After the distribution function is obtained, a uniformly distributed random variable is sampled from the semi-open range [0.0, 1.0). As an example, if the number is 0.56, then entering from the vertical axis of this plot and following a horizontal line we will hit the blue line at value = 2. Therefore this simulated sampling implies that the value = 2 has ocurred. 
As a result, every number between 0 and 0.5 will produce a value = 1, every number between 0.5 and 0.8 a value = 2, and numbers above 0.8 will generate a value = 3 in the example provided.

![Alt text](exercise_1.png?raw=true "Cumulative distribution function for the example")