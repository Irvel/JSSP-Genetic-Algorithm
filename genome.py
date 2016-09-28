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

    def __str__(self):
        # A string representation of the genome takes the sum of the
        # Job, Order, Machine and Duration and converts that value into
        # ASCII
        genome_string = ""
        numeric_value = 0
        ascii_value = ""
        for op in self.operations:
            numeric_value += op.job
            numeric_value += op.duration
            numeric_value += op.machine
            numeric_value += op.order
            ascii_value = chr(numeric_value)
            genome_string.append(ascii_value)
        return genome_string