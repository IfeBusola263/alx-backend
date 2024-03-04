# Queuing System in JS

* dump.rdb
```
The dump data from the redis-5.0.7 directory
```

* 0-redis_client.js
```
a script that connects to the Redis server running on the machine.
```

* 1-redis_op.js
```
implements new functions to 0-redis_client.js

setNewSchool:
accepts two arguments schoolName, and value.
sets in Redis the value for the key schoolName
displays a confirmation message using redis.print

displaySchoolValue:
accepts one argument schoolName.
logs to the console the value for the key passed as argument
```

* 2-redis_op_async.js
```
builds on 1-redis_op.js
Using promisify, the function displaySchoolValue is modified to use ES6 async / await
```

* 4-redis_advanced_op.js
```
builds on 2-redis_op_async.js to use the client to store a hash value.
```

* 5-subscriber.js and 5-publisher.js are redis clients which connect to the server. 
```
5-subscriber.js
> On connect, logs the message 'Redis client connected to the server'
> On error, logs the message 'Redis client not connected to the server: ERROR MESSAGE'
> subscribes to the channel holberton school channel
> When it receives message on the channel holberton school channel, it logs the message to the console
> When the message is KILL_SERVER, it unsubscribes and quits.
```

```
5-publisher.js
> On connect, logs the message 'Redis client connected to the server'
> On error, logs the message 'Redis client not connected to the server: ERROR MESSAGE'

Implements a function publishMessage which:
	  > Takes two arguments: message (string), and time (integer - in ms)
	  > After time millisecond:
	   	* The function logs to the console 'About to send MESSAGE'
		* The function publishs to the channel 'holberton school channel', the message passed in argument after the time passed in arguments

```

* 6-job_creator.js
```
Has a queue created with Kue
Has an object containing the Job data with the following format:
{
  phoneNumber: string,
  message: string,
}
Has a queue named push_notification_code, and a created a job with the object created before
When the job is created without error, logs to the console "Notification job created: JOB ID"
When the job is completed, logs to the console "Notification job completed"
When the job is failing, logs to the console "Notification job failed"
```

* 6-job_processor.js
```
> Has a queue created with Kue
> Implementes a function named sendNotification:
	    > Take two arguments "phoneNumber" and "message"
	    > logs to the console "Sending notification to $PHONE_NUMBER, with message: $MESSAGE"

> Has a queue process that listens to new jobs on push_notification_code:
> Every new job calls the sendNotification function with the phone number and the message contained within the job data

Keep in mind:

* Only one Redis server is needed to execute the program
* Two node processes will need to run each script at the same time
* Kue is used to set up the queue
```

* 7-job_creator.js
```
> Has an array jobs with static data.
> Has a queue created with Kue.
> A loop that goes through the array jobs and for each object:
  > Create a new job to the queue push_notification_code_2 with the current object
  > If there is no error, logs to the console "Notification job created: $JOB_ID"
  > On the job completion, logs to the console "Notification job $JOB_ID completed"
  > On the job failure, logs to the console "Notification job $JOB_ID failed: ERROR"
  > On the job progress, logs to the console "Notification job $JOB_ID PERCENTAGE% complete"
```

* 7-job_processor.js
```
Has an array that contains the blacklisted phone numbers - 4153518780 and 4153518781.
These 2 numbers will be blacklisted by the jobs processor.

Implements a function sendNotification that takes 4 arguments:
	   > phoneNumber
	   > message
	   > job
	   > done

   > When the function is called, the progress of the job of 0 out of 100 is tracked.
   > If phoneNumber is included in the "blacklisted array", the job will fail with an
     Error object and the message: "Phone number $PHONE_NUMBER is blacklisted".
   > Otherwise:
     The progress tracked to 50%
     Logged to the console is "Sending notification to $PHONE_NUMBER, with message: $MESSAGE"
A queue with Kue that will proceed job of the queue push_notification_code_2 with two jobs
at a time is also implemented.

Keep in mind:

* Only one Redis server is needed to execute the program.
* Two node processes will need to run each script at the same time.
* Kue is used to set up the queue.
```

* 8-job.js
```
Implements a function named createPushNotificationsJobs:

It takes into argument "jobs" (array of objects), and "queue" (Kue queue)
If jobs is not an array, it should throw an Error with message: "Jobs is not an array"
For each job in jobs, a job is created in the queue "push_notification_code_3"
When a job is created, it logs to the console "Notification job created: $JOB_ID"
When a job is complete, it logs to the console "Notification job $JOB_ID completed"
When a job is failed, it logs to the console "Notification job $JOB_ID failed: ERROR"
When a job is making progress, it logs to the console "Notification job $JOB_ID PERCENT% complete".
```

* 8-job.test.js
```
test suite for the 8-jobs.js
```

* 9-stock.js
```
> Implements a function named getItemById:
	   takes "id" as argument
	   returns the item from "listProducts" with the same "id".

> A client to connect to the Redis server:
     > It will set in Redis the stock for the key item.ITEM_ID with a
     help function "reserveStockById" that will take "itemId" and "stock" as arguments.
     > It will return the reserved stock for a specific item with helper
     "async function getCurrentReservedStockById", that will take "itemId" as an argument.

> Implements a small express server, with a "/list_products" route and
  "/list_products/:itemId", that will return the current product and the
  current available stock (by using getCurrentReservedStockById)
  with the following JSON format:
```
```
{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
```
```
A "/reserve_product/:itemId:" route

> Which If the item does not exist, it returns: {"status":"Product not found"}
> If the item exists, it checks that there is at least one stock available. If not it returns: {"status":"Not enough stock available","itemId":1}
> If there is enough stock available, it reserves one item (by using reserveStockById), and returns: {"status":"Reservation confirmed","itemId":1}
```

* 100-seat.js
```
An express app server for Seat Reservation.
```