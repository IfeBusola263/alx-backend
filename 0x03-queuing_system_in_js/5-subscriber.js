import { createClient } from 'redis';
import { print } from 'redis';
import { promisify } from 'util';

const client = createClient()
      .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
      .on('connect', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel')
client.on('message', function (channel, msg) {
    console.log(msg);
    if (msg === 'KILL_SERVER') {
	this.unsubscribe('holberton school channel');
	this.quit();
    }
});
