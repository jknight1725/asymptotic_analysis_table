# asymptotic_analysis_table
Generates source code for html table of the Highest N solvable in a given time T 

Rows are the highest N solvable by an algorithm with the respective time complexity in the given time
assuming that the algorithm takes f(n) microseconds to solve

e.g.
more effiecient algorithm                 less efficient algorithm
time complexity: n                        time complexity: n^2
time(microseconds): 10^6                  time(microseconds): 10^6
highest N solvable: 10^6                  highest N solvable: 1000

In one second(10^6 microseconds) the algorithm running at time complexity n is 1000 times faster than the algorithm with time complexity n^2
