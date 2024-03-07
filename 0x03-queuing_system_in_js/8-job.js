function createPushNotificationsJobs(jobs, queue){

	if (!Array.isArray(jobs))throw Error('Jobs is not an array');

	const jobOn = 'push_notification_code_3';
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
}

export default createPushNotificationsJobs;
