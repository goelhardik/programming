You're given a directed weighted graph with 44 nodes (AA, BB, CC, and DD) and 66 edges, defined below:

D→AD→A has weight aa
A→BA→B has weight bb
B→CB→C has weight cc
C→DC→D has weight dd
A→CA→C has weight ee
B→DB→D has weight ff
aa2.png

The total weight of a simple cycle is the sum of its edge weights (e.g.: A→C→D→AA→C→D→A has a total weight of e+d+ae+d+a). If the total weight is negative, it's called a negative cycle.

Given edge weights aa, bb, cc, dd, ee, and ff, find some minimum non-negative integer (pp) that, when added to one single edge weight in the graph, will get rid of any negative cycles.

Input Format

A single line containing 66 space-separated integers: aa, bb, cc, dd, ee, and ff, respectively.

Constraints

−20≤a,b,c,d,e,f≤20−20≤a,b,c,d,e,f≤20
Output Format

Print the minimum value of pp; if no non-negative pp will eliminate the negative cycle, print −1−1.

Sample Input

2 -5 0 1 1 1
Sample Output

2
Explanation

Adding 22 to bb (the weight of edge A→BA→B) will remove the negative cycle.
