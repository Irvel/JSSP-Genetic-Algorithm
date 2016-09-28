import random

BAD_SCORE = -10000

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

def permute(n):
	"""return a list of n valid permutations"""

def is_valid_permutation(permutation):
	return False

def get_random_permutation():
	"""return a random permutation from the pool"""

def calculate_makespan(permutation):
	""""""

def calculate_fitness(permutation):
    penalization = 0
    if not is_valid_permutation(permutation):
        penalization = BAD_SCORE
    make_span = calculate_makespan(permutation)
    score = make_span + penalization
    return score


if __name__ == "__main__":
	num_operations = 11
	num_columns = 4
	num_machines = 3
	max_operations_per_job = 3
	
	""" 
	operations is a Nx4 matrix representing each operation
	and its Job, Order, Machine, and operation Time.
	E.g.

		 J  O  M   T
	Op1 [1, 1, 2, 10]
	Op2 [2, 1, 1,  5]
	Op3 [1, 2, 1, 20]
	Op4 [1, 3, 3, 50]
	Op5 [2, 2, 2,  3]
	"""
	operations = []
	for i in range(num_operations):
		operations.append([])
		for j in range(num_columns):
			operations[i].append(None)

	fill_matrix(operations, num_operations, num_columns, max_operations_per_job, num_machines)
	print_matrix(operations, num_operations, num_columns)
