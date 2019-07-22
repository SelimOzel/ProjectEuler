# Fibonacci
def Fib(n):
	if(n==1):
		return 1
	if(n==2):
		return 2
	return(Fib(n-1)+Fib(n-2))

def main():
	print("Solve Problem")
	number = 0
	evenFibSum = 0
	fibIndex = 1
	while(number < 4000000):
		number = Fib(fibIndex)
		if(number % 2 == 0):
			evenFibSum += number
		print("Fibonacci Index 	: ", fibIndex)
		print("Fibonacci Number 	: ", number)
		print("Sum is, ", evenFibSum, " at index ", fibIndex, "." )

		fibIndex += 1

if __name__ == "__main__":
    main()