import time

def main():
	t0 = time.process_time()

	print("Solve Problem")

	print("Clocked at: ", (time.process_time()-t0)*1000, "ms")

if __name__ == "__main__":
    main()