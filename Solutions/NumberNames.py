#Takes in a number and then prints out the English name of that number
#By Richard Bradshaw

def get_digit_and_position_name(digit, position):
	if not isinstance(digit, int):
		raise TypeError( "digit must be an integer" )
	if not isinstance(position, int):
		raise TypeError( "position must be an integer" )
	name = ""
	if position != 10:
		name = [" One", " Two", " Three", " Four", " Five",
			" Six", " Seven", " Eight ", " Nine"][digit-1]
		if position == 100:
			name = name + "-hundred"
	else:
		name = [" Twenty", " Thirty", " Fourty", " Fifty",
			" Sixty", " Seventy", " Eighty", " Ninty"][digit - 2] #10s are accounted for elsewhere
	return name

def account_for_tens(number): # the names for 10s are unique so a special method is made to process them
	number %= 10
	return [" Ten", " Eleven", " Twelve", " Thirteen", " Fourteen",
		" Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"][number]
		
#sub-unit is 3 digits long and rank is either 1000000, 1000, or 1
def process_sub_unit_name(sub_unit, rank):
	name = ""
	sub_position = 100
	while sub_unit > 0:
		digit = sub_unit/sub_position
		if sub_position == 10 and digit == 1:
			name = name + account_for_tens(sub_unit)
			sub_unit = 0
		elif digit != 0:
			name = name + get_digit_and_position_name(digit, sub_position)
			sub_unit = sub_unit - digit * sub_position
		sub_position = sub_position/10
	
	if rank == 1000000:
		name = name + " million"
	elif rank == 1000:
		name = name + " thousand"
	return name
		
def print_name_in_english( x ):
	if not isinstance(x, int):
		raise TypeError( "x must be an integer" )
	
	name_string = ""
	if x < 0:
		name_string = "Negative"
		x = -x
	elif x == 0:
		print "Zero"
		return
	rank = 1000000    #Holds the position to be examined starting at 1 million
	while rank > 0:
		sub_unit = x/rank #find the digit in the position
		if sub_unit > 0:
			name_string = name_string + process_sub_unit_name(sub_unit, rank)
			x = x - sub_unit * rank
		rank = rank/1000
		
	
	print name_string.strip().lower().capitalize()
			
			
			
try:
	number = int(input('Please enter a number: '))
	print_name_in_english(number)
except NameError:
	print "Invalid number entered"