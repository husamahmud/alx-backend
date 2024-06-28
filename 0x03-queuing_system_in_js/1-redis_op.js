import {createClient} from 'redis';

const client = createClient();

async function setNewSchool(schoolName, value) {
    try {
        await client.connect()
        await client.set(schoolName, value, redis.print)
    } catch (error) {
        console.error('Error setting value in Redis:', error);
    } finally {
        await client.disconnect();
    }
}

setNewSchool()