from population import Population
from job import Job
import random
from operation import Operation
from population import is_valid_permutation
from datetime import datetime, timedelta

def print_matrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print (matrix[i][j], end=" ")
        print ("")

def fill_matrix(matrix, num_operations, num_columns, operations_per_job, num_machines):
	job_number = 1
	job_count = 1
	for i in range(num_operations):
		if (job_count > operations_per_job):
			job_count = 1
			job_number += 1
		matrix[i][0] = job_number
		matrix[i][1] = job_count
		matrix[i][2] = random.randrange(1, num_machines + 1, 1)
		matrix[i][3] = random.randrange(5, 100, 5)
		job_count += 1

def get_operations_list(matrix, num_operations):
    operations_list = []
    for i in range(num_operations):
        job_num = matrix[i][0]
        order_num = matrix[i][1]
        machine_num = matrix[i][2]
        time = matrix[i][3]
        operations_list.append(Operation(machine_num, time, job_num, order_num))

    return operations_list

if __name__ == "__main__":
	products = {}
	products['1111'] = 2
	products['2222'] = 3

	all_jobs = []
	all_operations = []
	for key, value in products.items():
		for i in range(value):
			all_jobs.append(Job(datetime.now(), datetime.now() + timedelta(hours=170), key))
	for job in all_jobs:
		all_operations.extend(job.operations)

	for operation in all_operations:
		print(operation)

    population = Population(operations_list)
    population.reproduce_population()
