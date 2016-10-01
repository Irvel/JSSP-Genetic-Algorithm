"""
genome.py
~~~~~~~~~~~~~
This class stores the set of operations that compose an individual in the
population.
"""
class Genome:
    def __init__(self, operations):
        self.operations = operations
        self.score = 999999

    def __str__(self):
        # A string representation of the genome takes the sum of the
        # Job, Order, Machine and Duration in numeric value
        genome_string = ""
        numeric_value = 0
        ascii_value = ""
        for op in self.operations:
            numeric_value += op.duration
            ascii_value = str(int(numeric_value) % 10)
            genome_string += ascii_value
        from population import is_valid_permutation
        return genome_string[:12] + " " + str(is_valid_permutation(self.operations)) + " " + str(self.score)

