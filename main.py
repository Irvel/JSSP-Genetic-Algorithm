from population import Population
from job import Job
import random
from operation import Operation
from population import is_valid_permutation, calculate_makespan
from datetime import datetime, timedelta

if __name__ == "__main__":
    products = {}
    products['5967'] = 19
    products['8047'] = 19
    products['4025'] = 18

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
    current_best = population.genomes[1]
    print("\nReproducing population 199000 times...\n")
    for i in range(199000):
        if current_best is not population.genomes[0]:
            current_best = population.genomes[0]
            print("It #" + str(i) + ". The current best is: " +  str(current_best), end="")
            print("Improvement percentage: " + str(100 - calculate_makespan(current_best.operations)[1]/calculate_makespan(all_operations)[1] * 100)[:6] + "%")
        population.reproduce_population()
    population.reap_population()
    print()
    print(population)
