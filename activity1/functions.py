def arb_args(*args):
	for i in args:
		print(i)

arb_args("hello", "world")
arb_args("it's", "a", "me", "mario")

def inner_func(x, y):
	def square(int):
		return int * int
	
	def half(int):
		return int / 2

	return (square(x), half(y))

print(inner_func(2, 3))
print(inner_func(12, 6))
print(inner_func(999, 123456789))

def lunch_lady(str1, str2 = "mystery meat"):
	print(f"{str1} would like to have {str2} for lunch")

lunch_lady('Johnny', 'hamburger')
lunch_lady('Jane')
