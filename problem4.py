result = 0

def palindrome(num):
	size = len(str(num))
	return str(num)[0:size/2] == str(num)[::-1][0:size/2]

for x in range(1, 1000):
	for y in range(x, 1000):
		if x * y > result: 
			if palindrome(x * y):
				result = x * y

print result