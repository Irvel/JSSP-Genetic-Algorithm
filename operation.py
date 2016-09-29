"""
operation.py
~~~~~~~~~~~~~
This stores the information of each individual operation in the
production line.
 - name improves readability when printing
 - machine is the machine in which that operation will be executed
 - duration is the amount of time in which the operation will be completed
 - job_model is the radiator model that this operation belongs to
 - job_id is the job to which this operation belongs
 - dependencies is a list containing the operations that this operation
   depends on
"""
class Operation:

    def __init__(self, name, machine, duration, job_model, job_id):
    	self.name = name
    	self.machine = machine
    	self.duration = duration
    	self.job_model = job_model
    	self.job_id = job_id
    	self.dependencies = []

    def __str__(self):
    	return (" Machine: " + str(self.machine)
    		+ " Duration: " + str(self.duration) + " Job model: " + str(self.job_model) + " Job ID: " 
            + str(self.job_id) + " Name: " + str(self.name))

    def print_dependencies(self):
    	if len(self.dependencies) > 0:
    		print(str(self) + " depends on ")
    		for operation in self.dependencies:
    			print(str(operation))
