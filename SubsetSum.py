def mergeLists(l1, l2):
	from heapq import merge
	result = []
	last = -1
	for i in merge(l1, l2):
		if i != last:
			last = i
			result.append(i)
	return result

def trim(l, e):
	result = [l[0]]
	last = l[0]
	for i in xrange(1, len(l)):
		if l[i] > last * (1 + e):
			result.append(l[i])
			last = l[i]
	return result

def approxSubsetSum(S, t, e):
	from bisect import bisect_left
	n = len(S)
	L = {0: [0]}
	for i in xrange(1, n+1):
		L[i] = mergeLists(L[i-1], [x + S[i-1] for x in L[i-1]])
		L[i] = trim(L[i], e/(2.0 * n))
		L[i] = L[i][:bisect_left(L[i], t)+1]
	return max(L[n])

print approxSubsetSum([1,3,5,6,8,9,14], 21, 0.5)
