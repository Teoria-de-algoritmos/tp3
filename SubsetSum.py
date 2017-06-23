def mergeLists(first, second):
	from heapq import merge
	result = [-1]
	for i in merge(first, second):
		if i != result[-1]:
			result.append(i)
	return result[1:]

def trim(l, e):
	result = [l[0]]
	for i in xrange(1, len(l)):
		if l[i] > result[-1] * (1 + e):
			result.append(l[i])
	return result

def approxSubsetSum(S, t, epsilon):
	from bisect import bisect_left
	n = len(S)
	L = {0: [0]}
	for i in xrange(1, n+1):
		L[i] = mergeLists(L[i-1], [x + S[i-1] for x in L[i-1]])
		L[i] = trim(L[i], epsilon / (2.0 * n))
		L[i] = L[i][:bisect_left(L[i], t)+1]
	return max(L[n])

print approxSubsetSum([1,3,5,6,8,9,14], 21, 0.5)
