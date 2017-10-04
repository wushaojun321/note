#encoding:utf8
'''
原理：python里面所有东西都是对象，函数也是，装饰器原理是将被装饰函数作为参数传入到装饰函数里面去，可以为函数增加功能（打印日志写一个）
	>>> def my_decorator(func):
	...     def wrap(*arg,**kwarg):
	...             print arg,kwarg
	...             return func(*arg,**kwarg)
	...     return wrap
	...
	>>> def my_hello(name):
	...     return name+'hello!'
	...
	>>> @my_decorator
	... def my_hello(name):
	...     return name+'hello!'
	...
	>>> my_hello('wsj')
	('wsj',) {}
	'wsjhello!'
'''
def decorator(func):
	def wrap(*args,**kw):
		print '*'*40 + 'start!' + '*'*40
		print func(*args,**kw)
		print '*'*40 + 'end!' + '*'*40
	return wrap

@decorator
def hello():
	return 'hello ,wsj!'

hello()