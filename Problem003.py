def FindLargestPrime(Number):
	primeList = []
	currentPrime = 2
	primeList.append(currentPrime)
	currentPrime = 3
	primeList.append(currentPrime)

	while(currentPrime < Number/2):
		isPrime = True

		# Only check odd numbers
		currentPrime += 2
		for prime in primeList:
			# Current prime is not prime
			if(currentPrime % prime == 0):
				isPrime = False
				break
		# Current prime is prime
		if(isPrime):
			primeList.append(currentPrime)
			if(Number % currentPrime == 0):
				print("Prime Factor: ", currentPrime)

def main():
	print("Solve Problem")

	FindLargestPrime(600851475143)


if __name__ == "__main__":
    main()