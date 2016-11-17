import random

def bubble(iterable):

	for i in xrange(len(iterable),0, -1):
		for j in xrange(0, (i-1)):
			if iterable[j] > iterable[j+1]:

				iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

	return iterable


if __name__ == '__main__':

	data = [random.randint(0, 100) for x in xrange(100)]
	print bubble(data)