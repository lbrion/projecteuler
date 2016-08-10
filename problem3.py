number = 600851475143

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i: 	#if i is not a factor of n, increment i
            i += 1
        else:		#else i is a factor, divide by i
            n //= i
    return n

print largest_prime_factor(number)