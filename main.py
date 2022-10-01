numbers = [5, 20, 30, 30, 50]

delval = int(input('Enter the deletion value: '))

try:
	numbers.remove(delval)
except ValueError:
	numbers.clear()
print (numbers)
