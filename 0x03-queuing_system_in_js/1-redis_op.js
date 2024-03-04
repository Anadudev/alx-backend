import { createClient } from 'redis';

const client = await createClient()
  .on('error', error => console.log('Redis client not connected to the server:', error))
  .connect();
console.log('Redis client connected to the server');

function setNewSchool(schoolName, value){
	await client.set(schoolName, value);
}

function displaySchoolValue(schoolName){
	value = await client.get(schoolName);
	console.log(value);	
}

await client.disconnect();
