class Task:
	def __init__(self):
		self.perform()

	def perform(self):
		for i in range(1, 51):
			print(i, end='')
			if i%3==0:
				print(" foo", end='')
			if i%5==0:
				print(" bar", end='')
			if i%7==0:
				print(" baz", end='')
			print()



task = Task()