import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { spy } from 'sinon';
import { expect } from 'chai';


describe('createPushNotificationsJobs', function (){
    const queue = createQueue();
    const Console = spy(console, 'log');
    const obj = {
        phoneNumber: '4153518780',
	message: 'This is the code 1234 to verify your account'
    };

    const jobs = [
	{
	    phoneNumber: '4153518780',
	    message: 'This is the code 1234 to verify your account'
	},
	{
	    phoneNumber: '4153518781',
	    message: 'This is the code 4562 to verify your account'
	}
    ];

    before(function () {
	queue.testMode.enter(true);
    });

    afterEach(function() {
	Console.restore()
	queue.testMode.clear();
    });

    after(function() {
	queue.testMode.exit();
    });

    it('should throw an error when jobs is not an array', function () {
	expect(() => createPushNotificationsJobs(obj, queue)).to.throw('Jobs is not an array');
    });

    it('should confirm only two jobs are created', async function () {
	await createPushNotificationsJobs(jobs, queue);
	// queue.process('push_notification_code_3', () => {
	//     const jobId1 = queue.testMode.jobs[0].id
	//     const jobId2 = queue.testMode.jobs[1].id
	//     // expect(Console.callCount).to.equal(2);
	//     expect(Console.calledWith(`Notification job created: ${jobId1}`)).to.be.true;
	//     expect(Console.calledWith(`Notification job created: ${jobId2}`)).to.be.true;
	// });
	expect(queue.testMode.jobs.length).to.equal(2);
	expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
	expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
	expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
	expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });
});
