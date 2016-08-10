fib0 = 1
fib1 = 2
result = 0

while fib1 < 4000000:
	if fib1 % 2 == 0:
		result += fib1
	(fib0, fib1) = (fib1, fib0 + fib1)

print result