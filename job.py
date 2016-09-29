"""
job.py
~~~~~~~~~~~~~
Stores the information of each job.
 - start_date is the date when the job was received
 - goal_date is the date when the job must be delivered
 - model is the radiator model
 - operations is the list of operations that comprise the job
 - job_id is a unique ID for each job
"""
from operation import Operation

class Job:
	def __init__(self, start_date, goal_date, model, job_id):
		self.start_date = start_date
		self.goal_date  = goal_date
		self.model = model
		self.operations = []
		self.job_id = job_id

		if model == "5967":
			o1 = Operation("Corte de tubo", "VT1", 4.58, "5967", job_id)
			o2 = Operation("Fab. de aleta", "VT2", 2.99, "5967", job_id)
			o3 = Operation("Operacion PUN", "PUN", 2.55, "5967", job_id)
			o4 = Operation("Operacion TROQ1", "TROQ1", 1.56, "5967", job_id)
			o5 = Operation("Operacion TROQ2", "TROQ2", 0.32, "5967", job_id)
			o6 = Operation("Operacion VT3", "VT3", 17.46, "5967", job_id)
			o7 = Operation("Operacion HYR", "HYR", 14.32, "5967", job_id)

			self.operations.extend([o1, o2, o3, o4, o5, o6, o7])
			o6.dependencies = [o1, o2, o3, o4, o5]
			o7.dependencies = [o6]
		elif model == "8047":
			o1 = Operation("Corte de tubo", "VT1", 5.1, "8047", job_id)
			o2 = Operation("Fab. de aleta", "VT2", 2.8, "8047", job_id)
			o3 = Operation("Operacion PUN", "PUN", 2.236, "8047", job_id)
			o4 = Operation("Operacion TROQ1", "TROQ1", 5.13, "8047", job_id)
			o5 = Operation("Operacion TROQ2", "TROQ2", 1.58, "8047", job_id)
			o6 = Operation("Operacion VT3", "VT3", 19.28, "8047", job_id)
			o7 = Operation("Operacion HYR", "HYR", 16.59, "8047", job_id)

			self.operations.extend([o1, o2, o3, o4, o5, o6, o7])
			o6.dependencies = [o1, o2, o3, o4, o5]
			o7.dependencies = [o6]
		elif model == "4025":
			o1 = Operation("Corte de tubo", "VT1", 2.44, "4025", job_id)
			o2 = Operation("Fab. de aleta", "AP1", 7.5, "4025", job_id)
			o3 = Operation("Operacion TROQ1", "TROQ1", 1.35, "4025", job_id)
			o4 = Operation("Operacion AP2", "AP2", 23.94, "4025", job_id)
			o5 = Operation("Operacion HYR", "HYR", 8.1, "4025", job_id)

			self.operations.extend([o1, o2, o3, o4, o5])
			o4.dependencies = [o1, o2]
			o5.dependencies = [o3, o4]

	def print_operations(self):
		for op in self.operations:
			print(str(op) + "\n")