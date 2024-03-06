import { createClient, print } from 'redis';
import { createQueue } from 'kue';
import express from 'express';
import { promisify } from 'util';

const client = createClient()
      .on('error', (err) => console.log(`Unestablish Redis connection: ${err}`))
      .on('connect', () => console.log('Redis Server connected'));

function reserveSeat(number) {
    client.set('available_seats', number, print);
}

async function getCurrentAvailableSeats() {
    const get = promisify(client.get).bind(client)
    const numAvailableSeats = await get('available_seats');
    return numAvailableSeats;
}

let reservationEnabled = true;

const queue = createQueue();

const PORT = 1245;
const HOST = 'localhost';
const app = express();

app.use(express.json());

app.get('/available_seats', async (req, res) => {
 const numAvaliableSeats = await getCurrentAvailableSeats();
    res.status(200).json({"numberOfAvailableSeats": numAvaliableSeats});
});

app.get('/reserve_seat', (req, res) => {
    console.log(reservationEnabled);
    if (!reservationEnabled){
	res.status(200).json({ "status": "Reservation are blocked" });
	return;
    }
    const job = queue.create('reserve_seat');

    job
	.on('failed', (err) => { console.log(`Seat reservation job ${job.id} failed: ${err}`)})
	.on('complete', () => {
	    console.log(`Seat reservation job ${job.id} completed`)
	});

    job.save((err) => {
	if (!err) res.status(200).json({ "status": "Reservation in process" });
	else
	    res.status(200).json({ "status": "Reservation failed" });
    });
});

app.get('/process', (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
	const seatsAvailable = await getCurrentAvailableSeats();
	if (Number(seatsAvailable) === 0) {
	    console.log('I got here when zero');
	    reservationEnabled = false;
	    done(new Error('Not enough seats available'));
	} else {
	    reserveSeat(seatsAvailable - 1);
	    done()
	}
    });

    res.status(200).json({"status":"Queue processing"});
});

app.listen(PORT, HOST, () => {
    reserveSeat(50);
    console.log(`Express server is running on PORT ${PORT}`);
});
