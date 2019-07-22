def isPalindrome(n):
	myWord = str(n)
	for index in range(int(len(myWord)/2)):
		if(myWord[index] == myWord[len(myWord)-index-1]):
			continue
		else:
			return 0
	return 1

def main():
	print("Solve Problem")

	largestProduct = 0
	for i in range(1000,99,-1):
		for k in range(1000, 99,-1):
			product = i*k
			if(isPalindrome(product) == 1):
				print(i, " x ", k, " = ", product)
				if(largestProduct < product):
					largestProduct = product
	print(largestProduct)

if __name__ == "__main__":
    main()