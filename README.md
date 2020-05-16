# Empirical-Analysis-Of-Algorithms
A comparative empirical time complexity analysis of some well-known computational algorithms by implementing those using three of the most popular programming languages — C++, Java and Python. These programming languages are differentiated under the characteristics of their
execution time and memory utilization. The implementation results are presented using a comparative analysis.

## Algorithms
* Sorting:
    * Bubble sort
    * Quick sort
    * Merge sort
* Graph Traversal
    * Breadth First Search (BFS)
    * Depth First Search (DFS)
* Greedy Algorithm
    * Dijkstra’s algorithm for Single Source Shortest Path
    * Prim’s algorithm for Minimum Spanning Tree
* Dynamic Programming
    * 0/1 Knapsack problem
    * Optimal Binary Search Tree (OBST)
* Backtracking
    * m-Colouring problem
    * n-Queens problem

## Tools used for anaylysis
* time Linux command:
The time command is used to determine how long a given command takes to run. It prints a summary of real-time, user CPU time and system CPU time spent on executing a command. ‘real‘ time is the time elapsed wall clock time taken, while ‘user‘ and ‘sys‘ time are the time taken in user and kernel mode respectively. For our analysis, we have taken into consideration the ‘real’ time.

* massif [Valgrind ](https://valgrind.org/) Valgrind tool for Linux:
Massif is a heap profiler. It measures how much heap memory your program uses. This includes both the useful space, and the extra bytes allocated for book-keeping and alignment purposes. It can also measure the size of your program’s stack(s), although it does not do so by default. Heap profiling can help you reduce the amount of memory your program uses.
