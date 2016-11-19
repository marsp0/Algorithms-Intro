import random
import time


def bubble(iterable):

	for i in xrange(len(iterable),0, -1):
		for j in xrange(0, (i-1)):
			if iterable[j] > iterable[j+1]:

				iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

	return iterable


if __name__ == '__main__':

	data = [random.randint(1,1000) for x in xrange(10000)]
	current_time = time.time()
	data = bubble(data)
	after_time = time.time()
	total_time = after_time - current_time
	print total_time