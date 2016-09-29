"""
operation.py
~~~~~~~~~~~~~
This stores the information of each individual operation in the
production line.
 - machine is the machine in which that operation will be executed
 - duration is the amount of time in which the operation will be completed
 - job is the set of operations needed to fully build a radiator
 - order determines the relative order among a set of operations that belog
 to the same job
"""
class Operation:

    def __init__(self, machine, duration, job_model, job_id):
    	self.machine = machine
    	self.duration = duration
    	self.job_model = job_model
    	self.job_id = job_id
    	self.dependencies = []

    def __str__(self):
    	return ("Job#" + str(self.job_model) + 
    	" Machine#" + str(self.machine) + " Duration=" + str(self.duration))

    def print_dependencies(self):
    	if len(self.dependencies) > 0:
    		print(str(self) + " depends on ")
    		for operation in self.dependencies:
    			print(str(operation))
