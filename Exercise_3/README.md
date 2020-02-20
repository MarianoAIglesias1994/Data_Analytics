# Exercise 3

To start with, let:
* **t** be the total number of coins,
* **p** the number of pirates selected by Morgan,
* **c** the number of coins each selected pirate receives,
* **m** the number of coins Morgan receives.

The objective of Morgan achieving the maximum number of coins given “The pirate law” is translated to math as maximizing the remainder **m** of the division between **t** and **p**.

4 conditions are given:

1. The treasure has less than 1000 golden coins, **t** < 1000.
2. If Morgan chooses a group of 99 pirates, 51 coins are going to be for him, **t** % 99 = 51.
3. If Morgan chooses a group of 77 pirates, 29 coins are going to be for him, **t** % 77 = 29.
4. Pirates must have at least 1 coin each, **c** >= 1.

From this conditions, the total number of coins **t** can be found following this method: 

Create a table with **c** (the number of coins each selected pirate receives) as the first column, with a value from 1 (Condition 4) through the next integers, and in the second column the total number of coins that the treasure should have in order to verify Condition 2. Therefore, when **c** = 1, **t** = 1 * 99 + 51 = 150, and so on.

| **c** | **t** |
| 	 --- 	|     --- 	   |
|	  1	    |	  150   |	
|	  2	    |	  249	   |	
|	  3	    |	  348	   |
|	  4	    |	  447	   |
|	  5	    |	  546	   |
|	  6	    |	  **645**	   |
|	  7	    |	  744	   |
|	  8	    |	  843	   |
|	  9	    |	  942	   |
|	  10    |	  1041	   |
|    ...	|	  ...	   |	

We stop at **c** = 10 because of Condition 1.

Next, the corresponding table is done for Condition 3. Therefore, when **c** = 1, **t** = 1 * 77 +  29 = 106, and so on.

| **c** | **t** |
| 	 --- 	|     --- 	   |
|	  1	    |	  106   |	
|	  2	    |	  183	   |	
|	  3	    |	  260	   |
|	  4	    |	  337	   |
|	  5	    |	  414	   |
|	  6	    |	  491	   |
|	  7	    |	  568	   |
|	  8	    |	  **645**	   |
|	  9	    |	  722	   |
|	  10    |	  799	   |
|	  11	|	  876	   |
|	  12    |	  953	   |
|	  13    |	  1030	   |
|    ...	|	  ...	   |

Finally, it can be seen that **t** = 645, as it is the only value that verifies all 4 conditions.

To continue, a new table is proposed where the first column is **p** (the number of pirates selected by Morgan, varying from 1 to 645), and the second column is **m** (the number of coins Morgan receives) obtained as the remainder of the division between **t** and **p**. Thus, the maximum element in the second column will be Morgan best case. This happens when Morgan chooses **p** = 323 pirates, each one with only **c** = 1 coin, and he gets **m** = 322 coins.

This procedure is automated in 'Exercise_3_plot.py' script. Also, the following figure is produced in order to show every possible combination from the previous table of solutions (blue circles), and the optimum solution is highlighted (red star). Each point in this graph consists of a **p** number of pirates selected by Morgan and its corresponding **m** (number of coins Morgan receives) in order to verify all conditions.

![Alt text](exercise_3.png?raw=true "Possible solutions to Morgan's problem and optimum solution")

After solving the exercise via a sort of 'bruteforce' methodology, we can think that perhaps it was very logical for Morgan to take at most half the coins (a bit less, 645/2 = 322.5) and divide the rest between the corresponding number of pirates, one coin for each. 

* In the case he chooses less than 323 pirates, the situation is bad for him because the pirates will start getting two coins each, and the number **m** he receives will be less than the optimum. 
* And in the case he chooses more than 323 pirates, the situation is bad for him because although the pirates get only one coin, there will be more pirates to divide the treasure.

Therefore this local maximum is also the global maximum in this problem.
