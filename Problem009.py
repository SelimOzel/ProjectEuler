'''
a*a + a*b + a*c + b*a + b*b + b*c + c*a + c*b + c*c

a^2 + b^2 + c^2 + 2ab + 2ac + 2bc = 1000

c^2 + ab + ac + bc = 500
''' 

import math

def Triplet(input):
	x = 1
	while(x*x <= input):
		y = 1
		while(y*y <= input):
			if (x*x + y*y == input):
				return x, y
			y += 1
		x += 1

	return -1, -1

def Solve():
	summation = 0
	candidate = 1
	while(candidate < 500):
		x, y = Triplet(candidate*candidate)
		if (x != -1):
			summation = x + y + candidate
			print("x: ", x)
			print("y: ", y)
			print("z: ", candidate)
			print("Sum: ", summation)	
			print("Assert: ", x*x+y*y, " equals ", candidate*candidate)		
			if(int(summation) == int(1000)):
				print ("Solution: ", summation)
				return


		#print(summation)

		candidate += 1	

def main():
	Solve()
	print("Solve Problem")



if __name__ == "__main__":
    main()