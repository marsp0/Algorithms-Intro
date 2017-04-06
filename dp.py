'''
	Dynamic Programming

	DP - 'careful brute force'
	DP - guessing + recursion + memoization
	dp - its kinda like shortest paths in a DAG. The hard part is to find the DAG

	Complexity:

	#subproblems * time per subproblem 

	5 Steps to use with DP (not necesseraly sequential)

		1. Define subproblems
		2. Guess (typically the solution)
		3. Relate subproblem solutions (using recurrence)
		4. Recurse and memoize (top-down or bottom-up)
		5. Solve the original problem

	DP problems have two commong traits :

	1. Optimal Substructure - the problems exhibit this trait if the optimal solution to it contains within it optimal solutions
								to subproblems
	2.

'''

import time

memo_memo = {}
memo_iter = {}

def fibonacci_memo(n):

	'''
		Fibonacci's numbers using memoization technique (DP)

		Complexity : O(n)

	'''
	try:
		return memo_memo[n]
	except KeyError:
		if n <= 2:
			f = 1
		else:
			f = fibonacci_memo(n-1) + fibonacci_memo(n-2)
		memo_memo[n] = f
	return memo_memo[n]

def fibonacci_exp(n):
	'''
		Fibonacci's numbers using recursion. The most simple, but inefficient algorithm.

		Complexity : O(2^n) , its actually the golden ratio to the power of n, but the order of the function is the same
	'''
	if n <= 2:
		return 1
	else:
		return fibonacci_exp(n-1) + fibonacci_exp(n-2)

def fibonacci_iter(n):
	'''
		bottom-up approach with the same Complexity as the fibonacci_memo function
	'''

	for i in xrange(1,n+1):
		if i <= 2:
			memo_iter[i] = 1
		else:
			memo_iter[i] = memo_iter[i-1] + memo_iter[i-2]
	return memo_iter[n]

def longest_common_sequence(string_a, string_b):
	memo = {}
	for i in xrange(string_a):
		memo[-1,]
	for i in xrange(len(string_a)):
		for j in xrange(len(string_b)):
			print memo
			if i == 0 and j == 0:
				if string_a[i] == string_b[j]:
					memo[(i,j)] = 1
				else:
					memo[(i,j)] = 0
			else:
				if string_a[i] == string_b[j]:
					print i-1,j-1
					memo[(i,j)] = 1 + memo[i-1,j-1]
				else:
					first = (i-1,j)
					second = (i,j-1)
					if not first in memo:
						first = (0,0)
					if not second in memo:
						second = (0,0)
					memo[(i,j)] = max(memo[first], memo[second])
	return memo

if __name__ == '__main__':
	#before_exp = time.time()
	#print fibonacci_exp(38)
	#after_exp = time.time()
	#print 'the time for the exp function is ', after_exp - before_exp
	#print
	#before_memo = time.time()
	#print fibonacci_iter(200)
	#after_memo = time.time()
	#print memo_iter
	#print 'the time after the memo function is ', after_memo - before_memo 
	print longest_common_sequence('abc','cba')