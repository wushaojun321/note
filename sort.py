#incoding:utf8
def insert_sort(L):
	'''插入排序'''
	count = len(L)
	for i in range(1,count):
		key = L[i]
		j = i - 1
		while j >= 0:
			if key < L[j]:
				L[j+1] = L[j]
				L[j] = key
			j -= 1
	return L
L = [54,2,43,6,12,32]
print insert_sort(L)

def qsort(arr):
	'''快排'''
	less = []
	pivotlist = []
	more = []
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		for i in arr:
			if i < pivot:
				less.append(i)
			elif i > pivot:
				more.append(i)
			else:
				pivotlist.append(i)
		less = qsort(less)
		more = qsort(more)
		return less+pivotlist+more

def qsort1(arr):
	'''快排进化'''
	if not arr:
		return []
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i<pivot]
		more = [i for i in arr[1:] if i>=pivot]
		print more
		return qsort1(less)+[pivot]+qsort1(more)


L1 = [11,54,2,43,6,12,32]
print qsort1(L1)


