"""
genome.py
~~~~~~~~~~~~~
This class stores the set of operations that compose an individual in the
population.
"""
class Genome:
    def __init__(self, operations):
        self.operations = operations
        self.score = 0