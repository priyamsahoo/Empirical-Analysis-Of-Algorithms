/* A Naive recursive implementation of 0-1 Knapsack problem */
#include <bits/stdc++.h>
using namespace std;

// A utility function that returns maximum of two integers
int max(int a, int b) { return (a > b)? a : b; }

// Returns the maximum value that
// can be put in a knapsack of capacity W
int knapSack(int W, int wt[], int val[], int n)
{

// Base Case
if (n == 0 || W == 0)
	return 0;

// If weight of the nth item is more
// than Knapsack capacity W, then
// this item cannot be included
// in the optimal solution
if (wt[n-1] > W)
	return knapSack(W, wt, val, n-1);

// Return the maximum of two cases:
// (1) nth item included
// (2) not included
else return max( val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
					knapSack(W, wt, val, n-1) );
}

// Driver code
int main()
{
	int val[] = {20, 22, 26, 28, 29, 40, 42, 43, 52, 68, 74, 76, 81, 101, 144, 157, 162, 172, 174, 177, 208, 231, 232, 237, 241, 247, 260, 272, 276, 278};
	int wt[] = {12, 16, 23, 24, 29, 30, 38, 46, 53, 58, 59, 60, 62, 66, 68, 78, 79, 88, 89, 90, 107, 114, 118, 119, 123, 127, 128, 129, 136, 144};
	int W = 300;
	int n = sizeof(val)/sizeof(val[0]);
	cout<<knapSack(W, wt, val, n);
	return 0;
}

// This code is contributed by rathbhupendra
