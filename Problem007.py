def FindPrime(primeIndex):
	primeList = []
	currentPrime = 2
	primeList.append(currentPrime)
	currentPrime = 3
	primeList.append(currentPrime)

	while(len(primeList) < primeIndex):
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
			print("Prime at ", len(primeList), "is", currentPrime)


def main():
	print("Solve Problem")

	FindPrime(10001)


if __name__ == "__main__":
    main()