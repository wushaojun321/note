#encoding:utf8

def fib1():
	'''使用yield'''
	a,b = 0,1
	while True:
		yield a+b
		a,b = b,a+b
a = fib1()
for i in range(100):
	print a.next()

def fib2(n):
	'''使用递归'''
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib2(n-1)+fib2(n-2)
print fib2(10)

