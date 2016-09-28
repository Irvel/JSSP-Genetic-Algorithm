"""
population.py
~~~~~~~~~~~~~
This stores a fixed set of genomes, and provides methods to
create new generations based on the existing one.
"""
from itertools import product
from genome import Genome
SIZE = 100
BAD_SCORE = -10000

class Population:
    def __init__(self, operations):
        self.genomes = []
        self.create_new_population(operations)

    def __str__(self):
        genomes_string = ""
        for genome in self.genomes:
            genomes_string.append(str(genome))
            genomes_string.append("\n")
        return genomes_string

    def create_new_population(self, operations):
        permutations = product(operations, repeat=len(operations))
        for _ in range(SIZE):
            genome = Genome(next(permutations))
            genome.score = self.calculate_fitness(genome.operations)
            self.genomes.append(genome)

    def calculate_fitness(self, permutation):
        penalization = 0
        if not is_valid_permutation(permutation):
            penalization = BAD_SCORE
        make_span = calculate_makespan(permutation)
        score = make_span + penalization
        return score

def is_valid_permutation(permutation):
    """ 
    Map containg the most recent iterated Order# for a Job#
    E.g.
    J1 -> 2
    J2 -> 1
    J3 -> 3

    This means that the last time an operation belonging to Job1 was
    processed, its Order# was 2. So, if the next operation of Job1 has
    an Order# of 1 it means it is not valid.
    """
    last_job_order = {}

    for operation in permutation:
        job = operation.job
        order = operation.order
        if job in last_job_order:
            if order < last_job_order[job]:
                return False
        last_job_order[job] = order
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

