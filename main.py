import random
import collections
from datetime import datetime, timedelta

from termcolor import cprint
# import tkinter.simpledialog

import plotter
from population import Population
from job import Job
from operation import Operation
from population import is_valid_permutation, calculate_makespan, calculate_fitness

if __name__ == "__main__":

    # root = tkinter.Tk()
    # root.withdraw()

    products = collections.OrderedDict()
    # products['5967'] = tkinter.simpledialog.askinteger("5967", "Quantity of model 5967?", minvalue=0, initialvalue=1)
    # products['8047'] = tkinter.simpledialog.askinteger("8047", "Quantity of model 8047?", minvalue=0, initialvalue=1)
    # products['4025'] = tkinter.simpledialog.askinteger("4025", "Quantity of model 4025?", minvalue=0, initialvalue=1)
    # iterations = tkinter.simpledialog.askinteger("Iterations", "Iterations?", minvalue=1, initialvalue=50000)
    products['5967'] = 4
    products['8047'] = 5
    products['4025'] = 3
    iterations = 12000

    all_jobs = []
    all_operations = []
    job_id = 0
    for key, value in products.items():
        for i in range(value):
            all_jobs.append(Job(datetime.now(), datetime.now() + timedelta(hours=170), key, job_id))
            job_id += 1
    for job in all_jobs:
        all_operations.extend(job.operations)

    var1, var2 = calculate_makespan(all_operations)

    cprint("********** JSSP Genetic Solver **********", "yellow")

    population_size = int(4.9 * len(all_operations))
    population = Population(all_operations, population_size)

    current_best = population.genomes[1] # So that the first best is always printed
    makespans = []
    iteration_numbers = []

    print("Cantidad de modelos ingresados:")
    print(str(products['5967'])+ " modelos 5967")
    print(str(products['8047'])+ " modelos 8047")
    print(str(products['4025'])+ " modelos 4025")
    print("Population size: " + str(population_size))
    cprint("\n\nBase configuration:", "blue")
    for operation in all_operations:
        print(str(operation))
    cprint("Total makespan: " + str(var2) + "\n", "grey")

    print("\nReproducing population " + str(iterations) + " times...\n")
    p = 0
    for i in range(iterations):
        makespans.extend([calculate_fitness(x.operations) for x in population.genomes])
        for _ in range(len(population.genomes)):
            iteration_numbers.append(i)
        if current_best is not population.genomes[0]:
            current_makespan = calculate_makespan(current_best.operations)[1]

            current_best = population.genomes[0]
            print("#" + str(i) + ". The current best is: " + str(calculate_makespan(current_best.operations)[1])[:7], end=" ")
            print("    Improvement over base: ", end="")
            cprint(str(100 - calculate_makespan(current_best.operations)[1]/ var2 * 100)[:6] + "%", "cyan")
        population.reproduce_population()
        if i%(iterations/10) == 0:
            p += 10
            cprint("- Completion amount: " + str(p) + "%", 'green')

    population.reap_population()

    dummy, best_makespan = calculate_makespan(current_best.operations)
    sorted_operations = sorted(current_best.operations, key = lambda x: x.start_time, reverse = False)
    cprint("\n\nOptimized configuration:", "blue")
    for operation in sorted_operations:
        print(str(operation))
    cprint("Total makespan: " + str(best_makespan) + "\n", "grey")


    # plotter.plot(iteration_numbers, makespans)
