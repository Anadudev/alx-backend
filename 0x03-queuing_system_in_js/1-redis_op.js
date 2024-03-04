import { createClient } from 'redis';

const client = createClient()
  .on('error', error => console.log('Redis client not connected to the server:', error))
  .connect();
console.log('Redis client connected to the server');

function setNewSchool (schoolName, value) {
  client.set(schoolName, value);
}

function displaySchoolValue (schoolName) {
  value = client.get(schoolName);
  console.log(value);
}

client.disconnect();
