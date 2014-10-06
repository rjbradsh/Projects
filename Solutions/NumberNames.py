#in progress

def get_digit_and_position_name(digit, position):
	if not isinstance(digit, int):
		raise TypeError
	if not isinstance(position, int):
		raise TypeError
	name = ""
	
		

def print_name_in_english( x ):
	if not isinstance(x, int):
		raise TypeError
	name_string = ""
	if x < 0:
		name_string = "Negative "
	elif x == 0:
		print "Zero"
		return
	position = 1000000    #Holds the position to be examined starting at 1 million
	while position > 0:
		position_value = x/position #find the digit in the position
		if position_value > 0:
			

number = int(input('Please enter a number: '))
print_name_in_english(number)