import random

def merge_sort(array):

	if len(array) < 2:
		return array
	else:
		mid = len(array)//2
		left = merge_sort(array[:mid])
		right = merge_sort(array[mid:])
		return list(merge(left,right))

	

def merge(left,right):

	new = []
	left_index = 0
	right_index = 0
	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			new.append(left[left_index])
			left_index += 1
		else:
			new.append(right[right_index])
			right_index += 1

	if left_index < len(left):
		new.extend(left[left_index:])
	if right_index < len(right):
		new.extend(right[right_index:])
	return new

if __name__ == '__main__':

	array = []
	for i in xrange(100):
		array.append(random.randint(1,1000000))
	print merge_sort(array)