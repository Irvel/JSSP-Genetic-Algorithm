from population import Population
from job import Job
import random
from operation import Operation
from population import is_valid_permutation, calculate_makespan
from datetime import datetime, timedelta

if __name__ == "__main__":
    products = {}
    products['5967'] = 9
    products['8047'] = 9
    products['4025'] = 8

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

    print(is_valid_permutation(all_operations))
    var1, var2 = calculate_makespan(all_operations)
    print(str(var2))

    population = Population(all_operations)
    print(population)
    print("\nReproducing population 15000 times...\n")
    for i in range(15000):
        population.reproduce_population()
    population.reap_population()
    print()
    print(population)
