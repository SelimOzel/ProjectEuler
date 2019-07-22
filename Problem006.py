def SumOfSquares(n):
	sumResult = 0
	for i in range(1,n+1):
		sumResult += i*i
	return sumResult

def SquareOfSum(n):
	sumResult = 0
	for i in range(1,n+1):
		sumResult += i
	return sumResult*sumResult

def main():
	print("Solve Problem")

	print(SquareOfSum(100) - SumOfSquares(100))


if __name__ == "__main__":
    main()