#encoding:utf8
'''
概念：单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。在python中就是一个类，你只能创建一次，后面再创建的话也是和前面的一样。
实现：1，重写__new__，在创建类的时候判断是否已经创建过,没有的话才创建
	  2，重写__new__，将类引用的参数全部指向同一个内存地址
	  3，使用装饰器装饰类，判断类没有被创建之后才创建，否则，返回原来的类
	  4，__metaclass__（元类）
http://blog.csdn.net/ghostfromheaven/article/details/7671853
'''
#方法一
class Singleton(object):
	def __new__(cls,*args,**kw):
		if not hasattr(cls,'_instance'):
			cls._instance = super(Singleton,cls).__new__(cls,*args,**kw)
		return cls._instance
a = Singleton()
b = Singleton()
a.n = 1
print b.n
print id(a),id(b)

#方法二
class Singleton1(object):
	_state = {}
	def __new__(cls,*args,**kw):
		ob = super(Singleton1,cls).__new__(cls,*args,**kw)
		ob.__dict__ = cls._state
		return ob

#方法三
def decorator(cls):
	instance = {}
	def wrap(*args,**kw):
		if not cls in instance:
			instance[cls] = cls(*args,**kw)
		return instance[cls]
	return wrap

@decorator
class myclass(object):
	a = 1


