from population import Population
from job import Job
import random
from operation import Operation
from population import is_valid_permutation, calculate_makespan
from datetime import datetime, timedelta
import tkinter.simpledialog
import matplotlib.pyplot as plt

if __name__ == "__main__":

    root = tkinter.Tk()
    root.withdraw()

    products = {}
    products['5967'] = tkinter.simpledialog.askinteger("5967", "Quantity of model 5967?", minvalue=0, initialvalue=1)
    products['8047'] = tkinter.simpledialog.askinteger("8047", "Quantity of model 8047?", minvalue=0, initialvalue=1)
    products['4025'] = tkinter.simpledialog.askinteger("4025", "Quantity of model 4025?", minvalue=0, initialvalue=1)

    iterations = tkinter.simpledialog.askinteger("Iterations", "Iterations?", minvalue=1, initialvalue=50000)

    all_jobs = []
    all_operations = []
    job_id = 0
    for key, value in products.items():
        for i in range(value):
            all_jobs.append(Job(datetime.now(), datetime.now() + timedelta(hours=170), key, job_id))
            job_id += 1
    for job in all_jobs:
        all_operations.extend(job.operations)

    """
    for operation in all_operations:
        print(operation)

    print(is_valid_permutation(all_operations))
    """
    var1, var2 = calculate_makespan(all_operations)
    """
    print("Initial configuration...")
    for operation in all_operations:
        print(operation)
    print("Initial configuration makespan: " + str(var2))
    """
    population = Population(all_operations)
    #print(population)

    current_best = population.genomes[1]
    makespans = []
    generations = []
    #print("\nReproducing population " + str(iterations) + " times...\n")
    print("********** OPTIMIZACION DE PHAR **********")

    print("Cantidad de modelos ingresados:\n")
    print(str(products['5967'])+ "modelos 5967")
    print(str(products['8047'])+ "modelos 8047")
    print(str(products['4025'])+ "modelos 4025")
    print("\n \n Porcentaje completado:")
    p = 0
    print("0 %")
    for i in range(iterations):
        if current_best is not population.genomes[0]:
            current_makespan = calculate_makespan(current_best.operations)[1]
            generations.append(i)
            makespans.append(current_makespan)
            current_best = population.genomes[0]
            #print("It #" + str(i) + ". The current best is: " +  str(current_best), end="")
            #print("Improvement percentage: " + str(100 - calculate_makespan(current_best.operations)[1]/calculate_makespan(all_operations)[1] * 100)[:6] + "%")
        population.reproduce_population()
        if(i%(iterations/10) == 0):
            p+=10
            print(str(p) + " %")

    population.reap_population()
    #print()
    #print(population)
    print("\n\n")

    dummy, best_makespan = calculate_makespan(current_best.operations)
    sorted_operations = sorted(current_best.operations, key = lambda x: x.start_time, reverse = False)
    print("Mejor solucion encontrada:\n")
    for operation in sorted_operations:
        print(str(operation))
    print("Tiempo total: " + str(best_makespan))

    plt.plot(generations, makespans, 'ro')
    plt.title("Poblacion inicial: " + str(100) + " Generaciones: " + str(iterations))
    plt.ylabel("Makespan")
    plt.xlabel("Generacion")
    plt.show()
