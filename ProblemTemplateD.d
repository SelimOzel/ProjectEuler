import std.stdio;
import std.datetime.stopwatch;

void main() 
{ 
	auto t0 = StopWatch();
	t0.start();

	writeln("Solve Problem");

	writeln("Clocked at: ", t0.peek.total!"usecs"/1000.0, " ms");
}