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

    def create_new_population(self, operations):
        permutations = product(operations, repeat=len(operations))
        for _ in range(SIZE):
            genome = Genome(next(permutations))
            genome.score = self.calculate_fitness(genome.operations)
            self.genomes.append(genome)

    def calculate_fitness(self, permutation):
        penalization = 0
        if not self.is_valid_permutation(permutation):
            penalization = BAD_SCORE
        make_span = calculate_makespan(permutation)
        score = make_span + penalization
        return score

    def is_valid_permutation(self, permutation):
        return True

def calculate_makespan(permutation):
    return 0
