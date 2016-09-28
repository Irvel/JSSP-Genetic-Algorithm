from population import Population
import random
from operation import Operation

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
    operations_matrix = []
    for i in range(num_operations):
        operations_matrix.append([])
        for j in range(num_columns):
            operations_matrix[i].append(None)

    fill_matrix(operations_matrix, num_operations, num_columns, max_operations_per_job, num_machines)
    print_matrix(operations_matrix, num_operations, num_columns)

    operations_list = get_operations_list(operations_matrix, num_operations)
    for op in operations_list:
        print (op)
    population = Population(operations_list)
