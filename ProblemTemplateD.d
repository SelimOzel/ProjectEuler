import std.stdio;
import std.datetime.stopwatch;

void main() 
{ 
	auto t0 = StopWatch();

	writeln("Solve Problem");

	writeln("Clocked at: ", t0.peek.total!"msecs"/1000.0, " seconds");
}