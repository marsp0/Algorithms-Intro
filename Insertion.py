''' INSERTION SORT 
	
	- very efficient for small number of elements
	- its run time is n*log_2(n)
	- it sorts the elements in place

'''

import random
import time

def sort_by_insertion(iterable):
	#constant guard
	i = 1
	#start iteratin over the sequence 
	while (i < len(iterable)) :
		#start a second loop to sort the current element in the already sorted part of the sequence
		j = i
		while ((j > 0) and (iterable[j] < iterable[j-1])):
			'''we can do :
			temp = iterable[j-1]
			iterable[j-1] = iterable[j]
			iterable[j] = temp
			but it turns out that the following is faster (1 sec for 10000 elements)
			'''
			iterable[j-1], iterable[j] = iterable[j], iterable[j-1]
			j -= 1
		i += 1
	return iterable

if __name__ == '__main__':
	temp_data = []
	for i in xrange(1,10000):
		temp_data.append(random.randint(1,1000))
	current_time = time.time()
	p = sort_by_insertion(temp_data)
	after_time = time.time()
	print p
	print after_time - current_time
