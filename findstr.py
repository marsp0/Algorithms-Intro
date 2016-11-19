def find(iterable, string):

	len_str = len(string)
	len_total = len(iterable)

	#start iterating over the total string
	for i in xrange(len_total - len_str):
		j = 0
		#start from every current index of the outer loop to search for match
		while ((j < len_str) and (iterable[i+j] == string[j])):
			j += 1
		if j == len_str:
			return i
	return -1


if __name__ == '__main__' :

	print find('spasov is not actually martin spasov, but it is just another dude that has the name martin spasov, this is weird given that the name martin spasov is not that common', 'martin')