''' INSERTION SORT 
	
	- very efficient for small number of elements
	- its run time is n*log_2(n)
	- it sorts the elements in place

	Loop Inviariant of the insertion sort: At the start of each iteration of the for loop the sublist iterable[0:j-1] consists of the elements originally in the list,
	but in a sorted order.

	Three points of the loop invariant :

	1. Initialization : before the starting of the loop, the iterable[0] is a list with 1 element and thus is sorted.
	2. Maintanence : the loop invariant hold at the beginning of every iteration. The sequence iterable[0:j-1] is a sorted.
	3. Termination : at this point the variable used to count the current index should be the same as the len of the iterable

'''

import random
import time

def sort_by_insertion(iterable):
	#constant guard
	i = 1
	len_to_reach = len(iterable)
	#start iterating over the sequence 
	# NOTE:  the while loop here is faster than the for loop
	while (i < len_to_reach):
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
