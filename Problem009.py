import math

def isPythagorean(input):
	x = 1
	tripletList = []
	while(x <= input):
		y = 1
		while(y <= input):
			if (x*x + y*y == input*input):
				if(x < y ):
					tripletList.append([x, y])
			y += 1
		x += 1

	if(len(tripletList) == 0):
		return -1
	else:
		return tripletList

def main():
	
	print("Solve Problem")

	sumABC = 1000
	maxABC = 500
	for c in range (1, maxABC):
		result = isPythagorean(c)
		if(result != -1):
			resultFound = False
			for i in range (len(result)):
				a = result[i][0]
				b = result[i][1]
				print("Triplet: a = ", a, " b = ", b, " c = ", c)
				print("Sum: " , a+b+c)
				if(a + b + c == sumABC):
					print("Product: ", a*b*c)
					resultFound = True
					break
			if(resultFound):
				break


if __name__ == "__main__":
    main()