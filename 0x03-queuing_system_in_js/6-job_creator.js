import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});
const jobData = {
    phoneNumber: '2347890922',
    message: 'Welcome to the network',
};

const newJob = queue.create('push_notification_code', jobData)
      .save((err) => {
	  if (!err)
	      console.log(`Notification job created: ${newJob.id}`);
      });

newJob.on('complete', () => { console.log('Notification job completed') })
    .on('failed', () => { console.log('Notification job failed') });
