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

SIZE = 100  # The static size that the population will be kept at
BAD_SCORE = 1000  # The penalization for each genome that violates the date
MATE_DIST = 50  # How much genetic info from each parent to take

class Population:
    def __init__(self, operations):
        self.genomes = []
        self.create_new_population(operations)
        self.sort_population()
        self.reap_population()
        print("\n\nThe initial population has been generated")

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
        # Choose two parents from the existing population pseudo-randomly
        parent1, parent2 = random.sample(self.genomes, 2)
        genes_num = len(parent1.operations)

        # Choose MATE_DIST% of the genes from each parent
        p1_amount= int((genes_num) * (MATE_DIST / 100))

        idx_from_p1 = random.sample(range(genes_num), p1_amount)
        idx_from_p1.sort() # Preserve the genome relative order

        # Get the actual genes to be used for the first child
        genes_from_p1 = []
        for idx in idx_from_p1:
            genes_from_p1.append(parent1.operations[idx])

        # Get the indices of the unused genes by p1 from p2
        idx_from_p2 = []
        for idx, gene in enumerate(parent2.operations):
            if gene not in genes_from_p1:
                idx_from_p2.append(idx)
        idx_from_p2.sort()

        first_child = merge_genomes(parent1, parent2, idx_from_p1, idx_from_p2)

        # The genes for the second child are the ones unused by the first child
        idx_from_p1 = [x for x in range(genes_num) if x not in idx_from_p1]
        idx_from_p1.sort()
        idx_from_p2 = [x for x in range(genes_num) if x not in idx_from_p2]
        idx_from_p2.sort()

        second_child = merge_genomes(parent1, parent2, idx_from_p1, idx_from_p2)
        print("First child : ")
        print("".join([str(x.job) + str(x.order) for x in first_child]))
        print("\n\n\nSecond child : ")
        print("".join([str(x.job) + str(x.order) for x in second_child]))



def merge_genomes(parent1, parent2, idx_from_p1, idx_from_p2):
    idx1 = 0
    idx2 = 0
    child = []
    # Merge the selected genes from each parent while keeping their relative
    # order. The lists of indexes indicates which genes have been selected.
    while idx1 < len(idx_from_p1) and idx2 < len(idx_from_p2):
        if idx_from_p1[idx1] <= idx_from_p2[idx2]:
            child.append(parent1.operations[idx_from_p1[idx1]])
            idx1 += 1
        else:
            child.append(parent2.operations[idx_from_p2[idx2]])
            idx2 += 1

    while idx1 < len(idx_from_p1):
        child.append(parent1.operations[idx_from_p1[idx1]])
        idx1 += 1
    while idx2 < len(idx_from_p2):
        child.append(parent2.operations[idx_from_p2[idx2]])
        idx2 += 1
    return child



def calculate_fitness(permutation):
    penalization = 0
    if not is_valid_permutation(permutation):
        penalization = BAD_SCORE
    make_span = calculate_makespan(permutation)
    score = make_span + penalization
    return score


def is_valid_permutation(permutation):
    """
    Map containing the most recent iterated Order# for a Job#
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

