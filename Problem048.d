import std.stdio;
import std.datetime.stopwatch;
import std.bigint;

BigInt Solver(int input)
{
	BigInt counter = BigInt("0");
	BigInt sum = BigInt("0");
	for (int i = 0; i<input ; i++)
	{
		counter++;
		sum+=counter^^(i+1);
	}
	return sum;
}

void main() 
{ 
	auto t0 = StopWatch();
	t0.start();

	writeln("Solve Problem");
	writeln(Solver(1000));

	writeln("Clocked at: ", t0.peek.total!"usecs"/1000.0, " ms");
}