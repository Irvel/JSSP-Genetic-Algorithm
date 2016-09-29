"""
population.py
~~~~~~~~~~~~~
This stores a fixed set of genomes, and provides methods to
create new generations based on the existing one.
"""
import random
from itertools import product
from genome import Genome
from operator import attrgetter

SIZE = 100
BAD_SCORE = 1000

class Population:
    def __init__(self, operations):
        self.genomes = []
        self.create_new_population(operations)
        self.sort_population()
        self.reap_population()

    def __str__(self):
        genomes_string = ""
        for genome in self.genomes:
            genomes_string += str(genome)
        return genomes_string

    def create_new_population(self, operations):
        permutations = product(operations, repeat=len(operations))
        for _ in range(SIZE * 1000):
            random.shuffle(operations)
            genome = Genome(operations[:])
            genome.score = calculate_fitness(genome.operations)
            self.genomes.append(genome)

    def sort_population(self):
        """
        Sorts the population based on the fitness score
        """
        self.genomes.sort(key = attrgetter('score'), reverse = False)

    def reap_population(self):
        """
        Keeps only the first SIZE individuals
        """
        self.genomes = self.genomes[:100]

     def reproduce_population(self):
        """
        The miracle of life
        """
        pass



def calculate_fitness(permutation):
    penalization = 0
    if not is_valid_permutation(permutation):
        penalization = BAD_SCORE
    make_span = calculate_makespan(permutation)
    score = make_span + penalization
    return score


def is_valid_permutation(permutation):
    operation_done = {}
    for op in permutation:
        operation_done[op] = 0

    for op in permutation:
        for dep in op.dependencies:
            if operation_done[dep] == 0:
                return False
        operation_done[op] = 1
    return True

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

    #Return the biggest time of the jobs
    return cummulative_job_times[max(cummulative_job_times, key=cummulative_job_times.get)]

