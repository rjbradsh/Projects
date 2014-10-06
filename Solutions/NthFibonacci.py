#Prints the Nth fibonacci number and all numbers leading up to it
#Both recursive and non-recursive options are availble
#By Richard Bradshaw

def compute_fibonacci_nonrecursive( n ):
	if not isinstance(n, int):
		raise TypeError("n must be an integer")
	
	print "Non-recursive: "
	
	print 1
	
	if n > 1:
		x1 = 0
		x2 = 1
		
		pos = 1
		while pos < n:
			xtemp = x1 + x2
			x1 = x2
			x2 = xtemp
			print x2
			pos += 1
			
def fibonacci_recursion(x1, x2, pos, n): # the actual recursive function
	x = x1 + x2
	print x
	pos += 1
	if pos < n:
		fibonacci_recursion(x2, x, pos, n)
	
	
def compute_fibonacci_recursive( n ):
	if not isinstance(n, int):
		raise TypeError("n must be an integer")
	
	print "Recursive: "
	
	print 1
	
	if n > 1:
		fibonacci_recursion(0, 1, 1, n)

try:
	n = int(input("To what position do you want to calculate fibonacci numbers? "))
	if n > 0:
		x = str(input("Enter 1 to for recursive enter anything else for non recursive: "))
		if x.strip() == "1":
			compute_fibonacci_recursive(n)
		else:
			compute_fibonacci_nonrecursive(n)
except NameError:
	print "Invalid number entered"
	
