# Closures - Passing a variable as a parameter in a function and then using that variable in its nested function.

def func1(msg):
	def func2():
		print('Hello!!')
		print(msg)
		print('Bye!!')
	return func2()

func1('wassup??')

# Decorators - Passing a function as a parameter in a function and then using that function in its nested function

def func1(func3):
	def func2():
		print('Hello!!')
		func3()
		print('Bye!!')
	return func2()

@func1 # this means func1(innerfunc)
def innerfunc():
	print('I am inner function')
