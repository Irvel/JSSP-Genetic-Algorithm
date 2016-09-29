from population import Population
from job import Job
import random
from operation import Operation
from population import is_valid_permutation
from datetime import datetime, timedelta

if __name__ == "__main__":
	products = {}
	products['1111'] = 2
	products['2222'] = 1

	all_jobs = []
	all_operations = []
	job_id = 0
	for key, value in products.items():
		for i in range(value):
			all_jobs.append(Job(datetime.now(), datetime.now() + timedelta(hours=170), key, job_id))
			job_id += 1
	for job in all_jobs:
		all_operations.extend(job.operations)

	for operation in all_operations:
		print(operation)

    population = Population(all_operations)
    population.reproduce_population()
