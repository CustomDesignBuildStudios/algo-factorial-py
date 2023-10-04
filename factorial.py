
def factorial(value):
    
	"""
	Given a number returns the factorial of the number
	Arguments:
	value  - string - Number to get create the factorial from
	"""    
	#edge case: factorial of 0 is 1
	if value == 0:
		return 1

	
	factorial_value = 1
	while value > 0:
		factorial_value *= value
		value -= 1
	return factorial_value

value = int(input("Input number: "))
print(factorial(value))