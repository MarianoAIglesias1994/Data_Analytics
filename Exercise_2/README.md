# Exercise 2

## Original query

```sql
WITH events AS (
	SELECT
		device_id,
		time_stamp,
		LEAD(time_stamp) OVER (PARTITION BY device_id ORDER BY time_stamp) as next_time_stamp
	FROM events_table
	WHERE month = '201908'
	AND app_id = 1
	AND event_id = 4
),
per_event AS (
	SELECT
		device_id,
		DATE_DIFF('second', time_stamp, next_time_stamp) as time_diff
	FROM events
)
SELECT
	device_id,
	AVG(time_diff) as avg_per_user
FROM per_event
GROUP BY 1
```

This SQL query retrieves, for each user (device_id) of the client 1 (app_id = 1) during August 2019 (month = '201908'), the average time difference between two consecutive events (of the type event_id = 4). 

For instance, if event_id = 4 corresponds to the action 'open', then if the user has a big average time difference between consecutive openings, it would mean that he/she feels not very attracted to the app, and this could trigger the business team to engage him again. Another example could happen if the event_id = 4 corresponds to the action 'purchase', then if the user has a tiny average time difference for this kind of event, the business side might adjust prices or send advertising ir order to make him/her buy even more. Finally, if the event_id = 4 corresponds to the action 'add to cart', then if the user has a small average time difference for this kind of event, the business team could send promotions and discounts to convince the user to buy.

In order to explain more about how the query works, in the first part, 'events' is obtained with the following columns:

| device_id | time_stamp | next_time_stamp |
| 	 --- 	|    ---     |       ---       |
|	 1	    |	  1	     | 		  2		   |
|	 1	    |	  2	     | 		  3	       |
|	 1	    |	  3	   	 | 	      5        |
|   ...	  	|	 ...	 | 	     ...	   |
   
The window function allows to order the timestamps corresponding to each device_id, and then get the consecutive timestamp as a third column for each original timestamp.
Then, 'per_event' consists of a first column corresponding to each device_id, and a second one that shows the time difference in seconds between consecutive timestamps from each row in 'events'.

| device_id | time_diff  |
| 	 --- 	|    ---     |
|  	  1	    |	  1	  	 |
|	  1	    |	  1	  	 |
|	  1	    |	  2	     |
|    ...	|	 ...	 | 	

Lastly, the average time difference for each device_id is returned.

| device_id | avg_per_user |
| 	 --- 	|     --- 	   |
|	  1	    |	  1.33	   |	
|	  2	    |	  1.5	   |	
|	  3	    |	   2	   |
|    ...	|	  ...	   |	


## Modified query

```sql
SELECT
	device_id,
	IFNULL((DATE_DIFF('second', MIN(time_stamp), MAX(time_stamp))) * 1.0 /NULLIF(COUNT(device_id)-1,0) ,0) as avg_per_user
FROM events_table
WHERE month = '201908' AND app_id = 1 AND event_id = 4
GROUP BY device_id 
```

This modified SQL query does not use the window function. The main idea behind it is that the average of consecutive timestamps can be simplified to the quotient between: the difference between the maximum and minimum timestamp, and the number of timestamps minus 1.

```math
((T_2-T_1) + (T_3-T_2) + … + (T_N-T_{N-1})) / N  simplifies to (T_N-T_1) / N-1
```

The proposed solution is similar to the first part of the original, but adding this simplification trick and a protection against division by zero.
