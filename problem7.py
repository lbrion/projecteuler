primes = [2, 3]
cur = 4
while len(primes) < 10001:
	cur += 1
	for num in primes:
		if cur % num == 0:
			break
	else:
		primes.append(cur)

print primes
print cur