
"""
Fibonacci number generator
When given a position, the function returns the fibonacci at that position in the sequence.
The zeroth number in the fibonacci sequence is 0. The first number is 1
Negative numbers should return None
"""
def fibonacci(position):
  #this supports negative numbers
  if position < 0: 
    return None
  if position == 0:
    return 0
  if(position == 1 or position == 2):
    return 1
  return fibonacci(position - 1) + fibonacci(position - 2)


# Test cases
print("The 1st Fibonacci number: ", fibonacci(1))
print("The 21st Fibonacci number: ", fibonacci(21))

assert(fibonacci(0) == 0)
print("The 0th Fibonacci number: ", fibonacci(0)) # should return 0

assert(fibonacci(-1) == None)
print("The -1st Fibonacci number: ", fibonacci(-1)) # should return None

assert(fibonacci(1) == 1)
print("The 1st Fibonacci number: ", fibonacci(1)) # should return 1

assert(fibonacci(2) == 1)
print("The 2nd Fibonacci number: ", fibonacci(2)) # should return 1

assert(fibonacci(3) == 2)
print("The 3rd Fibonacci number: ", fibonacci(3)) # should return 2

assert(fibonacci(4) == 3)
print("The 4th Fibonacci number: ", fibonacci(4)) # should return 3

assert(fibonacci(5) == 5)
print("The 5th Fibonacci number: ", fibonacci(5)) # should return 5

assert(fibonacci(6) == 8)
print("The 6th Fibonacci number: ", fibonacci(6)) # should return 8

assert(fibonacci(7) == 13)
print("The 7th Fibonacci number: ", fibonacci(7)) # should return 13

assert(fibonacci(8) == 21)
print("The 8th Fibonacci number: ", fibonacci(8)) # should return 21

print("Code ran successfully!")


