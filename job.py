from operation import Operation

class Job:
	def __init__(self, start_date, goal_date, model):
		self.start_date = start_date
		self.goal_date  = goal_date
		self.model = model
		self.operations = []

		if model == "1111":
			o1 = Operation("m1", 3, "1111")
			o2 = Operation("m2", 4, "1111")
			o3 = Operation("m1", 2, "1111")

			self.operations.extend([o1, o2, o3])
			o3.dependencies = [o1, o2]
		elif model == "2222":
			o1 = Operation("m2", 4, "2222")
			o2 = Operation("m1", 2, "2222")
			o3 = Operation("m2", 3, "2222")

			self.operations.extend([o1, o2, o3])
			o3.dependencies = [o1, o2]

	def print_operations(self):
		for op in self.operations:
			print(str(op) + "\n")