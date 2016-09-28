def permute(n):
	"""return a list of n valid permutations"""

def is_permutation_valid(permutation):
	return False

def get_random_permutation():
	"""return a random permutation from the pool"""

def calculate_makespan(permutation):
	cummulative_machine_times = {}
	cummulative_job_times = {}

	for operation in permutation:
		#initialize variables with 0 if does not exist
		if !operation.job in cummulative_job_times:
			cummulative_job_times[operation.job] = 0

		if !operation.machine in cummulative_machine_times:
			cummulative_machine_times[operation.machine] = 0
			
		if cummulative_job_times[operation.job] < cummulative_machine_times[operation.machine]:
			cummulative_machine_times[operation.machine] += operation.duration
		 	cummulative_job_times[operation.job] = cummulative_machine_times[operation.machine]
		else:
			cummulative_job_times[operation.job] += operation.duration
			cummulative_machine_times[operation.machine] = cummulative_job_times[operation.job]

	#Return the biggest time of the jobs
	return cummulative_job_times[max(cummulative_job_times, key=cummulative_job_times.get)]
