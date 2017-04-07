class BinarySearch(list):
		def __init__(self,a,b):
			self.a = a
			self.b = b
			self.array = list.__init__(self,[x for x in range(self.b , (self.a + self.b),self.b)])
			self.length = len(self)

		def Search(self,target):
			lo = 0
			hi = self.length
			
			count_index = {}
			count_index['count'] = 0
			while lo < hi:
				count_index['count']  += 1
				mid = (hi+lo)//2
				midval = self[mid]
				if midval < target: 
					lo = mid+1
				elif midval > target:
					hi = mid
				else:
					count_index['index'] = mid
					return count_index

