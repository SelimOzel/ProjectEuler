import time

def Solver(input):
	sum = 0
	for i in range(1,input+1):
		sum += pow(i,i)
	print(sum)

def main():
	t0 = time.process_time()

	print("Solve Problem")
	Solver(1000)

	print("Clocked at: ", (time.process_time()-t0)*1000, "ms")

if __name__ == "__main__":
    main()