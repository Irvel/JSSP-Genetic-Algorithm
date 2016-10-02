"""
population.py
~~~~~~~~~~~~~
This stores a fixed set of genomes, and provides methods to
create new generations based on the existing one.
"""
import random
import collections
from operator import attrgetter

from genome import Genome

SIZE = 270  # The static size that the population will be kept at
MATE_DIST = 50  # How much genetic info from each parent to take
MUTATE_PROB = 0.4  # How likely is a newborn to mutate
bad_score = 6300  # The penalization for each genome that violates the date

class Population:
    def __init__(self, operations, size):
        self.genomes = []
        self.population_size = size
        self.create_new_population(operations)
        self.sort_population()
        self.reap_population()
        _, base_span = calculate_makespan(operations)
        bad_score = int(base_span * 1.1)

    def __str__(self):
        genomes_string = ""
        for genome in self.genomes:
            genomes_string += str(genome)
        return genomes_string + "\n# of valid genomes: " + str(self.num_trues())

    def create_new_population(self, operations):
        #print("\nCreating initial population...")
        genome = Genome(operations[:])
        genome.score = calculate_fitness(genome.operations)
        self.genomes.append(genome)
        for _ in range(self.population_size):
            genome = Genome(shuffle_valid_genome(operations[:]))
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
        self.genomes = self.genomes[:self.population_size]

    def reproduce_population(self):
        """
        The miracle of life
        This method will take two random parents and create two children from
        them.
        """
        first_child, second_child = self.mate()
        mutate_genome(first_child)
        mutate_genome(second_child)

        first_genome = Genome(first_child)
        second_genome = Genome(second_child)
        first_genome.score = calculate_fitness(first_child)
        second_genome.score = calculate_fitness(second_child)

        self.genomes.append(first_genome)
        self.genomes.append(second_genome)
        self.sort_population()
        self.reap_population()

    def mate(self):
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

        return first_child, second_child


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


def shuffle_valid_genome(operations, shuffle_amount=100):
        operations_dict = collections.OrderedDict() # Constant access time
        for i in range(len(operations) * (100 - shuffle_amount) // 100):
            operations_dict[operations[i]] = True

        while len(operations_dict) < len(operations):
            for op in random.sample(operations, len(operations)):
                if op not in operations_dict:
                    dependency_satisfied = True
                    for dep in op.dependencies:
                        # If its dependency is not yet satisfied, then can't add it
                        if dep not in operations_dict:
                            dependency_satisfied = False
                            break
                    if dependency_satisfied:
                        operations_dict[op] = True
        return [gene for gene in operations_dict.keys()]


def mutate_genome(operations):
    if random.random() < MUTATE_PROB:
        return shuffle_valid_genome(operations, 90)


def calculate_fitness(permutation):
    penalization = 0
    if not is_valid_permutation(permutation):
        penalization = bad_score
        make_span = 0
    else:
       _, make_span = calculate_makespan(permutation)
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
    operations_end_time = {}
    jobs_end_time = {}

    for operation in permutation:
        #initialize variables with 0 if does not exist
        if not operation in operations_end_time:
            operations_end_time[operation] = 0

        if not operation.machine in cummulative_machine_times:
            cummulative_machine_times[operation.machine] = 0

        #Check if the operation has dependencies
        if operation.dependencies:

            #initialize time of the operation to the max value of dependencies
            max_time_dependencies = operations_end_time[operation.dependencies[0]]
            for dependent_operation in operation.dependencies:
                if operations_end_time[dependent_operation] > max_time_dependencies:
                    max_time_dependencies = operations_end_time[dependent_operation]
            operations_end_time[operation] = max_time_dependencies

        #Calculate time
        if operations_end_time[operation] < cummulative_machine_times[operation.machine]:

            operation.start_time = cummulative_machine_times[operation.machine]

            cummulative_machine_times[operation.machine] += operation.duration
            operations_end_time[operation] = cummulative_machine_times[operation.machine]
        else:

            operation.start_time = operations_end_time[operation]

            operations_end_time[operation] += operation.duration
            cummulative_machine_times[operation.machine] = operations_end_time[operation]

        """Save the time of each operation.
         So, at the end you have the last one is the one saved """
        jobs_end_time[operation.job_id] = operations_end_time[operation]

    """Return a map mapping each job with the corresponding end time,
     and the biggest time of the jobs"""
    #print(operations_end_time)
    return jobs_end_time, jobs_end_time[max(jobs_end_time, key=jobs_end_time.get)]
