class BinarySearch(list):
		def __init__(self,a,b):
			self.a = a
			self.b = b

		def Search(value):
			lo = 0
			A = glist(self.a,self.b)
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
class list:
	def __init__(self,a,b):
		self.a = a 
		self.b = b 

	def glist(self): 
		a = self.a 
		b = self.b 
		i = 0
		j = 0
		blist = []
		while i < a:
			blist.append(i)
			i = i + 1
			j = j + b
		return blist
		lenght = len[blist]
