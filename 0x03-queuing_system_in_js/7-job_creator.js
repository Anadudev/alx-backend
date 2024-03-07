import kue from 'kue';

const queue = kue.createQueue();

const jobs = [
	{
		phoneNumber: '4153518780',
		message: 'This is the code 1234 to verify your account'
	},
	{
		phoneNumber: '4153518781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4153518743',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4153538781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4153118782',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4153718781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4159518782',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4158718781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4153818782',
		message: 'This is the code 4321 to verify your account'
	},
	{
		phoneNumber: '4154318781',
		message: 'This is the code 4562 to verify your account'
	},
	{
		phoneNumber: '4151218782',
		message: 'This is the code 4321 to verify your account'
	}
];

function sendNotification(phoneNumber, message) {
	console.log(
		`Sending notification to ${phoneNumber}, with message: ${message}`
	);
}
const jobOn = `push_notification_code_2`;
jobs.forEach((jobObj) => {

	const job = queue.create(jobOn, jobObj).save((error) => {
		if (!error) console.log(`Notification job created: ${job.id}`);
	});

	job.on('complete', () => console.log(`Notification job ${job.id} completed`));

	job.on('filed', (error) => console.log(
		`Notification job ${job.id} failed: ${error}`
	));

	job.on('progress', (progress) => console.log(
		`Notification job ${job.id} ${progress}% complete`
	));
});
