import { createClient } from 'redis';
import { print } from 'redis';
import { promisify } from 'util';

const client = createClient()
      .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
      .on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
    // used promisify to make the client get method a function
    // that returns a promise

    // get is a promisified version of client.get
    const get = promisify(client.get).bind(client)
    const res = await get(schoolName)
    console.log(res);
}

(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
