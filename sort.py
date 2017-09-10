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

