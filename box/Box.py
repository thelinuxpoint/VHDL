class Box():
	"""
		The Structure Which Contain all Sorting Algorithm

	"""
	def __init__(self,arr):
		self.arr = arr
		# store sorting algorithm with index
		self.s_dict = {
			0: self.merge_sort,
			1: self.quick_sort,
			2: self.radix_sort,
			3: self.counting_sort,
			4: self.insertion_sort,
			5: self.bubble_sort
		}

	def sort(self,index=0):
		"""
			0 : merge sort
			1 : quick sort
			2 : radix sort
			3 : counting sort
			4 : insertion sort
			5 : bubble sort
		"""
		self.s_dict[index](self.arr)

	def merge_sort(self):
		arr = self.arr

		def build(arr):
			
			if len(arr) > 1:
		        r = len(arr)//2
	    	    L = arr[:r]
	        	M = arr[r:]

	        	self.merge_sort(L)
	        	self.merge_sort(M)

	        	i = j = k = 0
	        	
	        	while i < len(L) and j < len(M):
	            	if L[i] < M[j]:
	                	arr[k] = L[i]
	                	i += 1
	            	else:
	                	arr[k] = M[j]
	                	j += 1
	            	k += 1
	           	# ---- Left off values ----
	        	while i < len(L):
	            	arr[k] = L[i]
	            	i += 1
	            	k += 1

	        	while j < len(M):
	            	arr[k] = M[j]
	            	j += 1
	            	k += 1


	def quick_sort(self):
		pass
	
	def insertion_sort(self):
		pass


	def bubble_sort(self):
		# copy 
		arr = self.arr
		# the bubble sort algo
		for i in range(0,len(arr)):
			for j in range(0,len(arr)-i-1):
				if arr[j] > arr[j + 1]:
        			temp = arr[j]
        			arr[j] = arr[j+1]
        			arr[j+1] = temp

        self.arr = arr

