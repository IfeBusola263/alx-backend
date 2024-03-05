import { createQueue } from 'kue';

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {

    job.progress(0, 100);

    if (!blacklist.includes(phoneNumber)) {
	job.progress(50, 100);
	console.log(
	    `Sending notification to ${phoneNumber}, with message: ${message}`
	);
	done();
	// setTimeout(() => {
	//     job.progress(100, 100);
	//     done();
	// }, 2000);
    } else {
	return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
}

const queue = createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
    const phone = job.data.phoneNumber;
    const msg = job.data.message;
    sendNotification(phone, msg, job, done);
});
