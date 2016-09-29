from population import Population
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

def calculate_makespan(permutation):
	cummulative_machine_times = {}
	cummulative_job_times = {}

	for operation in permutation:
		#initialize variables with 0 if does not exist
		if not operation.job in cummulative_job_times:
			cummulative_job_times[operation.job] = 0

		if not operation.machine in cummulative_machine_times:
			cummulative_machine_times[operation.machine] = 0

		if cummulative_job_times[operation.job] < cummulative_machine_times[operation.machine]:
			cummulative_machine_times[operation.machine] += operation.duration
			cummulative_job_times[operation.job] = cummulative_machine_times[operation.machine]
		else:
			cummulative_job_times[operation.job] += operation.duration
			cummulative_machine_times[operation.machine] = cummulative_job_times[operation.job]

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
	products['1111'] = random.randrange(1, 50, 1)
	products['2222'] = random.randrange(1, 50, 1)

	all_jobs = []
	all_operations = []
	for key, value in products.items():
		for i in range(value):
			all_jobs.append(Job(datetime.now(), datetime.now() + timedelta(hours=170), key))
	for job in all_jobs:
		all_operations.extend(job.operations)

	for operation in all_operations:
		print(operation)


    

    """ Print operations in original order """
    print("\n")
    print("--------- Valid Permutation ---------")
    for op in operations_list:
        print (op)
    print("Is valid permutation: " + str(is_valid_permutation(operations_list)))
    print("-------------------------------------")

    """ Swap 2 values to make it non valid """
    print("\n")
    print("Swaping values...")
    temp = operations_list[7]
    operations_list[7] = operations_list[8]
    operations_list[8] = temp

    """ Print operations in new order """
    print("\n")
    print("--------- Not Valid Permutation ---------")
    for op in operations_list:
        print (op)
    print("Is valid permutation: " + str(is_valid_permutation(operations_list)))
    print("-------------------------------------")

    print("\n\nThis is the generated population:")
    population = Population(operations_list)
    #print(population)
