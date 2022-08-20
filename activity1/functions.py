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



def lunch_lady(name, lunch = "mystery meat"):
	print(f"{name} would like to have {lunch} for lunch")

lunch_lady('Johnny', 'hamburger')
lunch_lady('Jane')



def sum_n_product(x, y):
	return (x + y, x * y)

print(sum_n_product(2, 5))
print(sum_n_product(9, 1))
print(sum_n_product(0, 101))



def alias_arb_args(*args):
	arb_args(*args)

alias_arb_args("Shrek", "is", "cool")



def arb_mean(*ints):
	total = 0
	for i in ints:
		total += i
		print(total)
	
	print(total / len(ints))

arb_mean(1, 2, 3, 1, 10, 8)
arb_mean(2, 1)



def arb_longest_string(*strings):
	longest = ""
	for i in strings:
		if len(i) > len(longest):
			longest = i

	return longest

print(arb_longest_string("one", "three", "0"))
print(arb_longest_string("123456789", "12345678", "1234567", "123456"))

