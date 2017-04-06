def binary_search(A, target):
	lo = 0
	hi = len(A)
	count = 0
	count_index = {}
	while lo <= hi:
		count = count + 1
		mid = lo + (hi-lo)/2
		mid = int(mid)
		if A[mid] == target:
			count_index['count'] = count
			count_index['index'] = mid
			return count_index          
		elif A[mid] < target: 
			lo = mid+1
		else:
			hi = mid-1
def list(a,b):
	i = 0
	j = 0
	blist = []
	while i < a:
		blist.append(i)
		i = i + 1
		j = j + b
	return blist
	length = len[blist]

