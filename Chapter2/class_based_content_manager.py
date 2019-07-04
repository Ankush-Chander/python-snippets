import time

class TimedCode:
	def __init__(self, task):
		self.task = task

	def __enter__(self):
		self.t_start = time.time()

	def __exit__(self, exc_type, exc_val, exc_tb):
		time_elapsed = time.time() - self.t_start
		print(self.task + " took "+ str(time_elapsed)+ " secs")

with TimedCode("task to be measured") as t:
	time.sleep(2)
