from population import Population
from job import Job
import random
import collections
from operation import Operation
from population import is_valid_permutation, calculate_makespan
from datetime import datetime, timedelta
import tkinter.simpledialog
import matplotlib.pyplot as plt

if __name__ == "__main__":

    root = tkinter.Tk()
    root.withdraw()

    products = collections.OrderedDict()
    products['5967'] = tkinter.simpledialog.askinteger("5967", "Quantity of model 5967?", minvalue=0, initialvalue=1)
    products['8047'] = tkinter.simpledialog.askinteger("8047", "Quantity of model 8047?", minvalue=0, initialvalue=1)
    products['4025'] = tkinter.simpledialog.askinteger("4025", "Quantity of model 4025?", minvalue=0, initialvalue=1)

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

    """
    for operation in all_operations:
        print(operation)
    """

    population = Population(all_operations)
    print(population)
    current_best = population.genomes[1]
    makespans = []
    generations = []
    print("\nReproducing population 40000 times...\n")
    for i in range(40000):
        if current_best is not population.genomes[0]:
            current_makespan = calculate_makespan(current_best.operations)[1]
            generations.append(i)
            makespans.append(current_makespan)
            current_best = population.genomes[0]
            print("It #" + str(i) + ". The current best is: " +  str(current_best), end="")
            print("Improvement percentage: " + str(100 - calculate_makespan(current_best.operations)[1]/calculate_makespan(all_operations)[1] * 100)[:6] + "%")
        population.reproduce_population()
    population.reap_population()
    print()
    print(population)
    print("\n\n")

    dummy, best_makespan = calculate_makespan(current_best.operations)
    print("Best configuration found:\n")
    for operation in current_best.operations:
        print(str(operation))
    print("Best makespan found: " + str(best_makespan))

    plt.plot(generations, makespans, 'ro')
    plt.title("Initial population: " + str(100) + " Generations: " + str(40000))
    plt.ylabel("Makespan")
    plt.xlabel("Generation")
    plt.show()