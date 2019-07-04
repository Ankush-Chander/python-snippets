from contextlib import contextmanager
import time

@contextmanager
def timed_code(code_name):
	t_start = time.time()
	try:
		yield t_start
	finally:
		time_elapsed = time.time() - t_start
		print(code_name+" took "+ str(time_elapsed)+ " secs")


with timed_code("Task to be measured"):
	time.sleep(2)

