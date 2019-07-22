# Multiples of 3 and 5
def Problem_01(n):
	sumOfMultiples = 0
	for i in range(n):
		if(i%3 == 0):
			sumOfMultiples += i
			continue
		if(i%5 == 0):
			sumOfMultiples += i
			continue
	print ("Sum is ", sumOfMultiples)


def main():
	print("Solve Problem")
	Problem_01(1000)


if __name__ == "__main__":
    main()