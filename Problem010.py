import time

def FindPrimes(limit):
	primeList = []
	currentPrime = 2
	primeList.append(currentPrime)
	currentPrime = 3
	primeList.append(currentPrime)

	while(currentPrime < limit-1):
		isPrime = True

		# Only check odd numbers
		currentPrime += 2
		for prime in primeList:
			if(prime*2 > currentPrime):
				break

			# Current prime is not prime
			if(currentPrime % prime == 0):
				isPrime = False
				break
		# Current prime is prime
		if(isPrime):
			primeList.append(currentPrime)

	return primeList

# Add al primes below input
def SumOfPrimes(inputNumber):
	print("Hi")

def main():
	t0 = time.process_time()

	print("Solve Problem")
	print(sum(FindPrimes(2000000)))

	print("Clocked at: ", time.process_time()-t0, "seconds")

if __name__ == "__main__":
    main()